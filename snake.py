import turtle
import time  # Time module can be used to create a delay
import random  # It helps us choose random modules

delay = 0.1  # Setting delay variable to 0.1 seconds

# Score
score = 0  # Initialising variable score and high_score
high_score = 0


#Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Afroz")  # Setting the title of screen
wn.bgcolor("green")  # Setting the color
wn.setup(width=600, height=600)  # Setting up of the screen
wn.tracer(0)  # turns off the screen update (makes the module go as fast as possible)

# Snake game
head = turtle.Turtle()
head.speed(0)  # Setting the speed of animation
head.shape("square")
head.color("black")
head.penup()  # we don't want the turtle module to draw lines
head.goto(0, 0)  # Position of the head at the beginning
head.direction = "stop"  # When it starts it just sits there (here head.direction is assigned to "stop")

# Food

food = turtle.Turtle()
food.speed(0)  # Setting the speed of animation
food.shape("circle")
food.color("Red")
food.penup()  # we don't want the turtle module to draw lines
food.goto(0, 60)  # Position of the food at the beginning (The turtle module assigns the value to (0, 0) by default)

segments = []  # Creating an empty list for adding segments

# Pen
pen = turtle.Turtle()
pen.speed(0) # Animation speed
pen.shape("square")  # Just to be consistent
pen.color("White")
pen.penup()
pen.hideturtle()  # Since we do not want the turtle onscreen
pen.goto(0, 260)   # Position of the text on screen
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 20, "normal"))  # displaying default score onscreen


# Functions
def go_up():     # This function sets the value of head.direction to "right"
    if head.direction!="down":  # This restricts the movement of snake in one direction only
        head.direction="up"


def go_down():
    if head.direction != "up":
        head.direction="down"


def go_right():
    if head.direction != "left":
        head.direction="right"


def go_left():
    if head.direction != "right":
        head.direction="left"


def move():
    if head.direction == "up":
        y=head.ycor()  # Setting the current y-coordinate to variable y
        head.sety(y + 20)  # when we press the up button it will move the head by 20 pixels each time

    if head.direction == "down":
        y=head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

# Keyboard bindings


wn.listen()  # This will make the turtle module active to keypresses and clicks
wn.onkeypress(go_up, "Up")  # It will call the function go_up() when we press the "up" button
wn.onkeypress(go_down, "Down")  # Notice,sHere we don't have go_down with parenthesis ()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop:
while True:

    wn.update()  # Everytime it enters the loop it updates the screen

    # Check for a collision with the border
    if head.xcor() < -290 or head.xcor() > 290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)  # It pauses the game
        head.goto(0, 0)  # It resets the head back to (0,0) position
        head.direction = "stop"

        # Hide the segments:
        for segment in segments:
            segment.goto(1000, 1000)  # Could not find a way to actually delete a segment in turtle module

        # Clear the segments list
        segments.clear()  # To clear the list of segments

        # Reset the score
        score = 0

        # Reset the delay
        #delay = 0.1

        # Update the score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    # Check for the collision with the food
    if head.distance(food) < 20:  # If the distance between the head and the food is less than 20 pixels run the loop
        # Move the food to a random spot (It changes the position of the food when we hit it)
        x=random.randint(-290, 290)  # It chooses a random number from -290 to 290 and assigns it to x
        y=random.randint(-290, 290)
        food.goto(x, y)  # It places the food that position


        # Add a segment
        new_segment = turtle.Turtle()  # creating a turtle for additional segments
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()  # So that the new_segment does not draw on the screen
        segments.append(new_segment)  # It appends the new_segment to the segments list

        # Shorten the delay of text appearing on the screen
        #delay -= 0.001

        # Increase the score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()  # Before we write the new score on the screen we clear it
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 20, "normal"))

    # Move the end segments first in reverse  # Move the back to the front
    for index in range(len(segments)-1, 0, -1):  #  goes from 9 to 0 if length==10
        x = segments[index-1].xcor()  #
        y = segments[index-1].ycor()
        segments[index].goto(x, y)  # We want segment 9 to move to where segment 8 was previously

    # Move segment 0 to where the head is (It is special case)
    if len(segments) > 0:  # It is the segment after the head (It will do something if there are more than one segment)
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move() # Calling the function move

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 10: # When the distance between the head and segment is less than 10 pixels run this loop
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments:
            for segment in segments:
                segment.goto(1000, 1000)  # Could not find a way to actually delete a segment in turtle module

            # Clear the segments list
            segments.clear()  # To clear the list of segments

            # Reset score
            score = 0

            # Reset the delay
            #delay = 0.01

            # Update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 20, "normal"))

    time.sleep(delay)  # passing delay to time.sleep



wn.mainloop() # It keeps the screen open for us  # This is the last line of program

