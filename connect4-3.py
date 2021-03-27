import numpy as np
import pygame #provides objects and functions for creating visuals and inputs
import sys #general system functions

ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255) #setting an RGB value for a bright blue
BLACK = (0, 0, 0)

#FUNCTIONS

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def print_board(board):
    print(np.flip(board, 0))

def is_valid_location(board, column):
    return board[ROW_COUNT-1][column] == 0

def get_next_open_row(board, column):  #??????? CHANGED R TO ROW, IF SOMETHING GOES WRONG LATER CHECK HERE TOO
    for row in range(ROW_COUNT):
        if board[row][column] == 0:
            return row
def drop_piece(board, row, column, piece):
    board[row][column] = piece

def winning_move(board, piece):
    # check horizontal locations
    for column in range(COLUMN_COUNT-(COLUMN_COUNT-3)):
        for row in range(ROW_COUNT):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True
    # check vertical locations
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT-(ROW_COUNT-3)):
            if board[row][column] == piece and board[row+1][column] == piece and board[row+2][column] == piece and board[row+3][column] == piece:
                return True
    # check for positive slope diagonals
    for column in range(COLUMN_COUNT-3):
        for row in range(ROW_COUNT-3):
            if board[row][column] == piece and board[row+1][column+1] == piece and board[row+2][column+2] == piece and board[row+3][column+3] == piece:
                return True
    # check for negative slope diagonals
    for column in range(COLUMN_COUNT-3):
        for row in range(3, ROW_COUNT):
            if board[row][column] == piece and board[row-1][column+1] == piece and board[row-2][column+2] == piece and board[row-3][column+3] == piece:
                return True
def draw_board(board):
    for column in range(COLUMN_COUNT): #all squares and circles are drawn for EACH column and row (for each row/column the default value is 0) so 0,0+SS gives top left corner, the lengthxwidth both SS
        for row in range(ROW_COUNT): #extra square size accounts for the black bar at the top
            pygame.draw.rect(screen, BLUE, (column*SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE)) #pygame.draw.rect()-draws a rectangle-rect(surface, color, rect dimensions (first two set up x/y of the corner and the other two define length and width)
            pygame.draw.circle(screen, BLACK, (int(column*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius) #circle(surface, color, center, radius) c*SS sets the postion + SS to set the other side /2 to get to the center of the square


#MAIN LOOP

board = create_board()
print_board(board)

game_over = False
turn = 0

#PYGAME
pygame.init()  #initiate pygame before we run the program
SQUARESIZE = 100 #sets the size of each block
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height) #sets the size of the board
radius = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size) #configures a display surface to the predetermined (size)
draw_board(board)
pygame.display.update()
while not game_over:
    for event in pygame.event.get(): #pygame continually loops "events"
        if event.type == pygame.QUIT: #if the event is exitying the game then the exit will happen
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            continue

            # Player 1 input moved into the event of clicking the mouse
            #if turn == 0:
            #    column = int(input("Player 1 Make your selection (0-6):"))
             #   if is_valid_location(board, column):
              #      row = get_next_open_row(board, column)
               #     drop_piece(board, row, column, 1)

                #    if winning_move(board, 1):
                 #       print("PLAYER 1 WINS!")
                  #      game_over == True
                   #     print_board(board)
                    #    break

            # Player 2 input moved into the event of clicking the mouse
            #else:
             #   column = int(input("Player 2 Make your selection (0-6):"))
              #  if is_valid_location(board, column):
               #     row = get_next_open_row(board, column)
                #    drop_piece(board, row, column, 2)

                 #   if winning_move(board, 2):
                  #      print("PLAYER 2 WINS!")
                   #     game_over == True
                    #    print_board(board)
                     #   break


            #print_board(board)

            #turn += 1
            #turn = turn % 2
