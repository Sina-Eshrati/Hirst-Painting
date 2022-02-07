import turtle
from random import choice
from turtle import Turtle, Screen

color_list = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
my_turtle = Turtle()
my_screen = Screen()
turtle.colormode(255)
my_turtle.penup()
my_turtle.speed(10)
my_turtle.hideturtle()
vertical = -200
for _ in range(10):
    my_turtle.goto(-215, vertical)
    for _ in range(10):
        my_turtle.dot(20, choice(color_list))
        my_turtle.forward(50)
    vertical += 50






my_screen.exitonclick()

