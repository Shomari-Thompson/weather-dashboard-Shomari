import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
DEFAULT_CITY = "New York"
