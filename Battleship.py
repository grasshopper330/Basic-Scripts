#import the ability to use random integers
from random import randint
#here we declare the existence of a board
board = []
#here we declare that the board is 5x5
for x in range(5):
    board.append(["O"] * 5)
#now we can show the board all put together
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)
#creating the placement of the battleship
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
#a for loop so that the player gets 3 turns
for turn in range(4):
    #allow the user to guess the row and column
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    #if the user guesses currectly...
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        #mark the spot that they guessed
        board[guess_row][guess_col] = "!"
        print ""
        print "Game Over"
        print ""
        #show them the board
        print_board(board)
        #get out of the for loop
        break
    #if the user guesses incorrectly...
    else:
        #if the guess a number that isn't on the board...
        if (guess_row < 0 or guess_row > 4) or \
        (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        #if they guess a number they already guessed...
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            #replace O with X for the incorrect guess
            board[guess_row][guess_col] = "X"
        #let the user know how many guesses they've made
        print "Turn: ", turn + 1
    if turn == 3:
        print ""
        print "Game Over"
        print ""
        print_board(board)
