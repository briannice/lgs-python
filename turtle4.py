from turtle import Turtle, Screen

# Create screen
WIDTH = 500
HEIGHT = 500
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.colormode(255)

guido = Turtle()

r,g,b=255,0,0

for i in range(255*2):
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    guido.forward(50+i)
    guido.right(91)
    guido.color((r,g,b))

screen.exitonclick()