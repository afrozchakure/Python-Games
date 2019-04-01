# Space Invaders
import turtle
import os
import math
import random  # To make the enemy start from random positions

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invader_background.gif")

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

# Draw Border
border_pen = turtle.Turtle()   # Creating a Turtle
border_pen.speed(0)  # Setting the speed of drawing diagrams
border_pen.color("white")
border_pen.penup()  # It will lift the pen and will prevent it from drawing
border_pen.setposition(-300, -300)  # The center is (0,0)
border_pen.pensize(3)  # Setting pensize
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)  # Moving forward
    border_pen.lt(90)   # Moving left 90 degrees
border_pen.hideturtle()  # Hiding the turtle cursor

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-270, 260)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Ariel",14,"normal"))
score_pen.hideturtle()

# Draw Game Over
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color('red')
game_over.penup()
game_over.setposition(-230, 260)
game_over.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)   # Set the space ship facing upwards (since default position faces right side)


playerspeed = 15  # Setting the players speed


# Choose the number of enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)   # Starts each enemy at a different spot
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)  # drawing speed
bullet.setheading(90)   # So that the bullet points up
bullet.shapesize(0.5, 0.5)      # Making the bullet size half of player size
bullet.hideturtle()  # When the game starts we want our bullet to be hidden

bulletspeed = 20  # setting the bullet speed more the playerspeed

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"  # Bullet is ready to fire

# Move the player left and right
def move_left():
    x = player.xcor()
    #y = player.ycor()
    x = x - playerspeed  # x = x - playerspeed ( Changing value of x each time )
    if x < -280:  # Blocking the player from crossing
        x = - 280
    player.setx(x)  # setting the player's location to new x

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global if it needs changed
    global bulletstate  # global variables can be read in python ( any changes in this function are reflected globally)

    if bulletstate == "ready":
        os.system("aplay laser.wav&")  # To play the sound when the bullet is fired
        bulletstate = "fire"  # changing the bulletstate to fire
        # Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10  # Each time the function is called the bullet moves 10 units above player position
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))  # (x^2 + y^2)^0.5
    if distance < 15:
        return True
    return False


# Create keyboard bindings
turtle.listen()   # Turtle is listening to your response
turtle.onkeypress(move_left, "Left")  # On pressing the left key turtle will call the mov_left() function
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")  # Keyboard binding

# Main game loop
while True:
    for enemy in enemies:   # It loops through all elements in enemy and tests their condition
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:  # Boundary Checking
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40   # Every time the enemy hits the borders the enemy drops down by 40
                e.sety(y)   # Setting enemy position to the new y
            # Change enemy direction
            enemyspeed *= -1  # Each time the enemy hits the boundary it reverses its direction

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemyspeed *= -1

        # Check collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            os.system("aplay explosion.wav&")

            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"  # So that we can fire the bullet again
            bullet.setposition(0, -400)  # It moves the bullet off the screen
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Ariel", 14, "normal"))

            # Reset the enemy
            x = random.randint(-200, 200)  # Starts each enemy at a different spot
            y = random.randint(100, 250)
            enemy.setposition(x, y)

        # Check if there is collision between the player and the enemy
        if isCollision(player, enemy):
            os.system("aplay explosion.wav&")
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            gameoverstr = "Game Over: Your Score: %s" % score
            gameover.write(gameoverstr, False, align="left", font=("Ariel", 14, "normal"))
            exit(0)
            break


    # Move the bullet
    if bulletstate == "fire":  # We want to move the bullet only when it is "fire" state and not in "ready" state
        y = bullet.ycor()
        y += bulletspeed  # To move the bullet
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()   # Hiding the turtle when the bullet reaches the top
        bulletstate = "ready"  # Allows us to fire another bullet on reaching the top


delay = input("Press Enter to finish.")