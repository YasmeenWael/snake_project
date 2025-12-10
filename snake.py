import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
wn = turtle.Screen()
wn.title("The Snake Game With Python")
wn.bgcolor("#222")
wn.setup(width=600, height=600)
wn.cv._rootwindow.resizable(False, False)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("brown")
head.penup()
head.speed(0)
head.goto(0, 0)
head.penup()
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(["#FFF","yellow", "#ff0000", "#00ff00", "#0000ff", "purple"])#white,red,green,blue
shapes = random.choice(["square", "circle", "triangle"])
food.shape(shapes)
food.color(colors)
food.penup()
food.speed(0)

def place_food():
    while True:
        x = random.randint(-270, 270)
        y = random.randint(-270, 230)  # Keep y-coordinate away from the score display area
        if y < 200 or y > 300:  # Adjust these values if needed
            food.goto(x, y)
            break

place_food()

# create pen
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 250)
pen.hideturtle()
pen.write("Score: 0   High Score: 0", align="center", font=("Arial", 24, "bold"))

# function to show game over
def game_over():
    pen.goto(0, 0)
    pen.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
    time.sleep(2)
    pen.clear()
    pen.goto(0, 250)
    pen.write("Score: {}   High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

# assigning key directions
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
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

# key binding
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
segments = []

# Main Gameplay
while True:
    wn.update()

    # Checking for head collisions with borders
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        game_over()
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(["#FFF",  "yellow", "#ff0000", "#00ff00", "#0000ff", "purple"])
        shapes = random.choice(["square", "circle", "triangle"])
        food.shape(shapes)
        food.color(colors)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(
            "Score: {}   High Score: {}".format(score, high_score),
            align="center",
            font=("Arial", 24, "bold"),
        )

    # Checking for head collisions with food
    if head.distance(food) < 20:
        place_food()

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("orange")  # tail color
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001  # increase game difficulty
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(
            "Score: {}   High Score: {}".format(score, high_score),
            align="center",
            font=("Arial", 24, "bold"),
        )

    # Shifting all snake body (segments[]) then move the (head)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Checking for head collisions with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            game_over()
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(["#FFF", "yellow", "#ff0000", "#00ff00", "#0000ff", "purple"])
            shapes = random.choice(["square", "circle", "triangle"])
            food.shape(shapes)
            food.color(colors)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(
                "Score: {}   High Score: {}".format(score, high_score),
                align="center",
                font=("Arial", 24, "bold"),
            )

    time.sleep(delay)


