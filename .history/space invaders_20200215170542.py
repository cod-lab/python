import turtle as t
import os

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#border
border = t.Turtle()
border.speed(0)         # 0 - fastest spd
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(600)
    border.lt(90)
border.hideturtle()





delay = input("ok")