#packages
import pygame as pg
import random as r
import tkinter as t
import winsound as w
from playsound import playsound as ps
from pydub import AudioSegment as aus
from pydub.playback import play as p

pg.init()
#pg.font.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (54,198,83)
blue = (30,144,255)
grey = (128,128,128)
yellow = (255,255,0)

#ui variables
game_caption = "snake2"
screen_widgth = 1000
screen_height = 500
box_width = 990
box_height = 400
snake_size = 10
food_size = 10
speed = 5

gamewindow = pg.display.set_mode((screen_widgth,screen_height))
boxwindow = pg.display.set_mode((box_width,box_height))
pg.display.set_caption(game_caption)
pg.display.update()

clock = pg.time.Clock()
fps = 30

#texts
font = pg.font.SysFont('Whimsy TT',35)
def text_screen(txt1,txt2,clr1,clr2,x1,y1,x2,y2):
    screen_txt1 = font.render(txt1,True,clr1)
    screen_txt2 = font.render(txt2,True,clr2)
    gamewindow.blit(screen_txt1,[x1,y1])
    gamewindow.blit(screen_txt2,[x2,y2])

def snake(boxwindow,black,snake_list,snake_size):
    for x,y in snake_list:
        pg.draw.rect(boxwindow,black,[x,y,snake_size,snake_size])

def gameloop():
    #game processing variables
    exitgame = False
    gameover = False
    score = 0
    velocity_x = 0
    velocity_y = 0
    #fps = 30
    
    snake_x = 100
    snake_y = 150
    food_x = r.randint(0,box_width)
    food_y = r.randint(0,box_height)
    
    #snake length
    snake_length = 1
    snake_list = []
    
    #game loop
    while exitgame != True:
        if gameover == True:
            #w.PlaySound("death.wav", w.SND_ALIAS )                #gives sound effects in windows
            #w.PlaySound(None, w.SND_PURGE)
            #ps('end.mp3')
            #ps('',False)
            #ps('end.wav')
            #song = aus.from_file('end.wav', 'wav')
            #p(song)
            
            boxwindow.fill(grey)
            text_screen("GAME OVER!","press ENTER to play again...",blue,yellow,250,160,230,200)
            
            #w.PlaySound("end.wav", w.SND_ASYNC | w.SND_ALIAS )                #gives sound effects in windows
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exitgame = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        #w.PlaySound(None, w.SND_ALIAS)
                        gameloop()
        else:
            #w.PlaySound(None, w.SND_ASYNC)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exitgame = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        velocity_x = speed
                        velocity_y = 0
                        #event.key != pg.K_LEFT
                    if event.key == pg.K_LEFT:
                        velocity_x = -speed
                        velocity_y = 0
                        #event.key != pg.K_RIGHT
                    if event.key == pg.K_UP:
                        velocity_x = 0
                        velocity_y = -speed
                        #event.key != pg.K_DOWN
                    if event.key == pg.K_DOWN:
                        velocity_x = 0
                        velocity_y = speed
                        #event.key != pg.K_UP
            
            ''' for event in pg.event.get():
                #if event.type == pg.KEYDOWN:
                if velocity_x == speed:
                    pg.K_LEFT = False 
                elif velocity_x == -speed:
                    pg.K_RIGHT = False
                elif velocity_y == -speed:
                    pg.K_DOWN = False
                else:
                    pg.K_UP = False '''
            
            #snake movement
            snake_x += velocity_x
            snake_y += velocity_y
                
            #collision or eating food
            #c = 10
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                #ps('f.wav')
                w.PlaySound("f.wav", w.SND_ASYNC)                #gives sound effects in windows
                #song = aus.from_wav('eat.wav')
                #p(song)
                
                score += 10
                snake_length += 2
                food_x = r.randint(0,box_width)
                food_y = r.randint(0,box_height)
                #c += 20
                
            gamewindow.fill(grey)
            boxwindow.fill(white)
            text_screen("sNake GaMe","score: " + str(score),green,red,10,5,800,5)
            pg.draw.rect(boxwindow,red,[food_x,food_y,10,10])
            
            #snake head for length
            snake_head = []
            snake_head.append(snake_x)
            snake_head.append(snake_y)    

            snake_list.append(snake_head)
            #print(snake_list)
            if len(snake_list) > snake_length:                      #if no. of lists of snake is more than snake length:
                del(snake_list[0])
            
            #snake eating itself (game over)
            ''' for x in snake_list:
                if abs(x[1] - snake_head[1])<5 and abs(x[2] - snake_head[2])<5:
                    exitgame = True '''
            
            if (snake_head in snake_list[:-1]) or (snake_x or snake_y)<0 or (snake_x>box_width) or (snake_y>box_height):     #list[-1]or[:-1] -> starting from last item
                gameover = True
                w.PlaySound("round_end.wav", w.SND_NOSTOP)                #gives sound effects when game is over (for windows)
                w.PlaySound("end.wav", w.SND_ASYNC | w.SND_ALIAS )                #gives sound effects in windows
                
            snake(boxwindow,black,snake_list,snake_size)
            
            """ e=[i*i for i in range(1,6)]
            #print("e is " + str(e))
            #print("e is " + str(e[-3:]))
            print("e is " + str(e[ :-1])) """

        pg.display.update()
        clock.tick(fps)
    pg.quit()
    quit()

gameloop()

'''
class game_screen
class snake
class food
class play_screen
'''