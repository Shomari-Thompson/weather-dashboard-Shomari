import tkinter as tk
from tkinter import messagebox
from api_handler import fetch_weather
from file_manager import save_weather_to_csv, read_weather_history

def run_gui():
    # Function to update the weather history
    def update_history_display():
        history = read_weather_history()
        history_text.delete(1.0, tk.END)
        for row in history:
            history_text.insert(tk.END, f"{row[0]} - {row[1]}: {row[2]}°F, {row[3]}\n")

    # Function to fetch weather and update everything
    def get_weather():
        city = city_entry.get()
        data = fetch_weather(city)
        if data:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            result_label.config(text=f"{city}: {temp}°F, {description}")
            save_weather_to_csv(city, data)
            update_history_display()  # Refresh history after saving
        else:
            messagebox.showerror("Error", "Could not fetch weather data.")

    # GUI Setup
    root = tk.Tk()
    root.title("Weather Dashboard")

    tk.Label(root, text="Enter city:").pack()
    city_entry = tk.Entry(root)
    city_entry.pack()

    tk.Button(root, text="Get Weather", command=get_weather).pack()

    result_label = tk.Label(root, text="")
    result_label.pack()

    # Weather History section with scrollbar
    history_frame = tk.Frame(root)
    history_frame.pack()

    history_scrollbar = tk.Scrollbar(history_frame)
    history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    history_text = tk.Text(history_frame, height=10, width=50, yscrollcommand=history_scrollbar.set)
    history_text.pack(side=tk.LEFT, fill=tk.BOTH)

    history_scrollbar.config(command=history_text.yview)

    # Show existing history on startup
    update_history_display()

    root.mainloop()
