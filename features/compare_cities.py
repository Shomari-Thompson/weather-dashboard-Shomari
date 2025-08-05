import csv
import os

def get_available_cities():
    """Return a sorted list of cities found in the latest team_weather_data file."""
    try:
        file_path = get_latest_csv()
        if not file_path:
            return []
        
        cities = set()
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                city = row.get("city") or row.get("City")
                if city:
                    cities.add(city.strip())

        return sorted(cities)
    except Exception as e:
        print(f"[City List Error] {e}")
        return []

def get_latest_csv():
    folder = os.path.join("New_Team_Dashboard", "exports")
    latest_file = None
    latest_time = 0

    if not os.path.exists(folder):
        return None

    for fname in os.listdir(folder):
        if fname.startswith("team_weather_data") and fname.endswith(".csv"):
            full_path = os.path.join(folder, fname)
            if os.path.getmtime(full_path) > latest_time:
                latest_file = full_path
                latest_time = os.path.getmtime(full_path)

    return latest_file

def get_city_comparison(selected_cities=None):
    """Return comparison results, optionally filtered by selected cities"""
    try:
        file_path = get_latest_csv()
        if not file_path:
            print("[Compare Error] ❌ No team_weather_data CSV file found.")
            return []

        comparison_results = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            city_data = {}

            for row in reader:
                city = row.get("city") or row.get("City")
                if not city:
                    continue
                city = city.strip()
                if selected_cities and city not in selected_cities:
                    continue

                try:
                    temp = float(row.get("temperature") or row.get("Temperature") or 0)
                    humidity = float(row.get("humidity") or row.get("Humidity") or 0)
                except ValueError:
                    continue

                condition = row.get("weather_main") or row.get("Weather") or "Unknown"

                if city not in city_data:
                    city_data[city] = {"temps": [], "humidities": [], "conditions": []}

                city_data[city]["temps"].append(temp)
                city_data[city]["humidities"].append(humidity)
                city_data[city]["conditions"].append(condition)

        for city, values in city_data.items():
            if not values["temps"] or not values["humidities"]:
                continue

            avg_temp_c = sum(values["temps"]) / len(values["temps"])
            avg_temp_f = round((avg_temp_c * 9/5) + 32, 1)
            avg_humidity = round(sum(values["humidities"]) / len(values["humidities"]), 1)
            common_condition = max(set(values["conditions"]), key=values["conditions"].count)
            score = 100 - abs(avg_temp_f - 70) - abs(avg_humidity - 50)
            score = max(0, round(score, 1))

            comparison_results.append((city, avg_temp_f, avg_humidity, common_condition, score))

        return sorted(comparison_results, key=lambda x: x[-1], reverse=True)

    except Exception as e:
        print(f"[Compare Error] {e}")
        return []
