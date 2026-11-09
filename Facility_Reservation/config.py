import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "reservations.db")
ROOMS = [
    {"Name": "A101", "capacity":10},
    {"Name": "A102", "capacity":25},
    {"Name": "A201", "capacity":60},
]
ROLES = ["scheduler", "marketing", "admin"]
