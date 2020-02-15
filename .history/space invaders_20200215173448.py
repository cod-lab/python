import turtle as t
import os

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#game border
cursor = t.Turtle()
cursor.color("white")
cursor.penup()                          # disable line drawing until pendown cmd executes, penup - pen(cursor) is in the air while moving it
cursor.speed(0)                         # 0 - fastest spd, cursor draws the border
cursor.setposition(-300,-300)           # position to bottom left
cursor.pendown()                        # starts drawing again whenever it moves
cursor.pensize(3)                       # size  of line drawing
for side in range(4):                   # taking all 4 sides
    cursor.fd(600)                      # horizontal lines (up & down sides)
    cursor.lt(90)                       # vertical lines (right & left sides)
cursor.hideturtle()

#player ship ui
ship = t.Turtle()
ship.color("blue")
ship.shape("triangle")
ship.penup()
ship.speed(0)
ship.setposition(0,-250)
ship.setheading(90)                     # 90 - facing toward upward direction

#player ship movement
ship_spd = 15
def move_left:
    x = ship.xcor()                     # set x coordinate of ship as value of x i.e 0
    x -= ship_spd                       # set x = -15 every time we press key
    ship.setx(x)                        # set new x coordinate of ship








delay = input("ok")