# LTU CS Chung S2022
# First, complete this program for standard tic tac toe game. 
# then modify it to solve the following extended tic tac toe board
# 
#    6 7 8 9
#    3 4 5
#    0 1 2
#
# Requried to test the following cases
# (1) X wins, (2) O wins, (3) Tie

def tic_tac_toe(): 

    board = list(range(0, 10)) # why starts from 0? due to index of the list.
    # print(board)

    WIN_CASES = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [1, 4, 7],
       [2, 5, 8],
       [3, 6, 9],
       [1, 5, 9],
       [3, 5, 7],
    ]

    def draw_board():
        print(board[7], board[8], board[9])
        print(board[4], board[5], board[6])
        print(board[1], board[2], board[3])
        print()

    def choose_number():
        while True:
            try:
                n = int(input())
                if n in board:
                    return n
                else:
                    print("\nInvalid move. Try again")
            except ValueError:
               print("\nThat's not a number. Try again")

    
    def is_game_over(): # return True if game is over
        # check if a player wins
        for a, b, c in WIN_CASES:
            if board[a] == board[b] == board[c]:
                draw_board() # when game is over
                print("Player {0} wins!\n".format(board[a]))
                print("Congratulations!\n")
                return True   
        # check if the game is tie. If tie, return True too.
        
        
        
        
        
        
        
        
        

    player = 'X'   # set first player as X
    while is_game_over() != True: # there is no do-while in Python
        draw_board()
        print("Player {0}: pick your move".format(player))
        board[choose_number()] = player # update the board
        player = 'O' if player == 'X' else 'X' # decide next player
        print()
#------------------ end of tic_tac_toe() ----------------------

while True:
    tic_tac_toe()
    if input("Play again (y/n)\n").lower() != "y":
        break
    print("----- A New Game -----")

print("Bye! End of game")   