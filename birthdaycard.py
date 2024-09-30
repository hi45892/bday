import pygame, sys
from pygame.locals import QUIT
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("birthday card")

pic1 = pygame.image.load("animation images/picture1.jpg")
pic1= pygame.transform.scale(pic1,(800,600))


pic2= pygame.image.load("animation images/picture2.jpg")
pic2= pygame.transform.scale(pic2,(800,600))

pic3= pygame.image.load("animation images/picture3.jpg")
pic3= pygame.transform.scale(pic3,(800,600))

f = pygame.font.SysFont("times new roman",28)
write =f.render("Happy Birthday!",True,"black")
write2 = f.render("have a lovely life",True,"black")
write3 = f.render("wish you all the best",True,"black")


while True:
    screen.blit(pic1,(0,0))
    screen.blit(write,(10,50))
    time.sleep(1)
    pygame.display.update()
    screen.blit(pic2,(0,0))
    screen.blit(write2,(300,300))
    time.sleep(1)
    pygame.display.update()
    time.sleep(1)
    screen.blit(pic3,(0,0))
    screen.blit(write3,(10,50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()





