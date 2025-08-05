import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from api_handler import fetch_weather
from file_manager import save_weather_to_csv, read_weather_history, clear_weather_history
from features.temperature_graph import plot_temperature_history
from features.background_manager import set_weather_background
from features.compare_cities import get_city_comparison
from features.settings_manager import load_settings, save_settings
import ttkbootstrap as tb
import threading
import re


class WeatherDashboard:

    def __init__(self, root):
        self.settings = load_settings()
        self.root = tb.Window(themename=self.settings.get("theme", "flatly"))
        self.style = self.root.style
        self.root.title("🌤️ Advanced Weather Dashboard")
        self.root.geometry("900x600")

        self.city = ttk.StringVar()
        self.favorite_city = ttk.StringVar()
        self.compare_city1 = ttk.StringVar()
        self.compare_city2 = ttk.StringVar()
        self.bg_label_holder = {"canvas": None}

        self.build_layout()

        for widget in self.root.winfo_children():
            widget.lift()

    def build_layout(self):
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(side=TOP, fill=X)

        self.sidebar = ttk.Labelframe(self.root, text="💾 Favorites", padding=10)
        self.sidebar.pack(side=LEFT, fill=Y, padx=10, pady=5)

        self.main = ttk.Labelframe(self.root, text="🌦️ Weather Panel", padding=10)
        self.main.pack(side=RIGHT, expand=YES, fill=BOTH, padx=10, pady=5)

        ttk.Label(top_frame, text="Enter City:").pack(side=LEFT, padx=5)
        ttk.Entry(top_frame, textvariable=self.city, width=30).pack(side=LEFT, padx=5)
        ttk.Button(top_frame, text="Get Weather", command=self.get_weather_in_background, bootstyle=PRIMARY).pack(side=LEFT, padx=5)
        ttk.Button(top_frame, text="Temperature Graph", command=self.plot_temperature_with_description, bootstyle=INFO).pack(side=LEFT, padx=5)
        ttk.Button(top_frame, text="Clear History", command=self.clear_and_refresh, bootstyle=DANGER).pack(side=LEFT, padx=5)
        ttk.Button(top_frame, text="Compare Cities", command=self.show_compare_cities, bootstyle=SUCCESS).pack(side=LEFT, padx=5)

        # Settings Dropdown
        settings_button = ttk.Menubutton(top_frame, text="⚙ Settings", direction="below")
        menu = ttk.Menu(settings_button, tearoff=0)
        settings_button["menu"] = menu

        themes = ["flatly", "darkly", "cyborg", "litera", "cosmo"]
        for t in themes:
            menu.add_command(label=t, command=lambda th=t: self.change_theme(th))

        menu.add_separator()
        menu.add_command(label="💾 Save Favorite Cities", command=self.save_favorites)
        settings_button.pack(side=LEFT, padx=5)

        ttk.Label(self.sidebar, text="Add City:").pack(pady=(10, 0))
        ttk.Entry(self.sidebar, textvariable=self.favorite_city, width=20).pack(pady=2)
        ttk.Button(self.sidebar, text="Add", command=self.add_favorite_city).pack(pady=2)

        for city in self.settings.get("favorite_cities", ["New York", "London", "Tokyo", "Miami", "Paris"]):
            self._create_favorite_button(city)

        self.result_label = ttk.Label(self.main, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=10)

        self.tree = ttk.Treeview(self.main, columns=("Time", "City", "Temp", "Humidity", "Condition"), show="headings", height=8, bootstyle="secondary")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        self.tree.pack(fill=X, pady=(10, 5))

        self.bg_canvas = ttk.Canvas(self.main, height=160)
        self.bg_canvas.pack(fill=BOTH, expand=False, pady=(0, 5))
        self.bg_label_holder["canvas"] = self.bg_canvas

        self.update_history_table()

    def _create_favorite_button(self, city):
        frame = ttk.Frame(self.sidebar)
        frame.pack(fill=X, pady=2)

        ttk.Button(frame, text=city, width=15, command=lambda c=city: self.get_weather(c)).pack(side=LEFT)
        ttk.Button(frame, text="❌", width=3, command=frame.destroy, bootstyle=DANGER).pack(side=RIGHT)

    def add_favorite_city(self):
        city = self.favorite_city.get().strip()
        if not city or len(city) < 2 or not re.match(r"^[A-Za-z\s\-]+$", city):
            messagebox.showwarning("Invalid Input", "Enter a valid city name.")
            return

        for child in self.sidebar.winfo_children():
            if isinstance(child, ttk.Frame):
                for widget in child.winfo_children():
                    if isinstance(widget, ttk.Button) and widget.cget("text").lower() == city.lower():
                        messagebox.showinfo("Duplicate", f"{city} already exists.")
                        return

        self._create_favorite_button(city)
        self.favorite_city.set("")

    def get_weather_in_background(self, city_override=None):
        threading.Thread(target=lambda: self.get_weather(city_override), daemon=True).start()

    def get_weather(self, city_override=None):
        city = city_override if city_override else self.city.get()
        if not city:
            messagebox.showerror("Input Error", "Enter a city.")
            return

        data = fetch_weather(city)
        if data:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            condition = data["weather"][0]["main"]

            self.result_label.config(text=f"{city}: {temp}°F, {desc}")
            set_weather_background(self.bg_label_holder["canvas"], condition)
            self.apply_theme_based_on_weather(condition)

            save_weather_to_csv(city, data)
            self.update_history_table()
        else:
            messagebox.showerror("Error", "Failed to fetch weather.")

    def apply_theme_based_on_weather(self, condition):
        theme_map = {
            "Clear": "flatly",
            "Clouds": "litera",
            "Rain": "darkly",
            "Snow": "morph",
            "Thunderstorm": "cyborg"
        }
        theme = theme_map.get(condition, "cosmo")
        self.root.style.theme_use(theme)
        self.settings["theme"] = theme
        save_settings(self.settings)

    def change_theme(self, theme):
        self.root.style.theme_use(theme)
        self.settings["theme"] = theme
        save_settings(self.settings)

    def save_favorites(self):
        favorites = []
        for child in self.sidebar.winfo_children():
            if isinstance(child, ttk.Frame):
                for widget in child.winfo_children():
                    if isinstance(widget, ttk.Button) and widget.cget("text") != "❌":
                        favorites.append(widget.cget("text"))
        self.settings["favorite_cities"] = favorites
        save_settings(self.settings)
        messagebox.showinfo("Saved", "Favorite cities saved.")

    def update_history_table(self):
        self.tree.delete(*self.tree.get_children())
        for row in read_weather_history()[-10:]:
            self.tree.insert("", "end", values=row)

    def clear_and_refresh(self):
        clear_weather_history()
        self.update_history_table()

    def plot_temperature_with_description(self):
        try:
            plot_temperature_history()
            import random
            desc = random.choice([
                "Temps are rising steadily.",
                "Dip in midweek = cold front?",
                "Mild fluctuations seen.",
                "Spikes = unstable patterns."
            ])
            messagebox.showinfo("Graph Insight", desc)
        except Exception as e:
            messagebox.showerror("Error", f"Graph error: {e}")

    def show_compare_cities(self):
        results = get_city_comparison()
        if not results:
            messagebox.showinfo("Compare Cities", "No comparison data.")
            return

        top = ttk.Toplevel(self.root)
        top.title("Compare Cities")

        ttk.Label(top, text="Select City 1").pack(pady=5)
        city1_cb = ttk.Combobox(top, textvariable=self.compare_city1, values=[r[0] for r in results])
        city1_cb.pack(pady=5)

        ttk.Label(top, text="Select City 2").pack(pady=5)
        city2_cb = ttk.Combobox(top, textvariable=self.compare_city2, values=[r[0] for r in results])
        city2_cb.pack(pady=5)

        def show_selected():
            selected = [r for r in results if r[0] in [self.compare_city1.get(), self.compare_city2.get()]]
            compare_window = ttk.Toplevel(top)
            tree = ttk.Treeview(compare_window, columns=("City", "Temp", "Humidity", "Condition", "Score"), show="headings")
            for col in tree["columns"]:
                tree.heading(col, text=col)
                tree.column(col, width=120)
            tree.pack(fill=BOTH, expand=True)
            for row in selected:
                tree.insert("", "end", values=row)

        ttk.Button(top, text="Compare", command=show_selected).pack(pady=10)


def main():
    app = WeatherDashboard(None)
    app.root.mainloop()


if __name__ == "__main__":
    main()
