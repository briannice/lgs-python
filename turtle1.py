from turtle import Turtle, Screen

# Create screen
WIDTH = 500
HEIGHT = 500
screen = Screen()
screen.setup(WIDTH, HEIGHT)

# Aanmaken van een turtle.
guido = Turtle()

# setpos
guido.penup()
guido.setpos(-200, 200)
guido.pendown()
guido.setpos(200, 200)
guido.setpos(200, -200)
guido.setpos(-200, -200)
guido.setpos(-200, 200)
guido.penup()

# shape
guido.shape("turtle")

# speed
guido.speed(1)

# forward and right
guido.setpos(-100,100)
guido.hideturtle()
guido.pendown()
guido.forward(200)
guido.right(90)
guido.forward(200)
guido.right(90)
guido.forward(200)
guido.right(90)
guido.forward(200)
guido.showturtle()
guido.penup()

# clear
guido.clear()

screen.bgcolor("purple")

# forward, setheading, left
guido.setpos(0,-100)
guido.color("red")
guido.begin_fill()
guido.pendown()
guido.setheading(45)
guido.forward(100)
guido.left(90)
guido.forward(100)
guido.left(90)
guido.forward(100)
guido.left(90)
guido.forward(100)
guido.end_fill()
guido.penup()

# Show screen
screen.exitonclick()