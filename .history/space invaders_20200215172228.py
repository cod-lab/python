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
cursor.setposition(-300,-300)           # position to bottom left
cursor.pendown()                        # starts drawing again whenever it moves
cursor.pensize(3)                       # size  of line drawing
for side in range(4):                   # taking all 4 sides
    cursor.fd(600)                      # horizontal lines (up & down sides)
    cursor.lt(90)                       # vertical lines (right & left sides)
cursor.hideturtle()





delay = input("ok")