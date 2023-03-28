import pygame

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT,)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,225,0)
YELLOW = (255,255,0)
VIOLET = (255,0,255)
CYAN = (0,255,255)

COLORS = [RED,GREEN,BLUE,YELLOW,VIOLET,CYAN]

class Square(pygame.sprite.Sprite):
    def __init__(self,color):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.surf = pygame.Surface((100, 100))
        self.surf.fill((color))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            pass
        if pressed_keys[K_DOWN]:
            pass
        if pressed_keys[K_LEFT]:
            pass
        if pressed_keys[K_RIGHT]:
            pass

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

S1 = Square(RED)
S2 = Square(BLUE)
S3 = Square(GREEN)
S4 = Square(YELLOW)




running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.display.quit()
                pygame.quit()
        elif event.type == QUIT:
            running = False
            pygame.display.quit()
            pygame.quit()

    pressed_keys = pygame.key.get_pressed()

    S1.update(pressed_keys)
    
    
    screen.fill((0,0,0))
    
    #center = ((SCREEN_WIDTH-S1.surf.get_width())/2,(SCREEN_HEIGHT-S1.surf.get_height())/2)

    screen.blit(S1.surf, ((300,SCREEN_HEIGHT/2)))
    screen.blit(S2.surf, (SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
    screen.blit(S3.surf, (300,200))
    screen.blit(S4.surf, (400,200))
    pygame.draw.circle(screen, (0,0,0),(350,250),10)
    pygame.display.flip()

