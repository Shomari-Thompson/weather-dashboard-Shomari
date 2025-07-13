# config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
DEFAULT_CITY = "New York"
