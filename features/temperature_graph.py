import pandas as pd
import matplotlib.pyplot as plt

def plot_temperature_history(file_path="data/weather_data.csv"):
    try:
        # Read the CSV file, skipping the header row
        df = pd.read_csv(file_path, names=["timestamp", "city", "temperature", "description"], skiprows=1)

        # Convert timestamp strings to datetime objects
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

        # Create and show the plot
        plt.figure(figsize=(10, 4))
        plt.plot(df["timestamp"], df["temperature"], marker="o", linestyle="-", color="blue")
        plt.title("Temperature History")
        plt.xlabel("Date & Time")
        plt.ylabel("Temperature (°F)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(True)
        plt.show()  # ✅ This now runs in the main thread and works properly

    except FileNotFoundError:
        print("[ERROR] Weather data file not found. Please run some searches first!")
    except Exception as e:
        print(f"[ERROR] Could not plot temperature history: {e}")
