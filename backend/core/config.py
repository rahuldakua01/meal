import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, "..", ".env")
if not os.path.exists(env_path):
    env_path = os.path.join(current_dir, "..", "..", ".env")

load_dotenv(env_path)

APP_BASE_URL = os.getenv("APP_BASE_URL", "http://localhost:8000")
MAIL_USERNAME = os.getenv("MAIL")
MAIL_PASSWORD = os.getenv("PASS")
MAIL_FROM = os.getenv("MAIL")
MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")
