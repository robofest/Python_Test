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
       [0, 1, 2],
       [3, 4, 5],
       [6, 7, 8],
       [7, 8, 9],
       [0, 3, 6],
       [1, 4, 7],
       [2, 5, 8],
       [0, 4, 8],
       [2, 4, 6],
       [1, 5, 9]
    ]

    def draw_board():
        for i in range(8, 0, -3):
            if i == 8:
                print(board[i - 2], board[i - 1], board[i], board[i + 1])
            else:
                print(board[i - 2], board[i - 1], board[i])
            
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
        isFinished = True
        for i in board:
            if i != 'X' and i != 'O':
                isFinished = False
                break
        if isFinished:
            print("It's a tie!")
            print("No one wins.")
            return True        
        
        
        
        
        
        
        

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