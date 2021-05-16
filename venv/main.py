# pygame : python을 통해 게임을 만들 수 있도록 지원해주는 모듈
import pygame
import sys
import time
import start
import sqlite3
import game
import game2

conn = sqlite3.connect("load.db")
cur = conn.cursor()

pygame.init()

# 이미지 버튼을 만드는 Button 클래스
class Button:
    # 매개변수로 처음 이미지와 클릭후 이미지, 크기, x좌표, y좌표, 클릭시 호출함수
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        # 마우스가 이미지 위로 올라갔을 때 이미지를 변화시키는 코드
        mouse = pygame.mouse.get_pos()      # 마우스 좌표 저장 / get_pos() 함수는 마우스 위치를 반환
        click = pygame.mouse.get_pressed()  # 클릭시
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # 이미지 안에 있으면
            screen.blit(img_act, (x_act, y_act))    # 클릭 이미지 로드
            if click[0] and action != None:
                time.sleep(1)   # 1초 동안 지연
                action()        # 지정 함수 호출
        else:
            screen.blit(img_in, (x, y))     # 마우스가 이미지 바깥이면 일반 이미지 로드

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# 화면을 초당 몇 번 출력하는가를 설정하기 위해 선언되는 변수
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
    while True:     # 게임 루프
        for event in pygame.event.get():    # 닫기 버튼 설정
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

            screen.blit(background_image, (0, 0))   # 이미지 로딩
            # event = pygame.event.poll()
            pygame.display.set_icon(programIcon)

            startBtn = Button(startImg, 415, 410, 195, 35, startImg_over, 415, 410, starter)
            loadBtn = Button(loadImg, 415, 460, 195, 35, loadImg_over, 415, 460, loader)
            pygame.display.update()
            # 일정 주기로 화면을 갱신
            clock.tick(15)

mainmenu()
pygame.quit()