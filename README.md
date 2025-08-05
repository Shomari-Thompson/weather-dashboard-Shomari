🌤️ Weather Dashboard – Tkinter Bootstrap Edition
This project is a desktop-based Advanced Weather Dashboard built with Python and ttkbootstrap (Tkinter + Bootstrap). It enables users to view real-time weather data, visualize trends, save personal settings, and compare multiple cities using a clean, modern GUI.

🧰 Features
🔍 City Search
Enter any city and view current temperature, humidity, and conditions via the OpenWeatherMap API.

🌆 Favorite Cities
Save and quickly access frequently searched cities, with options to remove or persist them across sessions.

🎨 Dynamic Theme Switching
Automatically adjusts the dashboard color theme based on current weather conditions, or manually select your preferred theme from the settings dropdown.

🛠️ Settings Menu
A settings dropdown lets you save favorite cities and switch between themes. Preferences are saved to a JSON settings file.

🧠 Compare Cities (with Dropdown)
Select cities from your team’s shared CSV dataset via a dropdown and compare them by temperature, humidity, condition, and a comfort-based score.

📜 Weather History Log
Automatically logs each city search to a CSV and shows the 10 most recent entries in a table.

📈 Temperature Graph
Displays a graph of recent temperatures using Matplotlib, with randomized weather insights.

🔐 Secure API Access
API credentials are stored in a .env file using python-dotenv.

✅ Modular Architecture
Organized into reusable components:

api_handler.py

file_manager.py

features/temperature_graph.py

features/background_manager.py

features/compare_cities.py

features/settings_manager.py

🛠️ How It Works
User enters a city name or selects from favorites.

The app fetches real-time weather data via OpenWeatherMap API.

It logs the result in a CSV and displays weather info and condition-based background.

The user can visualize data with a graph or compare cities using shared CSV inputs.

Preferences like theme and saved cities are stored in a local settings JSON file.

🚀 Getting Started
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Shomari-Thompson/weather-dashboard-Shomari.git
cd weather-dashboard-Shomari-main
2. Install required packages
bash
Copy
Edit
pip install ttkbootstrap requests python-dotenv pandas matplotlib
3. Create a .env file
In the root directory, add the following without quotes:

ini
Copy
Edit
API_KEY=your_openweathermap_api_key
BASE_URL=https://api.openweathermap.org/data/2.5/weather
DEFAULT_CITY=New York
4. Run the app
bash
Copy
Edit
python main.py
📂 Project Structure
bash
Copy
Edit
weather-dashboard/
│
├── main.py                        # Main GUI (Tkinter + ttkbootstrap)
├── api_handler.py                 # Weather API fetch logic
├── file_manager.py                # Read/write CSV history
├── .env                           # API key and config (not in Git)
├── config.py                      # Loads environment variables
├── data/
│   └── weather_data.csv           # Weather history logs
├── New_Team_Dashboard/exports/    # Shared CSV data for Compare Cities
├── features/
│   ├── background_manager.py      # Weather-based background setting
│   ├── compare_cities.py          # Ranking system + dropdown UI
│   ├── temperature_graph.py       # Matplotlib graph logic
│   └── settings_manager.py        # Load/save themes and favorites
├── requirements.txt (optional)
└── README.md                      # You're reading it!