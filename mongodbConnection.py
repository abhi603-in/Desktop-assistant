from urllib.parse import quote_plus
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection string
userName = "admin"
raw_password = "admin@123"
password = quote_plus(raw_password)
MONGO_URI = f"mongodb+srv://{userName}:{password}@cluster0.qudjlui.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["desktop_assistant"] 
command_logs = db["command_logs"]


def log_command(command_text, command_type, success=True, mode="offline"):
    log_entry = {
        "command": command_text,
        "type": command_type,
        "timestamp": datetime.now(),
        "success": success,
        "mode": mode
    }
    command_logs.insert_one(log_entry)

def try_log_command(command_text, command_type, success=True, mode="offline"):
    try:
        log_command(command_text, command_type, success, mode)
    except Exception as e:
        print(f"Error logging command: {e}")