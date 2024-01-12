import datetime, os, appdirs

# Info for dirs
appName = "SuTiTaToR"
appAuthor = "roccat1"

logPath = os.path.join(appdirs.user_log_dir(appName, appAuthor), datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log")

#create log file
if not os.path.exists(os.path.dirname(logPath)):
    os.makedirs(os.path.dirname(logPath), exist_ok=True)

if os.path.exists(logPath):
    with open(logPath, "w") as f:
        f.write("")

def log(message):
    with open(logPath, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)

log("[START] log started")