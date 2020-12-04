import pygame
import os
import random
import sys
import sqlite3
import time
import miniGame_1

conn = sqlite3.connect("load.db")
cur = conn.cursor()

pygame.init()

# Global Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load('../img/jh_run1.png'), pygame.image.load('../img/jh_run2.png'),
           pygame.image.load('../img/jh_run3.png'), pygame.image.load('../img/jh_run4.png'),
           pygame.image.load('../img/jh_run5.png'), pygame.image.load('../img/jh_run6.png'),
           pygame.image.load('../img/jh_run7.png'), pygame.image.load('../img/jh_run8.png')]
JUMPING = pygame.image.load('../img/jh_run7.png')
SLIDE = [pygame.image.load('../img/jh_slide.png')]

SMALL_BOX = [pygame.image.load('../img/box.png')]
LARGE_BOX = [pygame.image.load('../img/bigBox.png')]
PRESENT = [pygame.image.load('../img/gift.png')]
SNOWMAN = [pygame.image.load('../img/snowman.png')]
WINE = [pygame.image.load('../img/Wine.png')]
CART = [pygame.image.load('../img/Cart.png')]
HAT = [pygame.image.load('../img/Hat.png')]
WATERMELON = [pygame.image.load('../img/Watermelon.png')]

UMBRELLA = [pygame.image.load('../img/umbrella.png')]
SANTA = [pygame.image.load('../img/Santa.png')]
EYE = [pygame.image.load('../img/Eye.png')]
PIECE = [pygame.image.load('../img/WatermelonPiece.png')]

GROUND1_1 = pygame.image.load('../img/stage1_1_ground.png')
GROUND1_2 = pygame.image.load('../img/stage1_2_ground.png')
GROUND1_3 = pygame.image.load('../img/stage1_3_ground.png')
GROUND1_4 = pygame.image.load('../img/stage1_4_ground.png')

ringImg = pygame.image.load('../img/ring.png')

BG1_1 = pygame.image.load('../img/stage1_1_bg.png')
BG1_2 = pygame.image.load('../img/stage1_2_bg.png')
BG1_3 = pygame.image.load('../img/stage1_3_bg.png')
BG1_4 = pygame.image.load('../img/stage1_4_bg.png')

INFO1_1 = pygame.image.load('../img/stage1-1.png')
INFO1_1.convert()
INFO1_2 = pygame.image.load('../img/stage1-2.png')
INFO1_2.convert()
INFO1_3 = pygame.image.load('../img/stage1-3.png')
INFO1_3.convert()
INFO1_4 = pygame.image.load('../img/stage1-4.png')
INFO1_4.convert()

STAGE1 = pygame.image.load('../img/stage1.png')
STAGE1.convert()

LOGO1_1 = pygame.image.load('../img/stage1_1_logo.png')
LOGO1_2 = pygame.image.load('../img/stage1_2_logo.png')
LOGO1_3 = pygame.image.load('../img/stage1_3_logo.png')
LOGO1_4 = pygame.image.load('../img/stage1_4_logo.png')

STATUS1_1 = pygame.image.load('../img/Status1_1.png')
STATUS1_2 = pygame.image.load('../img/Status1_2.png')

class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            SCREEN.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            SCREEN.blit(img_in, (x, y))

class Jh:
    X_POS = 80
    Y_POS = 500
    Y_POS_SLIDE = 600
    JUMP_VEL = 8.5

    def __init__(self):
        self.slide_img = SLIDE
        self.run_img = RUNNING
        self.jump_img = JUMPING

        self.jh_slide = False
        self.jh_run = True
        self.jh_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.jh_rect = self.image.get_rect()
        self.jh_rect.x = self.X_POS
        self.jh_rect.y = self.Y_POS

    def update(self, userInput):
        if self.jh_slide:
            self.slide()
        if self.jh_run:
            self.run()
        if self.jh_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.jh_jump:
            self.jh_slide = False
            self.jh_run = False
            self.jh_jump = True
        elif userInput[pygame.K_DOWN] and not self.jh_jump:
            self.jh_slide = True
            self.jh_run = False
            self.jh_jump = False
        elif not (self.jh_jump or userInput[pygame.K_DOWN]):
            self.jh_slide = False
            self.jh_run = True
            self.jh_jump = False

    def slide(self):
        self.image = self.slide_img[0]
        self.jh_rect = self.image.get_rect()
        self.jh_rect.x = self.X_POS
        self.jh_rect.y = self.Y_POS_SLIDE
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 2]
        self.jh_rect = self.image.get_rect()
        self.jh_rect.x = self.X_POS
        self.jh_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.jh_jump:
            self.jh_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.jh_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.jh_rect.x, self.jh_rect.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class SmallBox(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 565


class LargeBox(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 520


class Umbrella(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[0], self.rect)
        self.index += 1

def saver1_1():
    cur.execute('UPDATE load set BigStage = 1, SmallStage = 1')
    conn.commit()

def saver1_2():
    cur.execute('UPDATE load set BigStage = 1, SmallStage = 2')
    conn.commit()

def saver1_3():
    cur.execute('UPDATE load set BigStage = 1, SmallStage = 3')
    conn.commit()

def saver1_4():
    cur.execute('UPDATE load set BigStage = 1, SmallStage = 4')
    conn.commit()

def main1_1():
    global game_speed, x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Jh()
    game_speed = 20
    x_pos_ground = 0
    y_pos_ground = 380
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        #SCREEN.blit(text, textRect)

        if points == 100:
            play1_2(death_count=0)

    def background():
        global x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg
        y_pos_ground = 645
        y_pos_bg = 0
        image_width = GROUND1_1.get_width()
        SCREEN.blit(BG1_1, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG1_1, (image_width + x_pos_bg, y_pos_bg))
        SCREEN.blit(GROUND1_1, (x_pos_ground, y_pos_ground))
        SCREEN.blit(GROUND1_1, (image_width + x_pos_ground, y_pos_ground))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG1_1, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        if x_pos_ground <= -image_width:
            SCREEN.blit(GROUND1_1, (image_width + x_pos_ground, y_pos_ground))
            x_pos_ground = 0
        x_pos_ground -= game_speed
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
        background()
        SCREEN.blit(LOGO1_1, (600, 20))
        SCREEN.blit(STATUS1_1, (20, 20))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallBox(SMALL_BOX))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeBox(LARGE_BOX))
            elif random.randint(0, 2) == 2:
                obstacles.append(Umbrella(UMBRELLA))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.jh_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                play1_1(death_count)

        player.draw(SCREEN)
        userInput = pygame.key.get_pressed()
        player.update(userInput)
        score()
        pygame.display.update()
        clock.tick(50)


def play1_1(death_count):
    global points
    i = 1
    run = True
    alphaBoo = True
    while run:
        SCREEN.blit(BG1_1, (0, 0))
        SCREEN.blit(GROUND1_1, (0, 640))
        font = pygame.font.Font('NotoSansCJKkr-Black.otf', 30)
        font2 = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)

        if alphaBoo:
            STAGE1.set_alpha(i)
            SCREEN.blit(STAGE1, (0, 0))
            pygame.time.delay(20)
            i += 20
            if i == 501:
                i = 0
                alphaBoo = False

        if death_count == 0:
            if alphaBoo == False:
                INFO1_1.set_alpha(i)
                SCREEN.blit(INFO1_1, (0, 0))
                pygame.time.delay(20)
                i += 20
                if i == 255:
                    i = 1
        elif death_count > 0:
            text = font.render("다시 시작하려면 아무 키나 누르세요", True, (0, 0, 0))
            text2 = font.render("(반지를 눌러 저장해 보세요)", True, (0, 0, 0))
            pauseBtn = Button(ringImg, 930, 10, 65, 65, ringImg, 930, 10, saver1_1)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            textRect2 = text2.get_rect()
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(RUNNING[0], (80, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                main1_1()

class Present(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 590


class Snowman(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 495


class Santa(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 470
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[0], self.rect)
        self.index += 1


def main1_2():
    global game_speed, x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Jh()
    game_speed = 20
    x_pos_ground = 0
    y_pos_ground = 380
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        # SCREEN.blit(text, textRect)

        if points == 100:
            play1_3(death_count=0)

    def background():
        global x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg
        y_pos_ground = 645
        y_pos_bg = 0
        image_width = GROUND1_2.get_width()
        SCREEN.blit(BG1_2, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG1_2, (image_width + x_pos_bg, y_pos_bg))
        SCREEN.blit(GROUND1_2, (x_pos_ground, y_pos_ground))
        SCREEN.blit(GROUND1_2, (image_width + x_pos_ground, y_pos_ground))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG1_2, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        if x_pos_ground <= -image_width:
            SCREEN.blit(GROUND1_2, (image_width + x_pos_ground, y_pos_ground))
            x_pos_ground = 0
        x_pos_ground -= game_speed
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
        background()
        SCREEN.blit(LOGO1_2, (600, 20))
        SCREEN.blit(STATUS1_2, (20, 20))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Present(PRESENT))
            elif random.randint(0, 2) == 1:
                obstacles.append(Snowman(SNOWMAN))
            elif random.randint(0, 2) == 2:
                obstacles.append(Santa(SANTA))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.jh_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                play1_2(death_count)

        player.draw(SCREEN)
        userInput = pygame.key.get_pressed()
        player.update(userInput)
        score()
        pygame.display.update()
        clock.tick(50)


def play1_2(death_count):
    global points
    i = 1
    run = True
    while run:
        SCREEN.blit(BG1_2, (0, 0))
        SCREEN.blit(GROUND1_2, (0, 640))
        font = pygame.font.Font('NotoSansCJKkr-Black.otf', 30)
        font2 = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)

        if death_count == 0:
            INFO1_2.set_alpha(i)
            SCREEN.blit(INFO1_2, (0, 0))
            pygame.time.delay(20)
            i += 20
            if i == 255:
                i = 1
        elif death_count > 0:
            text = font.render("다시 시작하려면 아무 키나 누르세요", True, (0, 0, 0))
            text2 = font.render("(반지를 눌러 저장해 보세요)", True, (0, 0, 0))
            pauseBtn = Button(ringImg, 930, 10, 65, 65, ringImg, 930, 10, saver1_1)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            textRect2 = text2.get_rect()
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(RUNNING[0], (80, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                main1_2()

class Wine(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 575


class Cart(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 530


class Eye(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 500
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[0], self.rect)
        self.index += 1


def main1_3():
    global game_speed, x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Jh()
    game_speed = 20
    x_pos_ground = 0
    y_pos_ground = 380
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        # SCREEN.blit(text, textRect)

        if points == 100:
            play1_4(death_count=0)

    def background():
        global x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg
        y_pos_ground = 645
        y_pos_bg = 0
        image_width = GROUND1_3.get_width()
        SCREEN.blit(BG1_3, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG1_3, (image_width + x_pos_bg, y_pos_bg))
        SCREEN.blit(GROUND1_3, (x_pos_ground, y_pos_ground))
        SCREEN.blit(GROUND1_3, (image_width + x_pos_ground, y_pos_ground))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG1_3, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        if x_pos_ground <= -image_width:
            SCREEN.blit(GROUND1_3, (image_width + x_pos_ground, y_pos_ground))
            x_pos_ground = 0
        x_pos_ground -= game_speed
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
        background()
        SCREEN.blit(LOGO1_3, (600, 20))
        SCREEN.blit(STATUS1_1, (20, 20))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Wine(WINE))
            elif random.randint(0, 2) == 1:
                obstacles.append(Cart(CART))
            elif random.randint(0, 2) == 2:
                obstacles.append(Eye(EYE))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.jh_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                play1_3(death_count)

        player.draw(SCREEN)
        userInput = pygame.key.get_pressed()
        player.update(userInput)
        score()
        pygame.display.update()
        clock.tick(50)


def play1_3(death_count):
    global points
    i = 1
    run = True
    while run:
        SCREEN.blit(BG1_3, (0, 0))
        SCREEN.blit(GROUND1_3, (0, 640))
        font = pygame.font.Font('NotoSansCJKkr-Black.otf', 30)
        font2 = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)

        if death_count == 0:
            INFO1_3.set_alpha(i)
            SCREEN.blit(INFO1_3, (0, 0))
            pygame.time.delay(20)
            i += 20
            if i == 255:
                i = 1
        elif death_count > 0:
            text = font.render("다시 시작하려면 아무 키나 누르세요", True, (0, 0, 0))
            text2 = font.render("(반지를 눌러 저장해 보세요)", True, (0, 0, 0))
            pauseBtn = Button(ringImg, 930, 10, 65, 65, ringImg, 930, 10, saver1_1)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            textRect2 = text2.get_rect()
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(RUNNING[0], (80, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                main1_3()

class Hat(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 575


class Watermelon(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 530


class Piece(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 420
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[0], self.rect)
        self.index += 1


def main1_4():
    global game_speed, x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Jh()
    game_speed = 20
    x_pos_ground = 0
    y_pos_ground = 380
    x_pos_bg = 0
    y_pos_bg = 0
    points = 0
    font = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)
    obstacles = []
    death_count = 0

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (900, 40)
        # SCREEN.blit(text, textRect)
        if points == 100:
            miniGame()

    def background():
        global x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg
        y_pos_ground = 645
        y_pos_bg = 0
        image_width = GROUND1_4.get_width()
        SCREEN.blit(BG1_4, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG1_4, (image_width + x_pos_bg, y_pos_bg))
        SCREEN.blit(GROUND1_4, (x_pos_ground, y_pos_ground))
        SCREEN.blit(GROUND1_4, (image_width + x_pos_ground, y_pos_ground))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG1_4, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        if x_pos_ground <= -image_width:
            SCREEN.blit(GROUND1_4, (image_width + x_pos_ground, y_pos_ground))
            x_pos_ground = 0
        x_pos_ground -= game_speed
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
        background()
        SCREEN.blit(LOGO1_4, (600, 20))
        SCREEN.blit(STATUS1_2, (20, 20))

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(Hat(HAT))
            elif random.randint(0, 2) == 1:
                obstacles.append(Watermelon(WATERMELON))
            elif random.randint(0, 2) == 2:
                obstacles.append(Piece(PIECE))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.jh_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                death_count += 1
                play1_4(death_count)

        player.draw(SCREEN)
        userInput = pygame.key.get_pressed()
        player.update(userInput)
        score()
        pygame.display.update()
        clock.tick(50)


def play1_4(death_count):
    global points
    i = 1
    run = True
    while run:
        SCREEN.blit(BG1_4, (0, 0))
        SCREEN.blit(GROUND1_4, (0, 640))
        font = pygame.font.Font('NotoSansCJKkr-Black.otf', 30)
        font2 = pygame.font.Font('NotoSansCJKkr-Black.otf', 20)

        if death_count == 0:
            INFO1_4.set_alpha(i)
            SCREEN.blit(INFO1_4, (0, 0))
            pygame.time.delay(20)
            i += 20
            if i == 255:
                i = 1
        elif death_count > 0:
            text = font.render("다시 시작하려면 아무 키나 누르세요", True, (0, 0, 0))
            text2 = font.render("(반지를 눌러 저장해 보세요)", True, (0, 0, 0))
            pauseBtn = Button(ringImg, 930, 10, 65, 65, ringImg, 930, 10, saver1_1)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            textRect2 = text2.get_rect()
            textRect2.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(text, textRect)
            SCREEN.blit(text2, textRect2)
            SCREEN.blit(RUNNING[0], (80, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                main1_4()

def miniGame():
    miniGame_1.play()

# play1_1(death_count=0)