import turtle as t
import os

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#game border
cursor = t.Turtle()
cursor.speed(0)                        # 0 - fastest spd, cursor draws the border
cursor.color("white")
cursor.penup()                          # disable line drawing until pendown cmd executes, penup - pen(cursor) is in the air while moving it
cursor.setposition(-300,-300)
cursor.pendown()                        # starts drawing wherever it moves
cursor.pensize(5)                       # size  of line drawing
for side in range(4):
    cursor.fd(600)
    cursor.lt(90)
cursor.hideturtle()





delay = input("ok")