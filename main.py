import scripts.UI as UI
import scripts.log as log
import scripts.client.connect as connect
import scripts.game as game

__author__ = "github.com/roccat1"

if __name__ == "__main__":
    log.log("[START] main started")

    # Connect to server
    connect.connect("127.0.0.1", 55555, "nicholas")
    game.online_mode = True
    game.player = 1
    UI.UI()