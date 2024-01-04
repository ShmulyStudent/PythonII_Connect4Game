"""Creates a GUI for connect four and fills in the board, disables buttons, and displays a winner"""
#Import tkinter to make the GUI
import tkinter as tk
#Import messagebox to display messages
from tkinter import messagebox
#Import the rules from the Connect4Game.py file
import Connect4Game as game

class Connect4GUI:
    """Sets up the connect four GUI"""
    def __init__(self, master):
        #Initialize
        self.master = master
        #Name the title
        self.master.title("Connect 4")
        #Set the game
        self.game = game.Connect4Game()
        #Create a list
        self.buttons = []
        #Loop through 7 columns
        for col in range(7):
            #Set up the buttons with the text being the column + 1
            #and using lambda to call the make.move function
            button = tk.Button(master, text=str(col + 1), command=lambda c=col: self.make_move(c))
            #Set up the spacing on the grid
            button.grid(row=0, column=col)
            #Append to the list
            self.buttons.append(button)
        #Create the canvas
        self.canvas = tk.Canvas(master, width=7 * 60, height=6 * 60)
        #Set it up on the grid
        self.canvas.grid(row=1, column=0, columnspan=7)
        #Call the function draw_board
        self.draw_board()

    def make_move(self, column):
        """Gets called when a button is pressed, and it accesses the rules, draws and fills in the 
        board, and determines and displays if there is a winner. Then it destroys the GUI window"""
        #Calls the make_move for the Connect4Game rules and movement abilities
        self.game.make_move(column)
        #Redraw the canvas and fill it in properly
        self.draw_board()
        #If there's a winner
        if self.game.winner is not None:
            #Set the winner text
            winner_text = f"Player {self.game.winner} wins!"
            #Display game over plus the winner text
            messagebox.showinfo("Game Over", winner_text)
            #Call the destroy functionto end the GUI window
            self.master.destroy()

    def draw_board(self):
        """Deletes the board and redraws it, then fills in the
        proper circles and determines the state of the buttons"""
        #First, delete the canvas
        self.canvas.delete("all")
        #Redraw the new canvas as a 6 x 7
        for row in range(6):
            for col in range(7):
                #Set up proper coordinates to make the squares, and place them touching each other
                x0, y0 = col * 60, row * 60
                x1, y1 = x0 + 60, y0 + 60
                #Create the canvas
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")
                #If the box is Player 1, fill it with a red circle
                if self.game.board[row][col] == 1:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="red", outline="red")
                #If the box is Player 2, fill it with a yellow circle
                elif self.game.board[row][col] == 2:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="yellow", outline="yellow")
        #Loop through the 7 buttons
        for col in range(7):
            #If the top square isn't filled, the button is normal
            if self.game.board[0][col] == 0:
                self.buttons[col]["state"] = tk.NORMAL
            #If the top square is filled, the button is disabled
            else:
                self.buttons[col]["state"] = tk.DISABLED

#If run directly
if __name__ == "__main__":
    #Creates an instance of Tk with the alias of tk
    root = tk.Tk()
    #Creates an instance of Connect4GUI and passes in root
    app = Connect4GUI(root)
    #Starts the main event loop
    root.mainloop()
