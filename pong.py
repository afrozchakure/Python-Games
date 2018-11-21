# Referred video https://www.youtube.com/watch?v=LH8WgrUWG_I

import turtle  # Turtle module is used for drawing shapes
import os    # Its a module used for adding sound to our game
import time  # importing the time module to add delay to our code

delay = 3  # Setting the delay variable to 0.1 seconds

wn=turtle.Screen()  # creating a screen
wn.title("Pong by Afroz")
wn.bgcolor("black") # setting the background color to black
wn.setup(width=800,height=600) # changing the size of the window
wn.tracer(0) # actually stops the window from updating(makes the game work much faster)

# Score
score_a = 0  # Its the default score for both the players
score_b = 0



# Paddle A
paddle_a=turtle.Turtle() # The small 't' is module name and the capital 'T' is the class name
paddle_a.speed(0) # This is the speed of animation (it sets the speed to the maximum possible speed)
paddle_a.shape("square") # using built in shape "square"
paddle_a.color("Red")  # giving color to paddle
paddle_a.shapesize(stretch_wid=5,stretch_len=1)  # stretch the paddle
paddle_a.penup()   # turtles draw a line by definition but we don't need lines(its opposite of pendown-tells we are not drawing lines)
paddle_a.goto(-350,0)  # it sets the position of paddle_a #see the width and then adjust the position

# Paddle B
paddle_b=turtle.Turtle() # The small 't' is module name and the capital 'T' is the class name
paddle_b.speed(0) # This is the speed of animation (it sets the speed to the maximum possible speed)
paddle_b.shape("square") # using built in shape "square"
paddle_b.color("Blue")  # giving color to paddle
paddle_b.shapesize(stretch_wid=5,stretch_len=1)  # stretch the paddle
paddle_b.penup()   # turtles draw a line by definition but we don't need lines
paddle_b.goto(350,0)  # since the paddle b is on the right side its value is positive 350



# Ball

ball=turtle.Turtle() # The small 't' is module name and the capital 'T' is the class name
ball.speed(0) # This is the speed of animation (it sets the speed to the maximum possible speed)
ball.shape("circle") # using built in shape "square"
ball.color("white")  # giving color to ball
ball.penup()   # turtles draw a line by definition but we don't need lines
ball.goto(0,0)   # position of ball in the window
ball.dx=0.1  # It moves towards the positive x by 0.1 pixels
ball.dy=-0.1  # The ball moves towards the positive y by 0.1 pixels (i.e. the ball moves diagonally with a positive slope)

# Pen
pen=turtle.Turtle()
pen.speed(0) # Animation speed
pen.color("white")
pen.penup()  # This is because we don't want it to draw a line when it moves
pen.hideturtle() # We don't need to see it (we just want to see the text not the turtle
pen.goto(0,260) # It will set the text at this position
pen.pencolor("Yellow")
pen.write("Player A: 0  Player B: 0",align="center",font=("Courier",20,"normal"))  # Its the default score on the screen


# Function

def paddle_a_up():
    y=paddle_a.ycor() # It assigns the y-coordinate of paddle_a to y
    y+=20 # It adds 20 pixels to the y coordinate
    paddle_a.sety(y)   # Its sets the y-coordinate of paddle_a to new "y"


def paddle_a_down():
    y=paddle_a.ycor()
    y-=20    # It subtracts 20 pixel from the y variable
    paddle_a.sety(y)  # sets the y-coordinate of paddle_a to new "y"


def paddle_b_up():
    y=paddle_b.ycor() # It assigns the y-coordinate of paddle_b to y
    y+=20       # It adds 20 pixels to the y cordinate
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)


# Keyboard binding
wn.listen() # It tells the turtle module to listen from keyboard input
wn.onkeypress(paddle_a_up, "w")  # When the user presses the key "w", call the function paddle_a_up()
wn.onkeypress(paddle_a_down, "s") # When the user presses the key "s",call the function paddle_a_down()

wn.onkeypress(paddle_b_up, "Up")  # for the up key its capital U and small p
wn.onkeypress(paddle_b_down, "Down") # notice that the curved brackets are not present in paddle_b_down function

game_over=False
# Main game loop
while not game_over:
    wn.update()  # Everytime the loop runs it updates the screen

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)  # Combining what we did inside the #BAll comment
    ball.sety(ball.ycor()+ball.dy)  # Combining the initial position to the subsequent increase

    # Border checking
    # we want our ball to bounce from the borders when it hits one
    if ball.ycor()>290:  # If y-co-ordinate of ball is greater than 290 pixels
        ball.sety(290)   # Sets the y-coordinate of ball to 290
        ball.dy *= -1  # It reverses the direction of the ball since here it changes -dy/dx ie,the slope
        os.system("aplay bounce.wav&")  # Every time the ball hits the wall it plays the sound

    if ball.ycor() < -290:  # It makes the ball jump from the bottom of the screen
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:  # When the ball reaches the x coordinate==390 it replaces the ball at the center
        ball.goto(0, 0)    # Puts the ball at the center
        ball.dx *= -1      # Changing the direction of the ball (It travels towards the paddle opposite to where it ends)
        score_a += 1  # Updating the score
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()  # It helps to clear the previous score
        pen.write("Player A: {}  Player B: {}". format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    # Paddle and ball collisions
    # For paddle_b
    if ((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < (paddle_b.ycor() + 40) and ball.ycor() > (paddle_b.ycor() - 40))):
            #checks whether the ball is either top of the paddle or below the paddle
        ball.dx *= -1
        ball.setx(340)
        os.system("aplay bounce.wav&")  # It plays the sound when the ball hits the paddle

    # For paddle_a
    if (ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40)):
        ball.dx*=-1    # The ball reverses its direction after hitting the paddle
        ball.setx(-340)  # After the ball hits the paddle it resumes from this position
        os.system("aplay bounce.wav&")

    # Paddle and border
    if paddle_a.ycor()+50>290:   # When the paddle hits the border it should restrict its movement to the playing area
        paddle_a.sety(240)

    if paddle_a.ycor()-50<-290:
        paddle_a.sety(-240)

    if paddle_b.ycor()+50>290:
        paddle_b.sety(240)

    if paddle_b.ycor()-50<-290:
        paddle_b.sety(-240)

    # Displaying the winner and exiting the screen
    if score_a==2:
        pen.clear()  # It clears the previous screen
        pen.color("red")   # Displays the following text in red color
        time.sleep(0.5)
        pen.write("Player A WON!!!",align="center",font=("courier",20,"normal"))  # Displays the victory message
        time.sleep(delay)
        game_over=True   # It exits the game

    if score_b==2:
        pen.clear()
        pen.color("blue")
        time.sleep(0.5)  # time.sleep takes in value of time in seconds
        pen.write("Player B WON!!",align="center",font=("courier",20,"normal"))
        time.sleep(delay)  # After the player wins it helps displaying the message on the screen before exiting
        game_over=True
