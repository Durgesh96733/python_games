import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("green")  # Green background
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off automatic screen updates to manually update the screen

# Snake head setup with triangle shape
head = turtle.Turtle()
head.shape("triangle")  # Use the triangle shape for the snake's head
head.color("red")  # Set the snake head color
head.penup()
head.goto(0, 0)
head.direction = "stop"  # Snake initially stops

# Snake body list
segments = []

# Food setup as yellow circle
food = turtle.Turtle()
food.shape("circle")  # Use circle shape for the food
food.color("yellow")  # Set food color to yellow
food.penup()
food.goto(0, 100)

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
        head.setheading(90)  # Make the triangle point up

def go_down():
    if head.direction != "up":
        head.direction = "down"
        head.setheading(270)  # Make the triangle point down

def go_left():
    if head.direction != "right":
        head.direction = "left"
        head.setheading(180)  # Make the triangle point left

def go_right():
    if head.direction != "left":
        head.direction = "right"
        head.setheading(0)  # Make the triangle point right

def move():
    # Move the head based on the direction
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Key bindings for Arrow Keys
screen.listen()  # Make the screen listen to key presses
screen.onkey(go_up, "Up")  # Use the Up arrow key to move up
screen.onkey(go_down, "Down")  # Use the Down arrow key to move down
screen.onkey(go_left, "Left")  # Use the Left arrow key to move left
screen.onkey(go_right, "Right")  # Use the Right arrow key to move right

# Main game loop
try:
    while True:
        screen.update()  # Update the screen at each iteration

        # Check for collision with the food
        if head.distance(food) < 20:
            food.goto(random.randint(-290, 290), random.randint(-290, 290))

            # Add a segment to the snake's body
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")  # Body segments will be square
            new_segment.color("red")  # Body color is red
            new_segment.penup()
            segments.append(new_segment)

        # Move the end segments first in reverse order
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()  # Move the snake head

        # Check for collision with the wall
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            head.goto(0, 0)
            head.direction = "stop"

            # Reset the segments list
            for segment in segments:
                segment.goto(1000, 1000)  # Move out of the screen
            segments.clear()

        # Check for collision with itself
        for segment in segments:
            if segment.distance(head) < 20:
                head.goto(0, 0)
                head.direction = "stop"

                # Reset the segments list
                for segment in segments:
                    segment.goto(1000, 1000)  # Move out of the screen
                segments.clear()

        time.sleep(0.1)  # Delay to control the speed of the snake

except turtle.Terminator:
    print("Turtle graphics window was closed.")
