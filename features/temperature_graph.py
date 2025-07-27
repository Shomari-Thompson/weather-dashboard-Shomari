import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Toplevel, Label, Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

def plot_temperature_history():
    try:
        df = pd.read_csv("data/weather_data.csv", names=["timestamp", "city", "temperature","humidity", "description"], skiprows=1)
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")

        # Create new window
        graph_window = Toplevel()
        graph_window.title("📈 Temperature Trend")
        graph_window.geometry("800x400")
        graph_window.resizable(True, True)

        # Container for layout
        container = Frame(graph_window)
        container.pack(fill="both", expand=True)

        # Create figure
        fig, ax = plt.subplots(figsize=(6, 3))
        ax.plot(df["timestamp"], df["temperature"], marker="o", linestyle="-", color="blue")
        ax.set_title("Temperature Over Time")
        ax.set_xlabel("Date & Time")
        ax.set_ylabel("Temperature (°F)")
        ax.grid(True)
        fig.autofmt_xdate(rotation=30, ha='right')

        # Embed the figure in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=container)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", fill="both", expand=True)

        # Random summary text
        summary_texts = [
            "Steady temperatures with slight variations.",
            "Recent spike in temperature suggests a heatwave.",
            "Cooling trend observed over the past few days.",
            "Data shows consistent mild weather conditions.",
            "Unusual temperature fluctuations noted."
        ]
        summary = Label(
            container,
            text="Summary:\n\n" + random.choice(summary_texts),
            font=("Arial", 11),
            justify="left",
            wraplength=180
        )
        summary.pack(side="right", padx=10, pady=10)

    except FileNotFoundError:
        print("[ERROR] Weather data file not found.")
    except Exception as e:
        print(f"[ERROR] Could not plot temperature history: {e}")
