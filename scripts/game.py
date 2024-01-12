import scripts.TicTacToeNxN as ttt
import scripts.log as log

games = [[ttt.TicTacToeNxN(3) for col in range(3)] for row in range(3)]
g_game = ttt.TicTacToeNxN(3)
turn = 1
player = None
online_mode = True

log.log("[START] Game created")

def update_prev_mov(row, col):
    if games[row][col].active:
            g_game.previous_move = (row, col)
    else:
        g_game.previous_move = None

def play_move(g_row, g_col, row, col) -> bool:
    global turn, games, g_game

    if (not g_game.previous_move or g_game.previous_move == (g_row, g_col)) and g_game.active:
        update_prev_mov(row, col)
        
        if games[g_row][g_col].move(turn, row, col) and games[g_row][g_col].active:
            # available move
            log.log(f"[INFO] s_game move at {row}, {col} from player {turn}")
            games[g_row][g_col].print_board()

            if games[g_row][g_col].check_win()[0] and games[g_row][g_col].check_win()[1] != 0:
                # someone wins small game
                log.log(f"[INFO] s_game {g_row}, {g_col} won by {turn} due to {games[g_row][g_col].check_win()[3]} {games[g_row][g_col].check_win()[2]}")
                update_prev_mov(row, col)
                turn = 1 if turn == 2 else 2
                
                if g_game_move(g_row, g_col, games[g_row][g_col].check_win()[1]):
                    return "END"
                else:
                    return "MINI WIN"

            elif games[g_row][g_col].check_tie()[0]:
                # tie
                small_game_tie(g_row, g_col)

            turn = 1 if turn == 2 else 2
            return True
        else:
            # wrong grid
            log.log(f"[INFO] wrong grid at {row}, {col} from player {turn}")
            return False

        
    elif not games[g_row][g_col].active:
        # game ended
        log.log(f"[GOOD ERROR] s_game {g_row}, {g_col} ended already")
        return False
    else:
        # wrong move
        log.log(f"[GOOD ERROR] Wrong move at {row}, {col} from player {turn}")
        return False

def g_game_move(g_row, g_col, player):
    global games, g_game, turn

    if g_game.move(player, g_row, g_col):
        # available move
        if g_game.check_win()[0] and g_game.check_win()[1] != 0:
            # someone wins
            log.log(f"[INFO] g_game won by {player} due to {g_game.check_win()[3]} {g_game.check_win()[2]}")
            return True
        elif g_game.check_tie()[0]:
            # tie
            g_game_tie()
            log.log("[INFO] g_game ended in a tie")
            return True
        return False
    else:
        # error msg
        log.log(f"[ERROR] [HIGH] !!!!!!!! Wrong move at {g_row}, {g_col} from player {player} on big game?!?!")

def small_game_tie(g_row, g_col):
    log.log(f"[INFO] Game {g_row}, {g_col} ended in a tie wtf to I do now?")

def g_game_tie():
    log.log("[INFO] Final game ended in a tie")