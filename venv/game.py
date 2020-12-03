import pygame
import os
import random
import sys

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

UMBRELLA = [pygame.image.load('../img/umbrella.png')]

GROUND = pygame.image.load('../img/ground.png')
BG = pygame.image.load('../img/stage1_bg.png')
LOGO = pygame.image.load('../img/stage1_logo.png')

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


def main():
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

    def background():
        global x_pos_ground, y_pos_ground, x_pos_bg, y_pos_bg
        y_pos_ground = 645
        y_pos_bg = 0
        image_width = GROUND.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        SCREEN.blit(GROUND, (x_pos_ground, y_pos_ground))
        SCREEN.blit(GROUND, (image_width + x_pos_ground, y_pos_ground))
        if x_pos_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        if x_pos_ground <= -image_width:
            SCREEN.blit(GROUND, (image_width + x_pos_ground, y_pos_ground))
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
        SCREEN.blit(LOGO, (600, 30))

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
                pygame.time.delay(2000)
                death_count += 1
                play(death_count)

        player.draw(SCREEN)
        userInput = pygame.key.get_pressed()
        player.update(userInput)
        score()
        pygame.display.update()
        clock.tick(50)


def play(death_count):
    global points
    run = True
    while run:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(GROUND, (0, 640))
        font = pygame.font.Font('NotoSansCJKkr-Black.otf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(RUNNING[0], (80, 500))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                main()


# menu(death_count=0)