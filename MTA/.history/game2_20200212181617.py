#packages
import pygame as pg
import random as r
import tkinter as t

pg.init()
pg.font.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (54,198,83)
blue = (30,144,255)

#ui variables
game_caption = "snake2"
screen_widgth = 1000
screen_height = 500
box_width = 990
box_height = 400
snake_size = 10
snake_x = 100
snake_y = 150
food_size = 10
food_x = r.randint(0,box_width)
food_y = r.randint(0,box_height)

gamewindow = pg.display.set_mode((screen_widgth,screen_height))
boxwindow = pg.display.set_mode((box_width,box_height))
pg.display.set_caption(game_caption)
pg.display.update()

#texts
font = pg.font.SysFont('Whimsy TT',35)
def text_screen(txt1,txt2,clr1,clr2,x1,y1,x2,y2):
    screen_txt1 = font.render(txt1,True,clr1)
    screen_txt1 = font.render(txt2,True,clr2)
    gamewindow.blit(screen_txt1,[x1,y1])
    gamewindow.blit(screen_txt2,[x2,y2])
    pass


#snake length
snake_length = 1
snake_list = []
def snake(boxwindow,black,snake_list,snake_size):
    for x,y in snake_list:
        pg.draw.rect(boxwindow,black,[x,y,snake_list,snake_size])


#game processing variables
exitgame = False
gameover = False
score = 0
speed = 5
velocity_x = 0
velocity_y = 0
fps = 30
clock = pg.time.Clock()

#game loop
while not exitgame:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exitgame = True
        if event.type == pg.KEYDOWN:
            if



'''
class game_screen
class snake
class food
class play_screen

