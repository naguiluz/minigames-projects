import numpy as np #used for various matrix and number functions
                   #"as" np allows us to rename an imported module

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board(): #set a function for creating the board
    board = np.zeros((6,7)) #setting board to the numpy module creating a set of zeros that is 6x7
    return board #function is to return the board we defined above

def print_board(board): #this function is specific to numpy, it flips the board on the x axis
    print(np.flip(board, 0))

def is_valid_location(board, column): #checks to make sure the top row of selected column is zero
    return board[5][column] == 0

def get_next_open_row(board, column): #for each row in the range, if the location has a zero then return(drop that piece) ??????? CHANGED R TO ROW, IF SOMETHING GOES WRONG LATER CHECK HERE TOO
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row
def drop_piece(board, row, column, piece): #function that sets game piece to rowXcolumn location
    board[row][column] = piece



board = create_board() #keeping names simple by creating a variable
print_board(board) #outputting board


board = create_board() #setting this up again initializes the board at the start of the game

game_over = False #setting game over to false at the start of the game
turn = 0 #set up turn order

while not game_over: #creating the loop for our game to run as long as someone hasn't won
    # ask for player 1 input
    if turn == 0:
        column = int(input("Player 1 Make your selection (0-6):")) #this string is returned and player 1 input is accepted, however we want the input to be returned as an integer
                                                                      # (0-6) represents the column they are selecting
        if is_valid_location(board, column): #if the column selection is checked and a zero is found
            row = get_next_open_row(board, column) #then the row is selected by checking each row and finding the next with a zero
            drop_piece(board, row, column, 1) #then a piece is dropped on the board in that row and column
        print(column) #their number is printed
        #print(type(selection)) this would allow us to see the class(string/num/etc) of what is being printed


    # ask for player 2 input

    else:
        column = int(input("Player 2 Make your selection (0-6):"))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)
        print(column)


    print_board(board) #this now prints our board using the new flip funtion

    turn += 1
    turn = turn % 2 #this "mod division" takes the remainder after dividing by two, effectively going back to 0 and 1 (odd and even)
