# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()
# Fetch .env configs in one place to avoid fetching it in other modules
class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "fallback-secret-key")

settings = Settings()
