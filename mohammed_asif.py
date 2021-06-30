# import turtle package
import turtle

# Mohammed_Asif-3-Chess Board (turtle)

# create turtle object
pen = turtle.Turtle()

# hides the pointer of turtle
pen.hideturtle()

# Increases drawing speed
pen.speed(100)

# setting up the beginning position
pen.penup()
pen.goto(-200, -150)
pen.pendown()


def draw():
    """This function will draw a square"""
    for k in range(4):
        pen.right(90)
        pen.forward(50)


# looping for getting a board
for i in range(1, 9):

    # drawing squares as row
    for j in range(1, 9):
        # set position for new square
        pen.forward(50)

        # calling function to draw each square
        draw()

    # checks whether the board is drawn . if drawn breakes the loop
    if i == 8:
        break

    # repositioning the pointer to draw the next row
    else:
        pen.backward(50 * 8)
        pen.left(90)
        pen.forward(50)
        pen.right(90)

# stops execution
turtle.done()
