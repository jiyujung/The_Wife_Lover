import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bgImg = pygame.image.load('../img/miniGame1Bg.png')
barImg = pygame.image.load('../img/barImage.png')

class ArrowSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('../img/arrow.png')
        self.position = position
        self.x = 141
        self.y = 300
        self.direction = 0
        self.moving = True
        self.pressedSpace = False

    def spaceAction(self):
        if self.pressedSpace:
            if 141 < self.x < 270:
                self.moving = False
            elif 270 <= self.x < 380:
                self.moving = False
            elif 380 <= self.x < 480:
                self.moving = False
            elif 480 <= self.x < 525:
                self.moving = False
            elif 525 <= self.x < 620:
                self.moving = False
            elif 620 <= self.x < 735:
                self.moving = False
            elif 735 <= self.x < 821:
                self.moving = False

    def update(self):
        self.spaceAction()
        if self.x < 810 and self.direction == 0 and self.moving:
            self.x += 20
        elif self.x == 821:
            self.direction = 1

        if self.x > 141 and self.direction == 1 and self.moving:
            self.x -= 20
        elif self.x == 141:
            self.direction = 0

        self.position = (self.x, self.y)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

arrow = ArrowSprite((141, 300))
arrow_group = pygame.sprite.RenderPlain(arrow)
score = 0

def play():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    arrow.pressedSpace = True

        event = pygame.event.poll()
        screen.blit(bgImg, (0, 0))
        screen.blit(barImg, (160, 350))

        arrow_group.update()
        arrow_group.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

play()
