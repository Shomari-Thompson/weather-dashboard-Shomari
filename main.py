import tkinter as tk
from tkinter import ttk, messagebox
from api_handler import fetch_weather
from file_manager import save_weather_to_csv, read_weather_history
from features.temperature_graph import plot_temperature_history
from file_manager import clear_weather_history
import threading


class WeatherDashboard:

    def plot_temperature_with_description(self):
        try:
            from features.temperature_graph import plot_temperature_history
            plot_temperature_history()

            description = [
                "Temperatures have been steadily rising over the past few days.",
                "Notice the dip during the midweek - possibly due to a cold front.",
                "This graph shows stable weather with mild fluctuations.",
                "Large spikes could indicate inconsistent weather patterns"
            ]
            import random
            desc = random.choice(description)
            messagebox.showinfo("Graph Insight", desc)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display graph:\n{e}")

    def get_weather_in_background(self, city_override=None):
        threading.Thread(target=lambda: self.get_weather(city_override), daemon=True).start()

    def __init__(self, root):
        self.root = root
        self.root.title("🌤️ Advanced Weather Dashboard")
        self.root.geometry("800x600")

        self.city = tk.StringVar()
        self.favorite_city = tk.StringVar()

        self.build_layout()

    def build_layout(self):
        # Frames
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.sidebar_frame = ttk.LabelFrame(self.root, text="💾 Favorite Cities", padding=10)
        self.sidebar_frame.grid(row=1, column=0, sticky="ns", padx=10, pady=5)

        main_frame = ttk.LabelFrame(self.root, text="🌦️ Weather Panel", padding=10)
        main_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Top input area
        ttk.Label(top_frame, text="Enter a city:").pack(side="left")
        ttk.Entry(top_frame, textvariable=self.city, width=25).pack(side="left", padx=5)
        ttk.Button(top_frame, text="Get Weather", command=self.get_weather_in_background).pack(side="left", padx=5)
        ttk.Button(top_frame, text="Show Temperature Graph", command=self.plot_temperature_with_description).pack(side="left", padx=5)
        ttk.Button(top_frame, text="Clear History", command=lambda: [clear_weather_history(), self.update_history_display()]).pack(pady=5)

        # Favorite city input
        ttk.Label(self.sidebar_frame, text="Add Favorite City:").pack(pady=(10, 0))
        ttk.Entry(self.sidebar_frame, textvariable=self.favorite_city, width=20).pack(pady=2)
        ttk.Button(self.sidebar_frame, text="Add", command=self.add_favorite_city).pack(pady=2)

        # Add default favorites
        default_favorites = ["New York", "London", "Tokyo", "Miami", "Paris"]
        for city in default_favorites:
            self._create_favorite_button(city)

        # Result label
        self.result_label = ttk.Label(main_frame, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Table
        self.tree = ttk.Treeview(main_frame, columns=("Time", "City", "Temp", "Humidity", "Condition"), show="headings", height=8)
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True, pady=10)

        self.update_history_table()

    def _create_favorite_button(self, city):
        ttk.Button(self.sidebar_frame, text=city, command=lambda c=city: self.get_weather(c)).pack(fill="x", pady=2)

    def add_favorite_city(self):
        city = self.favorite_city.get().strip()
        if not city:
            messagebox.showwarning("Input Error", "Please enter a valid city name.")
            return

        # Prevent duplicates
        for child in self.sidebar_frame.winfo_children():
            if isinstance(child, ttk.Button) and child.cget("text").lower() == city.lower():
                messagebox.showinfo("Duplicate", f"'{city}' is already in your favorites.")
                return

        self._create_favorite_button(city)
        self.favorite_city.set("")

    def get_weather(self, city_override=None):
        city = city_override if city_override else self.city.get()
        if not city:
            messagebox.showerror("Input Error", "Please enter a city name.")
            return

        data = fetch_weather(city)
        if data:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            self.result_label.config(text=f"{city}: {temp}°F, {desc}")
            save_weather_to_csv(city, data)
            self.update_history_table()
        else:
            messagebox.showerror("API Error", "Failed to fetch weather data.")

    def update_history_table(self):
        self.tree.delete(*self.tree.get_children())
        history = read_weather_history()
        if history:
            for row in history[-10:]:
                self.tree.insert("", "end", values=row)

    def update_history_display(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        history = read_weather_history()
        for row in history:
            try:
                self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3], row[4]))
            except IndexError:
                continue

                

def main():
    root = tk.Tk()
    app = WeatherDashboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
