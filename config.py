import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local dev)
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Required for Render DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
