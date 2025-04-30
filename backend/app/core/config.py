# app/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "fallback-secret-key")
    DEEP_SEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY", "fallback-secret-key")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "fallback-secret-key")

settings = Settings()
