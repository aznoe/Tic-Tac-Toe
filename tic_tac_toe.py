import os
    
class Board:
    def __init__(self):
        self.board = [" ", " ", " " , " " , " " , " " , " " , " " ," ", " "]
        
    
    def display(self):
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]}")    
        print("-----------")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]}" )    
        print("-----------")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]}" )    
    
    def update_cell(self, cell_nr, player):
        if self.board[cell_nr] is " ":
            self.board[cell_nr]  = player
        
    def is_winner(self, player):

        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]:
            result = True
            for cell_no in combo:
                if self.board[cell_no] is not player:
                    result = False
            if result == True:
                return True
        return False
        

    def is_tie(self):
        used_cells = 0
        for cell in self.board:
            if cell is not " ":
                used_cells+=1
        if used_cells == 9:
            return True
        else:
            return False



    def reset(self):
        self.board = [" "," ", " ", " " , " " , " " , " " , " " , " " ," "]


"""
    def ai_move(self, player):
        #if center is open, choose that
        if self.board[5] is " ":
            self.update_cell(5, player)

        #AI can win
        
        for i in range(3):
            if self.board[i] == " ":
                if self.board[i] == " " and self.board[i+1] == player and self.board[i-1] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i+1] == player and self.board[i+2] == player:
                    self.update_cell(i,player) 
                if self.board[i] == " " and self.board[i-1] == player and self.board[i-2] == player:
                    self.update_cell(i,player)

                if self.board[i] == " " and self.board[i+3] == player and self.board[i+6] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i-3] == player and self.board[i+3] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i-6] == player and self.board[i-3] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i+4] == player and self.board[i+8] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i-4] == player and self.board[i+4] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i-4] == player and self.board[i-8] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i+2] == player and self.board[i+4] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i-2] == player and self.board[i+2] == player:
                    self.update_cell(i,player)
                if self.board[i] == " " and self.board[i-2] == player and self.board[i-4] == player:
                    self.update_cell(i,player)



        #AI Blocks

        ##choose random
        
        for i in range(1,10):
            if self.board[i] == " ":
                self.update_cell(i, player)
                break
        """

        
board = Board()

def print_header():
    print("Welcome to tic-tac-toe\n")
    print("these are the numbers of the board!")
    print(" 1 | 2 | 3")    
    print("-----------")
    print(" 4 | 5 | 6" )    
    print("-----------")
    print(" 7 | 8 | 9\n\n" )
  

def refresh_screen():
        #clear screen
        os.system("clear")

        #print the header
        print_header()

        #show board
        board.display()
while True:
    refresh_screen()

    #get x input
    x_choice = int(input("\nx) Please choose 1 - 9. > "))

    #update board
    board.update_cell(x_choice, "X")

    #refresh screen
    refresh_screen()

    # check for x win
    if board.is_winner("X"):
        print("\nX wins!\n")
        play_again = input("Would you like to play again?(Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

     

    # check for tie
    if board.is_tie():
        print("\nTie!\n")
        play_again = input("Would you like to play again?(Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    #get o input
    o_choice = int(input("\no) Please choose 1 - 9. > "))

    #board.ai_move("O")

    #refresh screen
    refresh_screen()

    #update board
    board.update_cell(o_choice, "O")
    
    
    # check for O win
    if board.is_winner("O"):
        print("\nO wins!\n")
        play_again = input("Would you like to play again?(Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break


