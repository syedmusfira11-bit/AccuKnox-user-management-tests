#!/usr/bin/env python3
import requests
import time
from datetime import datetime

URLS_TO_MONITOR = [
    "https://opensource-demo.orangehrmlive.com",
    "https://www.google.com",
    "https://www.github.com"
]

CHECK_INTERVAL = 30  # seconds
LOG_FILE = "app_health.log"

def log_message(message):
    """Write log messages with timestamps."""
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {message}\n")
    print(message)

def check_app_health():
    """Check HTTP status codes of the monitored URLs."""
    for url in URLS_TO_MONITOR:
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code

            if status_code == 200:
                log_message(f"✅ {url} is UP (HTTP {status_code})")
            else:
                log_message(f"⚠️ {url} is DOWN (HTTP {status_code})")

        except requests.exceptions.RequestException as e:
            log_message(f"❌ {url} is DOWN - Error: {e}")

if __name__ == "__main__":
    log_message("----- Starting Application Health Check -----")
    try:
        while True:
            check_app_health()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        log_message("🛑 Health check stopped by user.")
