from turtle import Turtle, Screen

# Create screen
WIDTH = 500
HEIGHT = 500
screen = Screen()
screen.setup(WIDTH, HEIGHT)

# Aanmaken van een turtle.
guido = Turtle()

guido.color('red', 'yellow')
guido.begin_fill()
while True:
    guido.forward(200)
    guido.left(170)
    if abs(guido.pos()) < 1:
        break
guido.end_fill()

# Show screen
screen.exitonclick()