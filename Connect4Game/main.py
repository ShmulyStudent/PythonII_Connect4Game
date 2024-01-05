"""Creates competitors and sets them against each other 1000 times.
Counts up all of the wins and ties and then displays the results"""
#Import the rules from the Connect4Game.py file
import Connect4Game
#Import the AI from the DanielBatyrevAI.py file
import DanielBatyrevAI as DanielAI
#Import copy
import copy
#Import func_timeout
import func_timeout

#Create a competitor list of 2 AI's
competitor_list = [DanielAI.RandomStrategy(), DanielAI.RandomStrategy("alter ego")]
#Set the max wait time to 1 second
MAX_WAIT_TIME = 1
#Create a list for the winners
winners = list()
#Create the variable for a random choice
random_choice = DanielAI.RandomStrategy()

#Loop through 1000 games
for game_nr in range(1000):
    #Print the number game
    print(game_nr + 1)
    #Start off with tie = False
    tie = False
    #Set game to the rules from Connect4Game.py
    game = Connect4Game.Connect4Game()
    #While there's no winner
    while game.winner is None:
        #Create a deep copy to make sure nothing changes the game state
        game_safety_copy = copy.deepcopy(game)
        #Try a move
        try:
            #If it takes less than 1 second, do the move
            move = func_timeout.func_timeout(
                MAX_WAIT_TIME, competitor_list[game.current_player - 1].strategy, [game_safety_copy])
        #If it takes more than 1 second
        except func_timeout.FunctionTimedOut:
            #Display that it's taking too long
            print(f'time out limit exceeded: {competitor_list[game.current_player - 1].name} performs random move')
            #Do another move
            move = random_choice.strategy(game_safety_copy)
        #Call the move
        game.make_move(move)
        #If there are no squares left and no one has won (get the sum of going through all of the valid moves)
        if 0 == sum(map(game.is_valid_move, range(7))):
            #Tie is True
            tie = True
            #Get out of the while-loop
            break
    #If there's a tie
    if tie:
        #Add it to the winners list
        winners.append("tie")
    #If not
    else:
        #Add the winner to the winners list
        winners.append(competitor_list[game.current_player - 1].name)
    #Reverse the oder of the competitors to make it fair
    competitor_list.reverse()

#Create a dictionary
dictionary = {}
#Loop through the winners list
for item in winners:
    #For each item, add 1 to the current value
    #(If the element isn't in the dictionary yet, set the value to 0)
    dictionary[item] = dictionary.get(item, 0) + 1

#Print the dictionary
print(dictionary)
