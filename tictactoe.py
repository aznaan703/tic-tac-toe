import pygame
import sys
import numpy as np

pygame.init( )

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COL = 3

BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)

screen=pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

board = np.zeros( (BOARD_ROWS, BOARD_COL) )

def create_lines():

    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600), LINE_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False
    
def is_board_full():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COL):
            if board[row][col]==0:
                return False
    return True

create_lines()

player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    player = 2

                elif player == 2:
                    mark_square(clicked_row,clicked_col,2)
                    player = 1

                print(board)

    pygame.display.update()
