import pygame
from pygame.locals import *
import sys
import time
import math

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 1)


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position):
        super(AnimatedSprite, self).__init__()
        size = (90, 210)
        images = []
        images.append(pygame.image.load('../img/jh_run1.png'))
        images.append(pygame.image.load('../img/jh_run2.png'))
        images.append(pygame.image.load('../img/jh_run3.png'))
        images.append(pygame.image.load('../img/jh_run4.png'))
        images.append(pygame.image.load('../img/jh_run5.png'))
        images.append(pygame.image.load('../img/jh_run6.png'))
        images.append(pygame.image.load('../img/jh_run7.png'))
        images.append(pygame.image.load('../img/jh_run8.png'))

        self.rect = pygame.Rect(position, size)
        self.images = [pygame.transform.scale(image, size) for image in images]
        self.index = 0
        self.image = images[self.index]
        self.position = 200, 530
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.running = 2
        self.jumpingV = 20
        self.jumping = False
        self.slideCheck = False
        self.animation_time = round(100 / len(self.images * 300), 2)
        self.current_time = 0

    def afterSlide(self):
        self.image = pygame.image.load('../img/jh_slide.png')
        self.image = pygame.transform.scale(self.image, (90, 210))
        self.position = 200, 530
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def playing(self):
        if not self.jumping and not self.slideCheck:
            # print('playing')
            self.position = self.position[0], self.position[1] - self.running
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            if self.position[1] == 520 or self.position[1] == 540:
                self.running = -self.running
            # print(self.running)

    def jump(self):
        if self.jumping:
            self.position = self.position[0], self.position[1] - self.jumpingV
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            if 280 <= self.position[1] <= 300:
                self.jumpingV = - self.jumpingV
            if self.position[1] >= 530:
                self.position = self.position[0], 530
                self.jumpingV = 20
                self.jumping = False

    def slide(self):
        if self.slideCheck:
            self.image = pygame.image.load('../img/jh_slide.png')
            self.image = pygame.transform.scale(self.image, (205, 90))  #135 60 #60 140     #90 210
            self.position = self.position[0], 600
            self.rect = self.image.get_rect()
            self.rect.center = self.position

    def update(self, mt):
        self.current_time += mt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
        self.jump()
        self.playing()
        self.slide()

class Background(pygame.sprite.Sprite):
    def __init__(self, number, *args):
        self.image = pygame.image.load('../img/stage1_bg.png').convert()
        self.rect = self.image.get_rect()
        self._layer = -10
        pygame.sprite.Sprite.__init__(self, *args)
        self.moved = 0
        self.number = number
        self.rect.x = self.rect.width * self.number

    def update(self):
        self.rect.move_ip(-3, 0)
        self.moved += 3

        if self.moved >= self.rect.width:
            self.rect.x = self.rect.width * self.number
            self.moved = 0

player = AnimatedSprite(position=(200, 530))
all_sprites = pygame.sprite.Group(player)
obstacles_bottom = []
obstacles_top = []

def play():
    group = pygame.sprite.LayeredUpdates()
    Background(0, group)
    Background(1, group)

    while True:
        mt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if hasattr(event, 'key'):
                down = event.type == KEYDOWN
                up = event.type == KEYUP
                if event.key == K_UP:
                    player.jumping = True
                if down and event.key == K_DOWN:
                    player.slideCheck = True
                if up and event.key == K_DOWN:
                    player.slideCheck = False
                    player.afterSlide()

        screen.fill((0, 0, 0))
        group.update()
        group.draw(screen)

        all_sprites.update(mt)
        all_sprites.draw(screen)
        pygame.display.update()

        clock.tick(80)

play()