# Hi
# My name is Juma Yunus also known as zekgyn
# This is my first Py game and the first time using python
# In this game we are going to code as simple Pong game just to test what we have learnt so far

import turtle

wn = turtle.Screen()
wn.title("Pong by @zekgyn")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Defines speed of the ball and its movement in x direction
ball.dy = -0.2  # Defines speed of the ball and its movement in y direction

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()  # Hides the line drawn(comment this to see what I mean)
pen.hideturtle()  # The turtle is hidden unlike the ball and the paddle we don't want to see this turtle
pen.goto(0, 260)  # Shows where the turtle is going to be positioned on the screen
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Key binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball(the following two lines of code defines ball movement in x y coordinate at the same time)
    ball.setx(ball.xcor() + ball.dx)  # Will move the ball in x axis
    ball.sety(ball.ycor() + ball.dy)  # Will move the ball in y axis

    # Border checking(recall wn.setup width and height)
    if ball.ycor() > 290:
        ball.sety(290)  # Sets the ball back to 290
        ball.dy *= -1  # reverses the direction of the ball

    if ball.ycor() < -290:  # For when ball is below the zero point (y is negative)
        ball.sety(-290)  # Sets the ball back to 290
        ball.dy *= -1  # reverses the direction of the ball

    if ball.xcor() > 390:
        ball.goto(0, 0)  # Back to the centre
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)  # Back to the centre
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 40):  # Original code is
        # (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() >
        # paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 40):  # Original code is
        # (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() >
        # paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
