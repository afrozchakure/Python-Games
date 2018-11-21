import numpy as np  #Helps in using methods for making and adding functionality to a matrix
import pygame
import sys
import math

ROW_COUNT=6 #Global Static Variable
COLUMN_COUNT=7  #These are the rows and colums specified before the program begins

BLUE=(0,0,255)  #Its an RGB value (here only blue has some value)
BLACK=(0,0,0)   #Black value in RGB is (0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0) #YELLOW is a combination of both red and green


def create_board():
	board=np.zeros((ROW_COUNT,COLUMN_COUNT))  #Makes a matrix of 6 x 7 of all zeros (np.zeros(x,y) produces a matrix)
	return board

def drop_piece(board,row,col,piece):
    board[row][col]=piece  #fills the slot with the piece


def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0 #Checking to make sure that the column has not been filled fully, it checks the last row only (it returns a boolean value)

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0: #returns the slot which empty ,1st case which is empty
            return r

def print_board(board):#To make the board build from the bottom up
    print(np.flip(board,0))  #0 is the axis i.e. flip the board over x axis, right side up (np.flip() is a command in numpy)

def winning_move(board,piece): #The game lets you know that 4 dots are in line(either horizontally,vertically and diagonally)
    #Check horizontal locations for win

    for c in range(COLUMN_COUNT-3):  #we're subtracting 3 since the logic is applicable for 4 columns only
        for r in range(ROW_COUNT):
            if(board[r][c]== piece and board[r][c+1]==piece and board[r][c+2]==piece and board[r][c+3]==piece):
                return True

    #Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3): #we're subtracting 3 since the logic is applicable for 4 columns only3
            if(board[r][c]== piece and board[r+1][c]==piece and board[r+2][c]==piece and board[r+3][c]==piece):
                return True

    #Check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):  #we're subtracting 3 so that the logic works for 4 columns
        for r in range(ROW_COUNT-3): #we're subtracting 3 since the logic is applicable for 4 columns only
            if(board[r][c]== piece and board[r+1][c+1]==piece and board[r+2][c+2]==piece and board[r+3][c+3]==piece):
                return True

    #Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):  #Remember the the index of the matrix starts from the lower side since we have flipped the matrix
        for r in range(3,ROW_COUNT): #Here the negatively sloped diagonal cannot start any lower than the 3 index(i.e. 0,1,2 indices)
            if(board[r][c]== piece and board[r-1][c+1]==piece and board[r-2][c+2]==piece and board[r-3][c+3]==piece):
                return True


def draw_board(board):  #just like print_board but it draws in pygame
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))  #These are the (screen size,positon on y-axis,width,height)
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS) #pygame accepts only integers (refer pygame documentation)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c]==2:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    pygame.display.update() #so that the screen is updated after each click


board=create_board()
print_board(board)
game_over=False
turn=0

pygame.init() #Done in every pygame project i.e. it initializes the pygame module

SQUARESIZE=100 #The value of each square is in pixels

#Defining the screen size
width=COLUMN_COUNT * SQUARESIZE   # Its the number of columns times the squaresize
height= (ROW_COUNT+1) * SQUARESIZE  #One additional row for displaying the spot where we are dropping the circle

size=(width,height)  #size is a tuple of width and height

RADIUS=int(SQUARESIZE/2 -5) #radius has to be a little smaller than the squaresize

screen = pygame.display.set_mode(size)  #for pygame to read size  (from documentation)
draw_board(board)
pygame.display.update()  #Whenever we want to update our display

myfont=pygame.font.SysFont("monospace",75)  #Refer the documentation ()

while not game_over:
    for event in pygame.event.get():  #pygame is an event based library it reads every key or mouse-click pressed as an event

        pygame.display.update()
        if event.type==pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            posx=event.pos[0]  #This provides the position of the cursor
            if turn==0:
                pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)),RADIUS)
            else:
                pygame.draw.circle(screen,YELLOW,(posx,int(SQUARESIZE/2)),RADIUS)

        if event.type==pygame.QUIT:  #Done in every game, it allows us to properly exit out of any game
            sys.exit()   #system exit (when we click on exit sign it should close)

        if event.type==pygame.MOUSEBUTTONDOWN: # Where we click it drops down the piece in that place
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            #print(event.pos)


            # Ask for Player 1 Input
            if (turn == 0):
                posx=event.pos[0] #the initial position
                col=int(math.floor(posx/SQUARESIZE))  # The player enters the column no. here
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label=myfont.render("Player 1 wins!!!",1,RED)  #The font will be printed in "red"
                        screen.blit(label,(40,10)) #It updates text to the specific part(position) of the screen
                        game_over = True  # It ends the game


            # Ask for Player 2 Input
            else:
                posx = event.pos[0]  # the initial position
                col = int(math.floor(posx / SQUARESIZE))  # The player enters the column no. here

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        label=myfont.render("Player 2 wins!!",1,YELLOW)
                        screen.blit(label,(40,10))
                        game_over = True  # It ends the game
            print_board(board)
            draw_board(board)  #we need to draw_board after every turn

            turn += 1  # increase each term  by one
            turn = turn % 2  # It alternates between player 1 and player 2

        if game_over:
            pygame.time.wait(3000) #The wait value is in millisecond hence here the wait is 3 seconds



