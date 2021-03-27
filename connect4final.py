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
            pygame.draw.circle(screen, BLACK, (int(column*SQUARESIZE+SQUARESIZE/2), int(row*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)

    for column in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][column] == 1:
                pygame.draw.circle(screen, RED, (int(column * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), radius)
            elif board[row][column] == 2:
                pygame.draw.circle(screen, YELLOW, (int(column * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)), radius)
    pygame.display.update()


#MAIN LOOP

board = create_board()
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
myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]

            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), radius)

            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), radius)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:

            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            if turn == 0:
                posx = event.pos[0]
                column = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, WHITE)
                        screen.blit(label, (40,10))
                        game_over = True


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



            draw_board(board) 
            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)