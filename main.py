
__author__ = "github.com/roccat1"
 

if __name__ == "__main__":
    # Download libraries
    import os
    try:
        import datetime, appdirs, tkinter, webbrowser, PIL, functools, socket, threading
    except ImportError:
        os.system("pip install appdirs")
        os.system("pip install pillow")

    import scripts.log as log
    import scripts.UI.mainMenuUI as mainMenuUI

    log.log("[START] main started, log at: " + log.logPath)

    # Start UI
    mainMenuUI.mainWindowUI()