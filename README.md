# Weather Dashboard 🌦️

This project is an interactive weather dashboard built with Python and Tkinter. It allows users to check real-time weather data for any city using the OpenWeatherMap API, log historical data, and view past temperature trends.

---

## 🧰 Features

- 🔍 **City Search**: Type a city name and get the current temperature and weather conditions.
- 🌆 **Quick Favorites**: One-click weather lookup for cities like New York, London, Tokyo, Miami, and Paris.
- 📈 **Weather History**: Logs each weather lookup and displays a history panel of recent queries.
- 🧊 **CSV Logging**: Saves weather lookups to a local `.csv` file.
- 📊 **Graphing (coming soon)**: A placeholder button is included to show a future temperature history graph.

---

## 🛠️ How It Works

1. The user enters a city name or clicks a favorite city.
2. The app uses the OpenWeatherMap API to fetch current weather.
3. The temperature and description are shown in the GUI.
4. The results are saved in a CSV file and displayed in a scrollable history panel.

---

## 📦 Folder Structure

weather-dashboard-Shomari/
│
├── main.py # Launches the Tkinter GUI
├── gui.py # GUI logic and widget setup
├── api_handler.py # Handles OpenWeatherMap API requests
├── config.py # Stores API key and default settings
├── file_manager.py # Saves to and reads from weather_data.csv
├── features/ # (Optional) For additional features like graphing
├── data/weather_data.csv # Weather history log (created at runtime)
├── .gitignore # Excludes pycache, .env, and .db files
└── README.md # You're reading it!
## 🚀 Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/Shomari-Thompson/weather-dashboard-Shomari.git
   run py main.py

   ## 💻 Requirements

- Python 3.8+
- `requests` library  
- `tkinter` (included with most Python installations)

To install `requests`, run:

```bash
pip install requests



