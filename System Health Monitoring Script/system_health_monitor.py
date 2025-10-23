import psutil
import time
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80      # in percentage
MEMORY_THRESHOLD = 80   # in percentage
DISK_THRESHOLD = 80     # in percentage

# Log file
LOG_FILE = "system_health.log"


def log_message(message):
    """Write message to log file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)


def check_system_health():
    """Check CPU, Memory, Disk, and Process stats."""
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    process_count = len(psutil.pids())

    log_message(f"CPU Usage: {cpu_usage}%")
    log_message(f"Memory Usage: {memory.percent}%")
    log_message(f"Disk Usage: {disk.percent}%")
    log_message(f"Running Processes: {process_count}")

    # Check thresholds
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"⚠️ ALERT: High CPU usage detected: {cpu_usage}%")
    if memory.percent > MEMORY_THRESHOLD:
        log_message(f"⚠️ ALERT: High Memory usage detected: {memory.percent}%")
    if disk.percent > DISK_THRESHOLD:
        log_message(f"⚠️ ALERT: Disk space usage critical: {disk.percent}%")

    log_message("-" * 50)


if __name__ == "__main__":
    log_message("=== Starting System Health Monitor ===")

    # You can change the interval below (e.g., check every 60 seconds)
    while True:
        check_system_health()
        time.sleep(30)  # check every 30 seconds
