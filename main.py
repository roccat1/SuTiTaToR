import scripts.UI.boardUI as boardUI
import scripts.log as log
import scripts.client.connect as connect
import scripts.game as game
import scripts.UI.mainMenuUI as mainMenuUI

__author__ = "github.com/roccat1"

if __name__ == "__main__":
    log.log("[START] main started, log at: " + log.logPath)

    # Start UI
    mainMenuUI.mainWindowUI()