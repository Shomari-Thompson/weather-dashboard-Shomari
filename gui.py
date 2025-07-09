# gui.py

import tkinter as tk
from tkinter import messagebox
from api_handler import fetch_weather
from file_manager import save_weather_to_csv

def run_gui():
    def get_weather():
        city = city_entry.get()
        data = fetch_weather(city)
        if data:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            result_label.config(text=f"{city}: {temp}°F, {description}")
            save_weather_to_csv(city, data)
        else:
            messagebox.showerror("Error", "Could not fetch weather data.")

    #Gui Setup
    root = tk.Tk()
    root.title("Weather Dashboard")

    tk.Label(root, text="Enter city:").pack()
    city_entry = tk.Entry(root)
    city_entry.pack()

    tk.Button(root, text="Get Weather", command=get_weather).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
