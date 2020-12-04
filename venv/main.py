import pygame
import sys
import time
import start
import sqlite3
import game

conn = sqlite3.connect("load.db")
cur = conn.cursor()

pygame.init()

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in, (x, y))

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def starter():
    cur.execute('UPDATE load set BigStage = 0, SmallStage = 0')
    conn.commit()
    conn.close()
    start.main()

def loader():
    row = cur.execute('SELECT * from load').fetchone()
    bigStage = row[0]
    smallStage = row[1]
    conn.close()
    loader_2(bigStage, smallStage)

def loader_2(b, s):
    if b == 0 and s == 0:
        start.main()
    elif b == 1 and s == 1:
        game.play1_1(0)
    elif b == 1 and s == 2:
        game.play1_2(0)
    elif b == 1 and s == 3:
        game.play1_3(0)
    elif b == 1 and s == 4:
        game.play1_4(0)
    elif b == 2 and s == 1:
        game2.play2_1(0)
    elif b == 2 and s == 2:
        game2.play2_2(0)
    elif b == 2 and s == 3:
        game2.play2_3(0)
    elif b == 2 and s == 4:
        game2.play2_4(0)
    else:
        print("DB error")

pygame.display.set_caption("The Wife Lover")
startImg = pygame.image.load('../img/start.gif')
loadImg = pygame.image.load('../img/load.gif')
startImg_over = pygame.image.load('../img/start_over.gif')
loadImg_over = pygame.image.load('../img/load_over.gif')
background_image = pygame.image.load('../img/mainBg.png')
programIcon = pygame.image.load('../img/icon.png')

def mainmenu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

            screen.blit(background_image, (0, 0))
            event = pygame.event.poll()
            pygame.display.set_icon(programIcon)

            startBtn = Button(startImg, 415, 410, 195, 35, startImg_over, 415, 410, starter)
            loadBtn = Button(loadImg, 415, 460, 195, 35, loadImg_over, 415, 460, loader)
            pygame.display.update()
            clock.tick(15)

mainmenu()
pygame.quit()