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

# Weather History search 
def read_weather_history(file_path="data/weather_data.csv", limit=7):
    try:
        with open(file_path, mode='r') as file:
            reader = list(csv.reader(file))
            #skip header if prensent
            if reader and not reader[0][0].startswith('202'):
                reader = reader[1:]
            return reader[-limit:] #Get the last limit entries
    except FileNotFoundError:
        return []
        
            