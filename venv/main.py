import pygame
import sys
import time
import start
import load

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

def start():
    start.main()

def load():
    load.main()

pygame.display.set_caption("The Wife Lover")
startImg = pygame.image.load('../img/start.gif')
loadImg = pygame.image.load('../img/load.gif')
startImg_over = pygame.image.load('../img/start_over.gif')
loadImg_over = pygame.image.load('../img/load_over.gif')
background_image = pygame.image.load('../img/mainBg.gif')

def mainmenu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

            screen.blit(background_image, (0, 0))
            event = pygame.event.poll()

            startBtn = Button(startImg, 415, 410, 195, 35, startImg_over, 415, 410, start)
            loadBtn = Button(loadImg, 415, 460, 195, 35, loadImg_over, 415, 460, load)
            pygame.display.update()
            clock.tick(15)

mainmenu()
game_loop()
pygame.quit()