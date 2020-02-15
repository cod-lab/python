import turtle as t
import os

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#border
border = t.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(3):
    border.fd(600)
    border.lt(90)






delay = input("ok")