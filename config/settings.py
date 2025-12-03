"""
# Paths
# API URLs
# Environment settings (sandbox/production)
# Default container weight/volume settings
# Inventory forecast settings
# Function to load secrets.json

"""

import os
from pathlib import Path
from dotenv import load_dotenv

#--------------------------------
# Load environment variables (.env file)
# -------------------------------
# This load API keys and secret values from hidden .env file.
# Purpose: NEVER hardcode credentials inside Python files.
# Using os.getenv ("KEY") automatically grabs values from env.
load_dotenv()


#----------------------------------
# Project Path
# ---------------------------------
# BASE_DIR -> root folder of your project
# DATA_DIR -> where your local kdatabase or CSVs will be stored
# LOGS_DIR -> where log files will be written
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"


# Create the folders if they don't already exist.
# This prevents errors when the app tries to save files.
DATA_DIR.mkdir(exist_ok = True)
LOGS_DIR.mkdir(exist_ok = True)


# ------------------------------------
# QuickBooks API Credentials
# These come form the .env file to protect sensitive information.
# If a value isnt found, it defaults to an empty string or basic value
QB_CLIENT_ID = os.getenv("QB_CLIENT_ID", "")
QB_CLIENT_SECRET = os.getenv("QB_CLIENT_SECRET","")
QB_REDIRECT_URI = os.getenv("QB_REDIRECT_URI", "https://localhost:9000/callback")

# sandbox = testing, production = real live QUickbooks account
QB_ENVIRONMENT = os.getenv("QB_ENVIRONMENT", "sandbox")

# Realm ID = your company ID in QB
QB_REALM_ID = os.getenv("QB_REALM_ID", "")


# -------------------------------------
# Database Configuration
# --------------------------------------
# DB_TYPE decides what engine you are using (sqlite for now)
# DB_PATH id the file location for the SQLite database.
DB_TYPE = os.getenv("DB_TYPE", "sqlite")
DB_PATH = DATA_DIR / "masanta_inventory.db"


# If DB_URL is not set, default to SQLite URL
# SQLAlchemy uses this to connect to the database.
DB_URL = os.getenv("DB_URL", f"sqlite:///{DB_PATH}")


# --------------------------------------
# Inventory Forecasting & Buisness Rules
# --------------------------------------
# DEFAULT_LEAD_TIME_WEEKS -> how long a container takes to arrive (Masanta uses ~8 weeks)
# SAFETY_STOCK_WEEKS -> extra buffer inventroy 

#CHECK CHECK CHECK  MIN_ORDER_THRESHOLD -> reorder when remaining stock is under 30% 
DEFAULT_LEAD_TIME_WEEKS = 8
SAFETY_STOCK_WEEKS = 2
MIN_ORDER_THRESHOLD = 0.3


# --------------------------------------------
# Container Specifications (m^3 = cubic meters)
# --------------------------------------------
# These are internal volumes for standard shipping containers.
# You'll use this when building the "automatic container packing" algorithm
CONTAINER_SIZES ={
    "20ft": {"length_m":5.9, "width_m": 2.35, "height_m": 2.39, "volume_m3": 33.2},
    "40ft": {"length_m":12.03, "width_m": 2.35, "height_m": 2.39, "volume_m3": 67.7},
    "40hc": {"length_m":12.03, "width_m": 2.35, "height_m": 2.39, "volume_m3": 76.3},
}


# ----------------------------------------------
# Notifications (optional future feature)
# ----------------------------------------------
# If ENABLE_NOTIFICATIONS = true, app may email warnings:
# You're running low on T-HPD 15W50", etc.
ENABLE_NOTIFICATIONS = os.getenv("ENABLE_NOTIFICATIONS", "false").lower() =="true"
NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL", "")


# ------------------------------------------------
# Logging
# ------------------------------------------------
# LOG_LEVEL = the type of logs you want ("INFO", "DEBUG", "ERROR")
# LOG_FILE = where the app will write logs
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = LOGS_DIR / "masanta_app.log"