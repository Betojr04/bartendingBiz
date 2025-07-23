import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "devkey")  # Replace in production
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///bartending.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
