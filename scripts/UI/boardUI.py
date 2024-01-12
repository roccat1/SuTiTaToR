import tkinter as tk, os
from PIL import ImageTk, Image
from functools import partial

import scripts.log as log
import scripts.game as game
import scripts.client.client as client

online_mode = False

log.log("[START] UI started")

ASSETS_PATH = "assets/"
IMAGEFORMAT = ".png"

# create panels
panels = [[[[0 for col in range(3)] for row in range(3)] for g_col in range(3)] for g_row in range(3)]
infoLabel = None

player_to_sign = {1: "O", 2: "X"}
player_to_sign_anti = {1: "X", 2: "O"}

def exit() -> None:
    """exit"""
    global window
    window.destroy()
    os._exit(0)

def set_image_mini_game_ended(g_row: int, g_col: int, player: int) -> None:
    """Updates the image at the given game to the winning image of the player

    Args:
        g_row (int): grid row
        g_col (int): grid column
        player (int): player win
    """
    if player == 2:
        # O
        update_image(g_row, g_col, 1, 1, "blank", 0)
        update_image(g_row, g_col, 0, 0, "O_large_diagonal", 0) 
        update_image(g_row, g_col, 0, 2, "O_large_diagonal", 270)
        update_image(g_row, g_col, 2, 0, "O_large_diagonal", 90)
        update_image(g_row, g_col, 2, 2, "O_large_diagonal", 180)
        update_image(g_row, g_col, 0, 1, "O_large_lateral", 0)
        update_image(g_row, g_col, 1, 0, "O_large_lateral", 90)
        update_image(g_row, g_col, 1, 2, "O_large_lateral", 270)
        update_image(g_row, g_col, 2, 1, "O_large_lateral", 180)
    elif player == 1:
        # X
        update_image(g_row, g_col, 1, 1, "X", 0)
        update_image(g_row, g_col, 0, 0, "X_large_part", 0)
        update_image(g_row, g_col, 0, 2, "X_large_part", 270)
        update_image(g_row, g_col, 2, 0, "X_large_part", 90)
        update_image(g_row, g_col, 2, 2, "X_large_part", 180)
        update_image(g_row, g_col, 0, 1, "blank", 0)
        update_image(g_row, g_col, 1, 0, "blank", 0)
        update_image(g_row, g_col, 1, 2, "blank", 0)
        update_image(g_row, g_col, 2, 1, "blank", 0)

def button_click(g_row: int, g_col: int, row: int, col: int, event=None):
    """Executes when a button is clicked"""
    if online_mode:
        if game.player == game.turn:
            client.msg=f"{client.nickname};{g_row};{g_col};{row};{col}"
            execute_board_change(g_row, g_col, row, col)
        else:
            log.log("[INFO] Not your turn")
            infoLabel.configure(text=f"Not your turn")
    elif not online_mode:
        execute_board_change(g_row, g_col, row, col)

def execute_board_change(g_row, g_col, row, col):
    global infoLabel

    result = game.play_move(g_row, g_col, row, col)

    if result:
        if not game.g_game.active and result != "END":
            result = "ENDED"

        if result == "END":
            set_image_mini_game_ended(g_row, g_col, game.turn)
            log.log("[INFO] Game ended")
            if game.g_game.check_win()[0] and game.g_game.check_win()[1] != 0:
                infoLabel.configure(text=f"Player {player_to_sign_anti[game.turn]} won a THE game!")
            else:
                infoLabel.configure(text=f"TIE!!")
        elif result == "MINI WIN":
            set_image_mini_game_ended(g_row, g_col, game.turn)
            log.log("[INFO] s_game ended")
            if game.g_game.previous_move == None:
                infoLabel.configure(text=f"Player {player_to_sign_anti[game.turn]} won a mini game, player {player_to_sign[game.turn]}'s turn where he wants")
            else:
                infoLabel.configure(text=f"Player {player_to_sign_anti[game.turn]} won a mini game, player {player_to_sign[game.turn]}'s turn in row {game.g_game.previous_move[0]+1}, column {game.g_game.previous_move[1]+1}")
        elif result != "ENDED":
            update_image(g_row, g_col, row, col, "X" if game.turn == 1 else "O")
            if game.g_game.previous_move == None:
                infoLabel.configure(text=f"Player {player_to_sign[game.turn]}'s turn where he wants")
            else:
                infoLabel.configure(text=f"Player {player_to_sign[game.turn]}'s turn in row {game.g_game.previous_move[0]+1}, column {game.g_game.previous_move[1]+1}")
        
        if result == "ENDED":
            log.log("[INFO] Game already ended")
    else:
        infoLabel.configure(text=f"Wrong grid, you have to play in row {game.g_game.previous_move[0]+1}, column {game.g_game.previous_move[1]+1}")

def update_image(g_row: int, g_col: int, row: int, col: int, img: str, rotation = 0):
    """Updates the image at the given location to the given image

    Args:
        g_row (int): grid row
        g_col (int): grid column
        row (int): row
        col (int): column
        img (str): image name minus .png
    """
    img = ImageTk.PhotoImage(Image.open(f"{ASSETS_PATH}{img}{IMAGEFORMAT}").rotate(rotation))
    panels[g_row][g_col][row][col].configure(image=img)
    panels[g_row][g_col][row][col].image = img

def UI(get_online_mode: bool):
    global panels, infoLabel, online_mode

    online_mode = get_online_mode

    if not online_mode:
        game.player = 1
    else:
        import scripts.client.recievedPlayerNumber as recievedPlayerNumber
        game.player = recievedPlayerNumber.player
        print(game.player)
    
    app = tk.Tk()
    app.title("Tic Tac Toe")
    app.geometry("550x550")
    app.resizable(False, False)
    app.quit = exit

    log.log("[START] UI created")

    # title
    title = tk.Label(app, text="Tic Tac Toe", font=("Arial", 20))
    if online_mode: title.configure(text=f"Tic Tac Toe, you are {player_to_sign[game.player]}")
    title.grid(row=0, column=0, columnspan=11)

    infoLabel = tk.Label(app, text="Player O's turn", font=("Arial", 10))
    infoLabel.grid(row=1, column=0, columnspan=11)

    # image in grid
    img = ImageTk.PhotoImage(Image.open(f"{ASSETS_PATH}N{IMAGEFORMAT}"))

    for g_rowNum in range(len(panels)):
        for g_colNum in range(len(panels[g_rowNum])):
            for rowNum in range(len(panels)):
                for colNum in range(len(panels[rowNum])):
                    panels[g_rowNum][g_colNum][rowNum][colNum] = tk.Label(app, image=img)
                    panels[g_rowNum][g_colNum][rowNum][colNum].grid(row=2+rowNum+4*g_rowNum, column=colNum+4*g_colNum)
                    panels[g_rowNum][g_colNum][rowNum][colNum].bind("<Button-1>", partial(button_click, g_rowNum, g_colNum, rowNum, colNum))

    #create borders
    plus = ImageTk.PhotoImage(Image.open(f"{ASSETS_PATH}+.png"))
    minus = ImageTk.PhotoImage(Image.open(f"{ASSETS_PATH}-.png"))
    vertical = ImageTk.PhotoImage(Image.open(f"{ASSETS_PATH}v.png"))

    #+
    for row in range(2):
        for col in range(2):
            tk.Label(app, image=plus).grid(row=5+4*row, column=3+4*col)

    #-
    for row in range(2):
        for col in range(3):
            for s_col in range(3):
                tk.Label(app, image=minus).grid(row=5+4*row, column=4*col+s_col)
    
    #vertical
    for row in range(3):
        for col in range(2):
            for s_row in range(3):
                tk.Label(app, image=vertical).grid(row=2+4*row+s_row, column=3+4*col)



    app.mainloop()