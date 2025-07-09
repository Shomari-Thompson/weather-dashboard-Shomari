# file_manager.py

import csv
from datetime import datetime

def save_weather_to_csv(city, weather_data, file_path="data/weather_data.csv"):
    try:
        with open(file_path, mode= 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                city,
                weather_data.get("main",{}).get("temp"),
                weather_data.get("weather", [{}])[0].get("description")
            ])
        print(f"[INFO] Saved weather data for {city}")
    except Exception as e:
        print(f"[ERROR] Saving data failed: {e}")