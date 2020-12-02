import pygame
import sys
import time
import game

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)

# 배경 이미지 불러오기
background_image = pygame.image.load('../img/TutorialBg.png')

# 캐릭터 불러오기
character_jh = pygame.image.load('../img/jh_ill.png')
character_wife = pygame.image.load('../img/wife_ill.png')
character_jh_small = pygame.transform.scale(character_jh, (250, 332))
character_wife_small = pygame.transform.scale(character_wife, (250, 332))
character_jh_big = pygame.transform.scale(character_jh, (320, 424))
character_wife_big = pygame.transform.scale(character_wife, (320, 424))

# 글씨체 및 글씨 크기
font1 = pygame.font.Font('NotoSansCJKkr-Black.otf', 30)
font2 = pygame.font.Font('NotoSansCJKkr-Medium.otf', 20)

# next 이미지
nextImg = pygame.image.load("../img/next.png")
nextImg_over = pygame.image.load("../img/next_over.png")

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in, (x, y))

def main():
    text1 = font1.render("와이프", True, (255, 255, 255))
    text2 = font2.render("수박 화채, 수박 주스, 수박바.... 다 먹고 싶은데 어떡하지?", True, (255, 255, 255))

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
            # backBtn = Button(nextImg, 10, 10, 16, 16, nextImg_over, 10, 10, back)
            nextBtn = Button(nextImg, 550, 700, 16, 16, nextImg_over, 550, 700, next1)
            pygame.display.update()

def next1():
    text3 = font1.render("정훈쌤", True, (255, 255, 255))
    text4 = font2.render("이 겨울에 수박이 먹고 싶다고...??", True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            screen.blit(background_image, (0, 0))
            event = pygame.event.poll()
            pygame.draw.rect(screen, (128, 128, 128), (0, 570, 1000, 180))
            screen.blit(character_jh_big, (680, 326))
            screen.blit(character_wife_small, (0, 238))
            screen.blit(text3, (320, 590))
            screen.blit(text4, (320, 640))
            nextBtn = Button(nextImg, 550, 700, 16, 16, nextImg_over, 550, 700, next2)
            pygame.display.update()

def next2():
    text5 = font1.render("와이프", True, (255, 255, 255))
    text6 = font2.render("어... 너무 먹고 싶어", True, (255, 255, 255))

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
            screen.blit(text5, (320, 590))
            screen.blit(text6, (320, 640))
            nextBtn = Button(nextImg, 550, 700, 16, 16, nextImg_over, 550, 700, next3)
            pygame.display.update()
            event = pygame.event.poll()

def next3():
    text7 = font1.render("정훈쌤", True, (255, 255, 255))
    text8 = font2.render("기다려", True, (255, 255, 255))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            screen.blit(background_image, (0, 0))
            event = pygame.event.poll()
            pygame.draw.rect(screen, (128, 128, 128), (0, 570, 1000, 180))
            screen.blit(character_jh_big, (680, 326))
            screen.blit(character_wife_small, (0, 238))
            screen.blit(text7, (320, 590))
            screen.blit(text8, (320, 640))
            nextBtn = Button(nextImg, 550, 700, 16, 16, nextImg_over, 550, 700, gamer)
            pygame.display.update()
            event = pygame.event.poll()

def gamer():
    game.play()