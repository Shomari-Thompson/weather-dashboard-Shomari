import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
from api_handler import fetch_weather
from file_manager import save_weather_to_csv, read_weather_history


#Streamlit setup
st.set_page_config(page_title="Weather Dashboard", layout="wide")
st.title("🌤️ Advanced Weather Dashboard")

#City input
city = st.text_input("Enter a city")

#fetch and display weather 
if st.button("Get Weather"):
    data = fetch_weather(city)
    if data:
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"].capitalize()
        st.success(f"**{city}: {temp}°F, {desc}")
        save_weather_to_csv(city, data)
    else:
        st.error("Could not fetch weather data.")

# Favorites Selection
st.sidebar.header("💾 Favorite Cities")
favorite_cities = ["New York", "London", "Tokyo", "Miami", "Paris"]
for fav in favorite_cities:
    if st.sidebar.button(fav):
        city = fav
        data = fetch_weather(city)
        if data:
            temp = data["main"]["temp"]
            desc = data["Weather"][0]["description"].capitalize()
            st.success(f"**{city}**: {temp}°F, {desc}")
            same_weather_to_csv(city, data)

# Weather History Table
st.subheader("📜 Weather History")
history = read_weather_history()
if history:
    df = pd.DataFrame(history, columns=["Timestamp", "City", "Temperature", "Conditions"])
    df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
    st.dataframe(df.tail(10), use_container_width=True)

    #Plot temperature trend 
    st.subheader("📈 Temperature Trend")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df.sort_values("Timestamp")

    fig, ax = plt.subplots()
    ax.plot(df["Timestamp"], df["Temperature"], marker= 'o')
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°F)")
    ax.set_title("Temperature Over Time")
    ax.grid(True)
    st.pyplot(fig)
else:
    st.info("No history data found.")
    