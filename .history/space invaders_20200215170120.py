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
border.pensize(3)

delay = input("ok")