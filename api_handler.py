# api_handler.p

import requests
from config import API_KEY, BASE_URL

def fetch_weather(city):
    try:
        params = {'q': city, 'appid': API_KEY, 'units': 'imperial'}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[ERROR] API request failed: {e}")
        return None
    
    