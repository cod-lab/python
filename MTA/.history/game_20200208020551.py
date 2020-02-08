import pygame as pg
import random as r

pg.init()
pg.font.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (54, 198, 83)

#create window
speed=5
screen_width = 600
screen_height = 300
screen_caption = "snake game"
food_x = r.randint(0,screen_width/2)
food_y = r.randint(0,screen_height/2)

gamewindow = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption(screen_caption)
pg.display.update()

#game speciific variable
exitgame = False
gameover = False
score = 0
snake_x = 45
snake_y = 55
snake_size = 10
velocity_x = 0
velocity_y = 0
fps = 30
clock = pg.time.Clock()

#rendering font from pygame
font = pg.font.SysFont(None,55)
def text_screen(text1,text2,color1,color2,x1,y1,x2,y2):
    screen_text1 = font.render(text1,True,color1)
    screen_text2 = font.render(text2,True,color2)
    gamewindow.blit(screen_text1,[x1,y1])
    gamewindow.blit(screen_text2,[x2,y2])
    #pass

snk_len=1
snk_list=[]
def plot_snake(gamewindow,black,snk_list,snake_size2):
    for x,y in snk_list:
        pg.draw.rect(gamewindow,black,[x,y,snake_size2,snake_size2])

#game loop
while not exitgame:
    for event in pg.event.get():
        #print(event)
        if event.type == pg.QUIT:
            exitgame = True
        if event.type == pg.KEYDOWN:                    #on keypress
            if event.key == pg.K_RIGHT:
                #while event.key == pg.K_RIGHT:
                #snake_x += 5
                velocity_x = 5
                velocity_y = 0
            if event.key == pg.K_LEFT:
                #snake_x -= 5
                velocity_x = -5
                velocity_y = 0
            if event.key == pg.K_UP:
                #snake_y -= 5
                velocity_x = 0
                velocity_y = -5
            if event.key == pg.K_DOWN:
                #snake_y += 5
                velocity_x = 0
                velocity_y = 5

    snake_x += velocity_x
    snake_y += velocity_y
    if abs(food_x - snake_x)<10 and abs(food_y - snake_y)<10:
        score += 10
        snake_size += 10
        print("score=",score)

        food_x = r.randint(6,screen_width/2)
        food_y = r.randint(6,screen_height/2)
    gamewindow.fill(white)
    text_screen("sNaKe GaMe","score:" + str(score),green,red,5,5,400,5)
    #text_screen(,green,5,5)   def text_screen(text1,text2,color,x1,y1,x2,y2):
    pg.draw.rect(gamewindow, black, [snake_x,snake_y,snake_size, 10])
    pg.draw.rect(gamewindow, black, [food_x,food_y,10,10])
    plot_snake(gamewindow,black,snk_list,snake_size)

    pg.display.update()
    clock.tick(fps)

pg.quit()
quit()
