# 🌤️ Weather Dashboard – Tkinter Edition

This project is a desktop-based **Weather Dashboard** built with Python and **Tkinter**. It allows users to check real-time weather data for any city using the OpenWeatherMap API, save and view historical weather logs, and visualize temperature trends with Matplotlib — all from a clean, interactive GUI.

---


## 🧰 Features

- 🔍 **City Search**: Enter any city and view current temperature and conditions.
- 🌆 **Favorite Cities**: Quickly access weather data for common cities (New York, London, Tokyo, etc.).
- 📜 **Weather History Log**: Automatically logs each lookup into a CSV file and displays recent history.
- 📈 **Temperature Graph**: Embedded line graph showing recent temperature trends, with random summaries.
- 🔒 **Secure API Integration**: Uses a `.env` file and `python-dotenv` to securely load API keys.
- ✅ **Modular Design**: Organized into components like `api_handler`, `file_manager`, and `temperature_graph`.
- 🖼️ **Personal Enhancement**: Adds personality through tooltips, emojis, and weather insights.

---

## 🛠️ How It Works

1. The user enters a city name or selects one from the favorite city list.
2. The app fetches real-time weather data from the OpenWeatherMap API.
3. The results are displayed in the GUI and saved to a local CSV log.
4. Users can view recent weather history in a table or generate a temperature trend graph.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Shomari-Thompson/weather-dashboard-Shomari.git
cd weather-dashboard-Shomari-main
### 2. pip install requests python-dotenv pandas matplotlib
### 3 reate a .env file in the root directory with the following content (no quotes or spaces):
##API_KEY=your_openweathermap_api_key
##BASE_URL=https://api.openweathermap.org/data/2.5/weather
##DEFAULT_CITY=New York
### 4 Run the App python main.py
weather-dashboard/
│
├── main.py               # Tkinter GUI entry point
├── api_handler.py        # Handles API requests
├── config.py             # Loads environment variables
├── file_manager.py       # Saves and reads CSV weather history
├── temperature_graph.py  # Embedded graph plotting logic
├── data/weather_data.csv # Log file of weather lookups
├── .env                  # Stores API credentials (not tracked by Git)
├── .gitignore            # Version control exclusions
└── README.md             # Project documentation

