import datetime, os

logPath = "log.txt"

if os.path.exists(logPath):
    with open(logPath, "w") as f:
        f.write("")

def log(message):
    with open(logPath, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

log("[START] log started")