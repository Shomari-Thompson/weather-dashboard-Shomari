import csv
import os

def get_city_comparison():
    try:
        file_path = os.path.join("New_Team_Dashboard", "exports")
        latest_file = None
        latest_mtime = 0

        # Find the most recent team_weather_data CSV
        for fname in os.listdir(file_path):
            if fname.startswith("team_weather_data_20250728_193953") and fname.endswith(".csv"):
                full_path = os.path.join(file_path, fname)
                if os.path.getmtime(full_path) > latest_mtime:
                    latest_file = full_path
                    latest_mtime = os.path.getmtime(full_path)

        if not latest_file:
            return []

        comparison_results = []
        with open(latest_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            city_data = {}

            for row in reader:
                city = row.get("city") or row.get("City", "Unknown")
                try:
                    temp = float(row.get("temperature") or row.get("Temperature (F)", 0))
                    humidity = float(row.get("humidity") or 0)
                except ValueError:
                    continue  # Skip rows with invalid numeric data

                condition = row.get("weather_main") or row.get("Weather", "N/A")

                if city not in city_data:
                    city_data[city] = {
                        "temps": [],
                        "humidities": [],
                        "conditions": []
                    }

                city_data[city]["temps"].append(temp)
                city_data[city]["humidities"].append(humidity)
                city_data[city]["conditions"].append(condition)

        for city, values in city_data.items():
            if not values["temps"] or not values["humidities"]:
                continue  # Skip cities with missing data

            avg_temp_c = sum(values["temps"]) / len(values["temps"])
            avg_temp_f = round((avg_temp_c * 9/5) + 32, 1)  # 🔥 Convert to Fahrenheit
            avg_humidity = round(sum(values["humidities"]) / len(values["humidities"]), 1)
            common_condition = max(set(values["conditions"]), key=values["conditions"].count)
            score = 100 - abs(avg_temp_f - 70) - abs(avg_humidity - 50)
            score = max(0, round(score, 1))

            comparison_results.append((city, avg_temp_f, avg_humidity, common_condition, score))

        return sorted(comparison_results, key=lambda x: x[-1], reverse=True)

    except Exception as e:
        print(f"[Compare Error] {e}")
        return []
