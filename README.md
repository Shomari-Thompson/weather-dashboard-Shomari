# 🌤️ Weather Dashboard – Streamlit Edition

This project is a modern, browser-based **weather dashboard** built with Python and Streamlit. It allows users to check real-time weather data for any city using the OpenWeatherMap API, log historical queries, and visualize temperature trends over time.

Originally created with a Tkinter GUI, the project has evolved into a professional-looking web dashboard with improved user experience and extensibility for future machine learning features.

---

## 🧰 Features

- 🔍 **City Search**: Enter any city and get its current temperature and weather conditions.
- 🌆 **Quick Favorites**: Instantly check weather for common cities (New York, London, Tokyo, etc.).
- 📜 **Weather History Log**: Stores each lookup in a CSV file and displays the latest queries.
- 📈 **Temperature Graph**: Visualizes recent temperature trends with time-series plotting.
- 🔒 **Secure API Integration**: Uses a `.env` file for credentials and `python-dotenv` to manage secrets.
- ✅ **Modular Design**: Code is separated into logical components (API handling, file saving, UI).
- 🌐 **Streamlit UI**: Clean, modern interface with live updates — no Tkinter windows needed.
- 📦 **Planned**: Predictive temperature modeling (using lag features and regression).

---

## 🛠️ How It Works

1. The user enters a city name or clicks a favorite city in the sidebar.
2. The app uses the OpenWeatherMap API to fetch current weather data.
3. The temperature and condition are displayed instantly.
4. The data is logged into a CSV file (`data/weather_data.csv`).
5. The app loads recent history and shows a line chart of past temperatures.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Shomari-Thompson/weather-dashboard-Shomari.git
cd weather-dashboard-Shomari-main
    2. Install required packages
    pip install streamlit requests python-dotenv pandas matplotlib
    3. Add your .env file Create a file named .env in the root directory with the following content:
    API_KEY=your_openweathermap_api_key
BASE_URL=https://api.openweathermap.org/data/2.5/weather
DEFAULT_CITY=New York
     4. Run the app
     streamlit run main.py
weather-dashboard/
│
├── main.py               # Streamlit app entry point
├── api_handler.py        # Handles API requests to OpenWeatherMap
├── config.py             # Loads environment variables securely
├── file_manager.py       # Saves to and reads from weather_data.csv
├── data/weather_data.csv # CSV log of weather lookups
├── .env                  # API keys (excluded from Git)
├── .gitignore            # Files to ignore in version control
└── README.md             # Project documentation
