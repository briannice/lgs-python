from turtle import Turtle, Screen

# Create screen
WIDTH = 500
HEIGHT = 500
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

guido = Turtle()
guido.color('black')

for x in range(360):
    guido.pencolor(colors[x%6])
    guido.width(x//100 + 1)
    guido.forward(x)
    guido.left(59)

screen.exitonclick()