"""Creates an AI that uses a random strategy"""
#Imports the rules
import Connect4Game as Game
#Imports random
import random

#Use inheritance to inherit the functions from Connect4GameStrategy
class RandomStrategy(Game.Connect4GameStrategy):
    """Creates an AI that uses a random strategy"""
    #Default the name to Daniel Batyrev
    def __init__(self, name="Daniel Batyrev"):
        #Set the name
        self.name = name
    #Use classmethod to create an instance of the class
    @classmethod
    def strategy(cls, game_safety_copy):
        #Create a list
        valid_moves = list()
        #Loop 7 times
        for col in range(7):
            #If the move is valid
            if game_safety_copy.is_valid_move(col):
                #Append the move
                valid_moves.append(col)
        #Return a random choice out of the valid moves
        return random.choice(valid_moves)
