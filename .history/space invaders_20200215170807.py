import turtle as t
import os

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#game border
cursor = t.Turtle()
cursor.speed(0)         # 0 - fastest spd
cursor.color("white")
cursor.penup()
cursor.setposition(-300,-300)
''' cursor.pendown()
cursor.pensize(3)
for side in range(4):
    cursor.fd(600)
    cursor.lt(90)
cursor.hideturtle() '''





delay = input("ok")