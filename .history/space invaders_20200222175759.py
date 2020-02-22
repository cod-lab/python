import turtle as t
import os

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#game border
cursor = t.Turtle()
cursor.color("orange")
cursor.penup()                          # disable line drawing until pendown cmd executes, penup - pen(cursor) is in the air while moving it
cursor.speed(0)                         # 0 - fastest spd, cursor draws the border
cursor.setposition(-300,-300)           # position to bottom left
cursor.pendown()                        # starts drawing again whenever it moves
cursor.pensize(3)                       # size  of line drawing
for side in range(4):                   # taking all 4 sides
    cursor.fd(600)                      # horizontal lines (top & bottom sides)
    cursor.lt(90)                       # vertical lines (right & left sides)
cursor.hideturtle()

#player ship ui
ship = t.Turtle()
ship.color("blue")
ship.shape("triangle")
ship.penup()
ship.speed(0)                           # 0 - fastest speed
ship.setposition(0,-250)
ship.setheading(90)                     # 90 - facing towards upward direction

#player ship movement
ship_spd = 15
def move_left():
    x = ship.xcor()                     # set x coordinate of ship as value of x i.e 0
    x -= ship_spd                       # set x = -15 every time we press left key
    if x<-280:                          # boundary checking for left side
        x = -280    
    ship.setx(x)                        # set new x coordinate of ship
    
def move_right():
    x = ship.xcor()
    x += ship_spd
    if x>280:                           # boundary checking for right side
        x = 280
    ship.setx(x)
    
# keyboard binding, key's working
t.listen()                             # listen to keyboard action
t.onkey(move_left,"Left")              # when left key is pressed 'move_left' fn is called
t.onkey(move_right,"Right")            # when right key is pressed 'move_right' fn is called

#enemy ui
enemy = t.Turtle()
enemy.color("red")
enemy.shape("turtle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
#enemy.settiltangle(-90)               #change the angle of the shape irrespective of its heading direction, It'll still head right

enemy_spd = 2

# game loop
while True:
    #enemy movement
    #right -->
    x = enemy.xcor()
    x += enemy_spd
    enemy.setx(x)
    
    if x>280:
        x -=enemy_spd
    enemy.setx(x)


delay = input("press any key to end!")