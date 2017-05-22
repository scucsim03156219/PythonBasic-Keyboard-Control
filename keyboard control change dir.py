'''
如何設計使用上下左右鍵來移動物件，按鍵會移動方向
by Ching-Shoei Chiang
'''
import random, pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
screen = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('object moving')
WHITE = (255, 255, 255)

circleImg = pygame.image.load('circle64.png')
circlex = circley = 400
dirx = diry = 1
step = 10
updown = True

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
            elif event.key==K_UP:
                diry = -1
                updown = True                
            elif event.key==K_DOWN:
                diry = +1
                updown = True
            elif event.key==K_LEFT:
                dirx = -1
                updown = False
            elif event.key==K_RIGHT:
                dirx = 1
                updown = False
    if updown:
        circley = circley + diry*step
    else:
        circlex = circlex + dirx*step
    screen.blit(circleImg, (circlex, circley))
    
    screen.fill(WHITE)
    screen.blit(circleImg, (circlex, circley))         
    pygame.display.update()

    fpsClock.tick(FPS)
