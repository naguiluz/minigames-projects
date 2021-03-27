import numpy as np
import pygame
import sys
import math


ROW_COUNT = 6
COLUMN_COUNT = 7
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
#FUNCTIONS

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def print_board(board):
    print(np.flip(board, 0))

def is_valid_location(board, column):
    return board[ROW_COUNT-1][column] == 0

def get_next_open_row(board, column):
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
    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (column*SQUARESIZE, row*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            #if board[row][column] == 0: #this is stating that if there is no piece the cirle is black (removed because black circle is the new default)
            pygame.draw.circle(screen, BLACK, (int(column*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)

    for column in range(COLUMN_COUNT): #set up new loop so we could build the background separately then apply our new math as pieces are added
        for row in range(ROW_COUNT):
            if board[row][column] == 1:
                pygame.draw.circle(screen, RED, (int(column * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), radius) #removed extra square size addition and added height subtraction because we no longer need to correct for black space at top
            elif board[row][column] == 2:
                pygame.draw.circle(screen, YELLOW, (int(column * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), radius)
    pygame.display.update() #this is so the game will render changes


#MAIN LOOP

board = create_board()
#print_board(board) unnecesary bc final game shown in the screen
game_over = False
turn = 0

#PYGAME
pygame.init()
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)
radius = int(SQUARESIZE/2 - 5)

#DISPLAY
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 75) #calls font and size can also do bold and italic (x, x, x, x)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION: #this function creates the circle that follows the mouse
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE)) #this creates a black rectangle to stop the circles from taking up the whole space with each new loop
            posx = event.pos[0] #setting the x position

            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), radius) #this draws the circle at the top of the screen
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), radius)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(event.pos) this was used to first determine the average location of our clicks
            # Player 1 input moved into the event of clicking the mouse
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE)) #this places a black box each mouse click so that at the end the message is not obscured by the colored circle
            if turn == 0:
                posx = event.pos[0] #the x position is the first or "zero" element(value) in that event
                column = int(math.floor(posx/SQUARESIZE)) #the column is equal too the      intiger(of the rounded down(x position divided by the square size))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, WHITE) # creating a label to appear(self, text, antialias, background)
                        screen.blit(label, (40,10)) #this sets the location (self, source, destination, area, flags)
                        game_over = True



            # Player 2 input moved into the event of clicking the mouse
            else:
                posx = event.pos[0]
                column = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, WHITE)
                        screen.blit(label, (40, 10))
                        game_over = True



            draw_board(board)  # replace print with draw because the board doesnt need to be printed in console

            turn += 1
            turn = turn % 2

            if game_over: #this causes the game to wait 3 seconds befoore closing the window
                pygame.time.wait(3000)