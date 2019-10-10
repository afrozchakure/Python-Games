# Referred video https://www.youtube.com/watch?v=-8n91btt5d8

import pygame
import sys
import random  # Pythons random library

pygame.init()  # To initialize pygame

# Defining the width and height of the screen
WIDTH = 800  # Global variables
HEIGHT = 600

# Defining the color for player and enemy
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)  # Setting the background color

# Defining player position and player block size
PLAYER_SIZE = 50  # Its the size of the block
PLAYER_POS = [WIDTH/2, (HEIGHT-(2*PLAYER_SIZE))]  # Its the x and y-axis position

# Defining an enemy
ENEMY_SIZE = 50
X_POS = random.randint(0, WIDTH - ENEMY_SIZE)  # Its the starting position of the enemy block
ENEMY_POS = [X_POS, 0]  # Setting the enemy position
ENEMY_LIST = [ENEMY_POS]  # Defining an enemy list to contain multiple enemies

SPEED = 10  # Defining the speed at which the block falls

# Creating a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # We have a screen of WIDTH 800 and HEIGHT 600

game_over = False

score = 0  # Initializing the score

clock = pygame.time.Clock()  # It defines a clock

myFont = pygame.font.SysFont("monospace", 35)  # Defining the font in pygame (Monospace is font and 35 is in pixels)
endFont = pygame.font.SysFont("comicsansms", 40, True, False)

def set_level(score, SPEED):
    if score < 20:
        SPEED = 10
    elif score < 40:
        SPEED = 12
    elif score < 60:
        SPEED = 15
    else:
        SPEED = 20

    return SPEED

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        # Drawing the enemy rectangle
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], ENEMY_SIZE, ENEMY_SIZE))

def drop_enemies(ENEMY_LIST):
    delay = random.random()  # It generates a random value betwee 0 and 1
    if len(ENEMY_LIST) < 10 and delay < 0.1:  # When the no. of elements inside the list is less than 10
        x_pos = random.randint(0, WIDTH-ENEMY_SIZE)  # Assigning the x-coordinate to the new enemy randomly.
        y_pos = 0
        ENEMY_LIST.append([x_pos, y_pos])  # It appends new enemy coordinates to the enemy list

def update_enemy_positions(ENEMY_LIST, score):
    for idx, ENEMY_POS in enumerate(ENEMY_LIST):  # Using the enumerate function

        # Updating the position of enemy and making the enemy block fall
        if ENEMY_POS[1] in range(0, HEIGHT):  # It allows the enemy block to move down, Checks if the enemy is onscreen
            ENEMY_POS[1] += SPEED  # It increments the value of height

        else:
            ENEMY_LIST.pop(idx)  # It pops out the enemy from the enemy_list
            score +=1  # Incrementing the score each time we pass it

    return score  # It returns the score

def collision_check(enemy_list, player_pos):   # Causes the game to end if it returns True
    for enemy_pos in enemy_list:  # It iterates through each enemy_pos inside enemy_list
        if detect_collision(player_pos, enemy_pos):  # returns True if collision is detected for any enemy_pos
            return True
    return False


def detect_collision(PLAYER_POS, ENEMY_POS):
        p_x = PLAYER_POS[0]
        p_y = PLAYER_POS[1]

        e_x = ENEMY_POS[0]
        e_y = ENEMY_POS[1]

        if (e_x >= p_x and e_x < (p_x + PLAYER_SIZE)) or (p_x >= e_x and p_x < (e_x + ENEMY_SIZE)):  # Checks to see the x-overlap
            if (e_y >= p_y and e_y < (p_y + PLAYER_SIZE)) or (p_y >= e_y and p_y < (e_y + ENEMY_SIZE)):  # Checks to see the y-overlap
                return True
        return False  # False is returned only when the above if statements do not get run.

def limit(PLAYER_POS):  # Function to restrict the movement of the player
    p_x = PLAYER_POS[0]
    p_y = PLAYER_POS[1]

    if p_x <=0 and p_y <=0:
        p_x = 0
        p_y = 0

    elif p_x >=750 and p_y <=0:
        p_x = 750
        p_y = 0

    elif p_x >=750 and p_y >= 550:
        p_x = 750
        p_y = 550

    elif p_x <= 0 and p_y >= 550:
        p_x = 0
        p_y = 550

    elif p_x >= 750  :
        p_x = 750

    elif p_x <= 0 :
        p_x = 0

    elif p_y >=550:
        p_y = 550

    elif p_y <= 0:
        p_y = 0

    # elif p_x >= 100:
    #     p_x = 100
    #
    # elif p_y >= 50:
    #     p_y = 50

    PLAYER_POS = [p_x, p_y]

    return PLAYER_POS

while not game_over :  # It keeps running until we hit the game_over condition

    for event in pygame.event.get():  # For loop to get an event
        # print(event)  # It prints the event each time

        if event.type == pygame.QUIT:  # When we click on the close button it exits the program
            sys.exit()

        if event.type == pygame.KEYDOWN:  # (press Ctrl + /) for commenting many lines simultaneously
            x = PLAYER_POS[0]
            y = PLAYER_POS[1]  # Just grabbing the x and y coordinates

            if event.key == pygame.K_LEFT:  # When left key is pressed
                x -= PLAYER_SIZE  # Decrementing the position of x by PLAYER_SIZE (moving it by one whole block)

            elif event.key == pygame.K_RIGHT:  # When right key is pressed
                x += PLAYER_SIZE  # Incrementing the position of x by PLAYER_SIZE (moving it by one whole block)

            elif event.key == pygame.K_UP:
                y -= PLAYER_SIZE

            elif event.key == pygame.K_DOWN:
                y += PLAYER_SIZE

            PLAYER_POS = [x, y]  # We are passing in the new x and y values

            PLAYER_POS = limit(PLAYER_POS)  # Calling the limit function

    screen.fill(BACKGROUND_COLOR)  # It takes in an RGB value and updates the screen

    drop_enemies(ENEMY_LIST)   # Calling the drop enemies function
    score = update_enemy_positions(ENEMY_LIST, score)  # It updates the enemy position and stores the score value
    # print(score)  # Prints score to the console
    SPEED = set_level(score, SPEED)

    text = "Score:" + str(score)  # Storing our score to "text" variable
    final_score = "Final Score: " + str(score)
    msg = "Better Luck next time!!"
    label1 = myFont.render(text, 1, YELLOW)  #
    screen.blit(label1,  (WIDTH-200, HEIGHT-50))# Attaching our label to screen

    if collision_check(ENEMY_LIST, PLAYER_POS):   # It will enter the loop only when the function returns True
        label2 = endFont.render(final_score, 1, RED)  # The font will be printed in "red"
        label3 = endFont.render(msg, 1, (0, 255, 0))
        screen.blit(label2, (250, 250))  # It updates text to the specific part(position) of the screen
        screen.blit(label3, (250, 300))

        game_over = True
        # break  # It breaks out of the loop without showing the overlap

    draw_enemies(ENEMY_LIST)   # Calling the draw enemy function


    # Drawing the player rectangle
    pygame.draw.rect(screen, RED, (PLAYER_POS[0], PLAYER_POS[1], PLAYER_SIZE, PLAYER_SIZE))  # rect(Surface, Color, Rect, width=0) Look pygame documentatioN

    clock.tick(30)  # Setting the clock to 30 frames per second

    pygame.display.update()  # It will update the changes on our screen each time

    if game_over:
        pygame.time.wait(3000)  # The wait value is in millisecond hence here the wait is 3 seconds


