"""Sets up the initializing strategy, and the rules and movements of a connect four game"""
from abc import (ABC, abstractmethod)


class Connect4GameStrategy(ABC):
    """Initialize the strategy abstractly so that it can be inherited"""
    def __init__(self):
        ...
    #Call the abstract method decorator to allow the method to be abstract
    @abstractmethod
    def strategy(self, game_safety_copy):
        """Strategy method that is called abstractly"""
        ...


class Connect4Game:
    """Sets up the rules and basic movements of the connect four game"""
    def __init__(self):
        #Set up the variables board, player, and winner
        self.board = [[0] * 7 for _ in range(6)]
        self.current_player = 1
        self.winner = None

    def is_valid_move(self, column):
        """Decides if the move is valid or not"""
        #If move is out of bounds, return False
        if not (0 <= column < 7):
            return False
        #If place was not yet taken, return True
        return self.board[0][column] == 0

    def make_move(self, column):
        """Sets a move if possible and declares a winner if applicable"""
        #If not a good move or there's a winner, don't continue
        if not self.is_valid_move(column) or self.winner is not None:
            return
        #Loop through the rows in the column to do the move
        for row in range(5, -1, -1):
            #The first row to be empty
            if self.board[row][column] == 0:
                #Set it to your number
                self.board[row][column] = self.current_player
                #Declare winner if he wins
                if self.check_winner(row, column):
                    self.winner = self.current_player
                #If not, switch to other player
                else:
                    self.current_player = 3 - self.current_player
                return

    def check_winner(self, row, col):
        """Checks to see whether there's a winner or not"""
        #Set up the four directional components (0,1 is left-right, 1,0 is up-down,
        #1,1 is diaganol up-right, and -1,1 is diagonal up-left)
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
        #Loop through each direction
        results = [self.check_line(row, col, dr, dc) for dr, dc in directions]
        #If any are True, there's a win
        return any(results)

    def check_line(self, row, col, dr, dc):
        """Checks lines for a win"""
        #Set up the variables, start checking 3 spaces away from the current move
        count = 0
        row = row - dr * 3
        col = col - dc * 3
        #Loop seven times to cover all spots that could be part of a win, including this new move
        for _ in range(7):
            #If the move is in bounds and it equals its number (the current player went there)
            if 0 <= row < 6 and 0 <= col < 7 and self.board[row][col] == self.current_player:
                #Increment 1
                count += 1
                #If 4 in a row, there's a win
                if count == 4:
                    return True
            #Otherwise, go back to 0
            else:
                count = 0
            #Move on to the next spot by incrementing by the directional coordinates
            row += dr
            col += dc
        #If nothing wins, return False
        return False
