import turtle as t
import os
import math
import random as r

#screen
screen = t.Screen()
#screen.bgcolor("black")
screen.bgpic("giphy (2).gif")
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

#creating score
score = 0
scorestr = "score: %s" %score
score_pen =t.Turtle()
score_pen.color("white")
score_pen.speed(0)
score_pen.penup()
score_pen.setposition(-290,280)
score_pen.pensize(1)
score_pen.write(scorestr,False,"left",font=("Cookies",15,"normal")) 
score_pen.hideturtle()

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
player_spd = 30
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
no_of_enemies = 10
enemies = []
for i in range(no_of_enemies):
    enemies.append(t.Turtle())
#print("enemy list",enemies)
for enemy in enemies:
    #enemy = t.Turtle()
    enemy.shape("turtle")
    enemy.shapesize(1.5)
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = r.randint(-200,200)             #choose a random no. between -200 & 200
    y = r.randint(100,250)              #didn't understand the coordinate system for y!!!
    enemy.setposition(x,y)
    enemy.settiltangle(-90)             #change the angle of the shape irrespective of its heading direction, It'll still head right & left

enemy_spd = 5

#bullet ui
bullet = t.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.7)
bullet.hideturtle()                     #hiding now...shown only when fired

bullet_spd = 25

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

#universal collision fn for 'checking' multiple collisions using 'pythagoras theoram'
def collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))     # math.pow(a,b), a-base,b-power, math.sqrt(c)
    if distance<20:
        return True
    else:
        return False
    """ if abs(t1.xcor() - t2.xcor())<20 and abs(t1.ycor() - t2.ycor())<20: #- not working properly
        return True
    else:
        False """
        
#keyboard binding, key's working
t.listen()                              # listen to keyboard action
t.onkey(move_left,"Left")               # when left key is pressed 'move_left' fn is called
t.onkey(move_right,"Right")             # when right key is pressed 'move_right' fn is called
t.onkey(bfire,"space")                  # when spacebar is pressed 'fire' fn is called

#game loop
while True:
    for enemy in enemies:
        #enemy movement
        x = enemy.xcor()
        x += enemy_spd
        enemy.setx(x)
        
        #right -->
        if x>280:
            for e in enemies:           #loop to move all the enemies down after any one touching boundary
                y = e.ycor()
                y -= 25                 #when enemy touches right boundry it'll get down by 25 pixels
                e.sety(y)
            enemy_spd *= -1             #change direction, it will be same for all enemies thats y its not included in the loop
            
        #left -->
        if x<-280:
            for e in enemies:           #loop to move all the enemies down after any one touching boundary
                y = e.ycor()
                y -= 25                 #when enemy touches left boundry it'll get down by 25 pixels
                e.sety(y)
            enemy_spd *= -1 #-->         change direction
            #the moment enemy goes left 'enemy_spd' becomes negative(i.e -2) so we multiply it with -1 to make it positive(i,e 2) to go right
            
        #collisions 'aftermath'
        #after bullet collided with enemy
        if collision(bullet,enemy):
            #reseting enemy
            x = r.randint(-200,200)     #choose a random no. between -200 & 200
            y = r.randint(100,250)      #!!!didn't understand the coordinate system for y!!!
            enemy.setposition(x,y)
            
            #reseting bullet
            bullet.hideturtle()
            bullet_state = "readytofire"
            bullet.setposition(player.xcor(),player.ycor()-10)
            
            #increasing score and displaying it
            score += 10
            scorestr = "score: %s" %score           #updating 'scorestr' with new score
            score_pen.clear()
            #deleting what drawn earlier(previous score of current game session) and writing new score because otherwise it'll write on the previous text(which is a drawing here)
            score_pen.write(scorestr,False,"left",font=("Cookies",15,"normal"))             #writing the new score of current game session
        
        #after enemy collided with player while coming down
        if collision(enemy,player):
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break

    #bullet movement
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_spd
        if y<276:	                    #not yet bullet collided with top boundary
            bullet.sety(y)
        else:                           #now bullet collided with top boundary
            bullet.hideturtle()
            bullet_state = "readytofire"
            
        

delay = input("press any key to end!")