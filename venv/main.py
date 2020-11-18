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
    # 배경 이미지 불러오기
    background_image = pygame.image.load('../img/TutorialBg.png')

    # 캐릭터 불러오기
    character_jh = pygame.image.load('../img/jh_ill.png')
    character_wife = pygame.image.load('../img/wife_ill.png')

    character_jh_small = pygame.transform.scale(character_jh, (250, 332))
    character_wife_small = pygame.transform.scale(character_wife, (250, 332))
    character_jh_big = pygame.transform.scale(character_jh, (250, 332))
    character_wife_big = pygame.transform.scale(character_wife, (320, 424))

    font1 = pygame.font.SysFont('malgungothic', 30)
    text1 = font1.render("와이프", True, (255, 255, 255))

    font2 = pygame.font.SysFont('malgungothic', 20)
    text2 = font2.render("수박 화채, 수박 주스, 수박바.... 다 먹고 싶은데 어떡하지?", True, (255, 255, 255))

    nextImg = pygame.image.load("../img/next.png")
    nextImg_over = pygame.image.load("../img/next_over.png")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

            screen.blit(background_image, (0, 0))
            event = pygame.event.poll()

            pygame.draw.rect(screen, (128, 128, 128), (0, 570, 1000, 180))
            screen.blit(character_jh_small, (750, 238))
            screen.blit(character_wife_big, (0, 326))
            screen.blit(text1, (320, 590))
            screen.blit(text2, (320, 640))
            nextBtn = Button(nextImg, 550, 700, 16, 16, nextImg_over, 550, 700, None)
            pygame.display.update()
    #start.main()

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