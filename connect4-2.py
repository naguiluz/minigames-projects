import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

#FUNCTIONS

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT)) #"magic numbers" switched out for row/column count to allow for easier changes
    return board

def print_board(board):
    print(np.flip(board, 0))

def is_valid_location(board, column):
    return board[ROW_COUNT-1][column] == 0 #magic number 5 switched for rowcount-1 to allow for easier changes

def get_next_open_row(board, column):  #??????? CHANGED R TO ROW, IF SOMETHING GOES WRONG LATER CHECK HERE TOO
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row
def drop_piece(board, row, column, piece):
    board[row][column] = piece

def winning_move(board, piece):
    # check horizontal locations
    for column in range(COLUMN_COUNT-(COLUMN_COUNT-3)): #loop through each column except for the final 3 because a 4 in a row is not possible from those locations
        for row in range(ROW_COUNT): #loop through each row
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece: #this checks the last dropped piece and the 3 columns next to it in the same row
                return True
    # check vertical locations
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-(ROW_COUNT-3)):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece: #this checks last piece and 3 rows above it in same column
                return True
    # check for positive slope diagonals
    for column in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece: #checks for the slope of the pieces
                return True
    # check for negative slope diagonals
    for column in range(COLUMN_COUNT-3):
        for row in range(3, ROW_COUNT): #sets the first possible row that this victory could happen 
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True

#MAIN LOOP

board = create_board()
print_board(board)

game_over = False
turn = 0

while not game_over:
    if turn == 0:
        column = int(input("Player 1 Make your selection (0-6):"))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

            if winning_move(board, 1): #if our winning move function is met by player 1 print message and end game
                print("PLAYER 1 WINS!")
                game_over == True
                print_board(board)
                break





    else:
        column = int(input("Player 2 Make your selection (0-6):"))
        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

            if winning_move(board, 2): #if our winning move function is met by player 2 print message and end game
                print("PLAYER 2 WINS!")
                game_over == True
                print_board(board)
                break


    print_board(board)

    turn += 1
    turn = turn % 2
