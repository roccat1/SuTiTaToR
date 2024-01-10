import scripts.log as log

log.log("[START] TicTacToeNxN.py")

class TicTacToeNxN:
    def __init__(self, DIM):
        self.DIM = DIM

        self.board = [[0 for column in range(self.DIM)] for row in range(self.DIM)]
        self.turn = 1
        self.active = True

        log.log(f"[START] Game created with dimension {self.DIM}")

    def set_turn(self, player: int) -> None:
        """Sets the turn of the game

        Args:
            player (int): Player number
        """
        self.turn = player
        log.log(f"[INFO] Turn set to {self.turn}")

    def switch_turn(self) -> None:
        """Switches the turn of the game"""
        self.turn = 1 if self.turn == 2 else 2    
        log.log(f"[INFO] Turn switched to {self.turn}")
    
    def print_board(self) -> None:
        """Prints the board to the console"""
        log.log("[INFO] Board:")
        for row in self.board:
            log.log("[INFO] " + str(row))

    def check_win(self) -> tuple:
        """Checks if the game has been won by a player

        Returns:
            tuple: (bool, int, int, str) - (True if game has been won, player who won, row/column/diagonal number, row/column/diagonal)
        """
        self.active=False
        if self.check_rows()[0]:
            return self.check_rows()+("row",)
        elif self.check_columns()[0]:
            return self.check_columns()+("column",)
        elif self.check_diagonals()[0]:
            return self.check_diagonals()+("diagonal",)
        elif self.check_tie()[0]:
            return self.check_tie()+("tie",)
        else:
            self.active=True
            return (False, 0, 0)

    def check_rows(self) -> tuple:
        """Checks if any row has been won by a player

        Returns:
            tuple: (bool, int, int) - (True if row has been won, player who won, row number)
        """
        for row in self.board:
            player = row[0]
            if all([cell == player for cell in row]) and player != 0:
                return (True, player, self.board.index(row))
        
        return (False, 0, 0)

    def check_columns(self) -> tuple:
        """Checks if any column has been won by a player

        Returns:
            tuple: (bool, int, int) - (True if column has been won, player who won, column number)
        """
        for column in range(self.DIM):
            player = self.board[0][column]
            if all([self.board[row][column] == player for row in range(self.DIM)]) and player != 0:
                return (True, player, column)
        
        return (False, 0, 0)

    def check_diagonals(self) -> tuple:
        """Checks if any diagonal has been won by a player

        Returns:
            tuple: (bool, int, int) - (True if diagonal has been won, player who won, diagonal number)
        """
        player = self.board[0][0]
        if all([self.board[i][i] == player for i in range(self.DIM)]) and player != 0:
            return (True, player, 0)
        
        player = self.board[0][self.DIM-1]
        if all([self.board[i][self.DIM-1-i] == player for i in range(self.DIM)]) and player != 0:
            return (True, player, 1)
        
        return (False, 0, 0)

    def check_tie(self) -> tuple:
        """Checks if the game has ended in a tie

        Returns:
            tuple: (bool, int, int) - (True if game has ended in a tie, 0, 0)
        """
        if all([cell != 0 for row in self.board for cell in row]) and self.board[0][0] != 0:
            return (True, 0, 0)
        
        return (False, 0, 0)

    def move(self, player: int, row: int, column: int) -> bool:
        """Makes a move on the board

        Args:
            player (int): Player number
            row (int): Row number
            column (int): Column number

        Returns:
            bool: True if move was successful, False if move was invalid
        """
        if self.board[row][column] == 0:
            self.board[row][column] = player
            return True
        else:
            log.log("[INFO] Move failed")
            return False
        
    def playConsole(self):
        """Plays the game in the console"""
        player = 1
        while True:
            self.print_board(self.board)
            try:
                row = int(input(f"Player {player} choose row: "))
                column = int(input(f"Player {player} choose column: "))
            except: 
                print("Invalid input")
                continue
            if self.move(self.board, player, row, column):
                result = self.check_win(self.board)
                if self.result[0]:
                    print(f"Player {self.result[1]} wins due to {self.result[3]} {self.result[2]}")
                    self.print_board(self.board)
                    break
                else:
                    player = 1 if player == 2 else 2