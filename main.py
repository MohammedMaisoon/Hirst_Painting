import turtle
from turtle import *
import random
turtle.colormode(255)
dot=Turtle()
colors_list = [(198, 13, 32), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
dot.penup()
dot.hideturtle()
dot.setheading(225)
dot.forward(300)
dot.setheading(0)
for _ in range(10):
    for _ in range(10):
       dot.dot(20, random.choice(colors_list))
       dot.forward(50)
    dot.setheading(90)
    dot.forward(50)
    dot.setheading(180)
    dot.forward(500)
    dot.setheading(360)
screen=Screen()
screen.exitonclick()