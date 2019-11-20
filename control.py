import numpy as np
import pygame as pg
import pygbutton as pygb

pg.init()

display_width = 800
display_height = 600

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('FIRE EMBEL 84')

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
LIME  = (  0,255,  0)
BLUE  = (  0,  0,255)
NORMAL    = (  0,128,255)
CLICK     = ( 51,153,255)
HIGHLIGHT = (  0, 76,153)

clock = pg.time.Clock()
crashed = False
menuImg = pg.image.load('menu.png')

square = pg.Rect(0, 0, 30, 60)


def menu():
    gameDisplay.blit(menuImg)


while not crashed:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
        print(event)
    pg.display.update()
    clock.tick(60)

pg.quit()
quit()
