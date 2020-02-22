import turtle as t
import os
import math

#screen
screen = t.Screen()
screen.bgcolor("black")
screen.title("Space Invaders")

#game ui & border
cursor = t.Turtle()
cursor.color("green")
cursor.penup()                          # disable line drawing until pendown cmd executes, penup - pen(cursor) is in the air while moving it
cursor.speed(0)                         # 0 - fastest spd, cursor draws the border
cursor.setposition(-300,-300)           # position to bottom left
cursor.pendown()                        # starts drawing again whenever it moves
cursor.pensize(3)                       # size  of line drawing
for side in range(4):                   # taking all 4 sides
    cursor.fd(600)                      # horizontal lines (top & bottom sides)
    cursor.lt(90)                       # vertical lines (right & left sides)
cursor.hideturtle()

#player(ship) ui
player = t.Turtle()
player.shape("classic")
player.shapesize(1.8)
player.color("blue")
player.penup()
player.speed(0)                         # 0 - fastest speed
player.setposition(0,-250)
player.setheading(90)                   # 90 - facing towards upward direction

#player movement
player_spd = 15
def move_left():
    x = player.xcor()                   # set x coordinate of player as value of x i.e 0
    x -= player_spd                     # set x = -15 every time we press left key
    if x<-280:                          # boundary checking for left side
        x = -280    
    player.setx(x)                      # set new x coordinate of player
    
def move_right():
    x = player.xcor()
    x += player_spd
    if x>280:                           # boundary checking for right side
        x = 280
    player.setx(x)
    
#enemy ui
enemy = t.Turtle()
enemy.shape("turtle")
enemy.shapesize(1.5)
enemy.color("red")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200,250)
enemy.settiltangle(-90)                 #change the angle of the shape irrespective of its heading direction, It'll still head right & left

enemy_spd = 2

#bullet ui
bullet = t.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.7)
bullet.hideturtle()                     #shown only when fired

bullet_spd = 20

#bullet first position
''' there r 2 states of bullet - readytofire state, fire state, because bullet will be fired only when earlier bullet is disappeared i.e when bullet comes in readytofire state from fire state again'''
bullet_state = "readytofire"
def bfire():
    global bullet_state
    #we make this global so that any changes made here will also change the original variable which is outside this fn
    if bullet_state == "readytofire":
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()
        bullet_state = "fire"

#bullet collision with enemy using 'pythagoras theoram'
def bulletEncounteredEnemy(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))     # math.pow(a,b), a-base,b-power
    if distance<15:                                                                             # math.sqrt(c)
        return True
    else:
        return False
        
#keyboard binding, key's working
t.listen()                              # listen to keyboard action
t.onkey(move_left,"Left")               # when left key is pressed 'move_left' fn is called
t.onkey(move_right,"Right")             # when right key is pressed 'move_right' fn is called
t.onkey(bfire,"space")                  # when spacebar is pressed 'fire' fn is called

#game loop
while True:
    #enemy movement
    x = enemy.xcor()
    x += enemy_spd
    enemy.setx(x)
    
    #right -->
    if x>280:
        y = enemy.ycor()
        y -= 25                         # when enemy touches right boundry it'll get down by 25 pixels
        enemy.sety(y)
        enemy_spd *= -1
        
    
    #left -->
    if x<-280:
        y = enemy.ycor()
        y -= 25                         # when enemy touches left boundry it'll get down by 25 pixels
        enemy.sety(y)
        enemy_spd *= -1 #-->
        #the moment enemy goes left 'enemy_spd' becomes negative(i.e -2) so we multiply it with -1 to make it positive(i,e 2) to go in right
        
    #bullet movement
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_spd
        if y<276:	                    #not yet bullet collision with top boundary
            bullet.sety(y)
        else:                           #now bullet collision with top boundary
            bullet.hideturtle()
            bullet_state = "readytofire"
    
    #after bullet collision with enemy
    if bulletEncounteredEnemy(bullet,enemy):
        enemy.hideturtle()
        bullet.hideturtle()
        bullet_state = "readytofire"
        bullet.setposition(0,0)
        

delay = input("press any key to end!")