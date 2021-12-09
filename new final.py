import pygame, sys, random, time
pygame.init()
display_w = 1400
display_h = 800
dark_red = 180, 0, 0
light_red = 230, 0, 0
black = 0, 0, 0
yellow = 255,140,0
gold = 211, 175, 55
orange = 255,165,0
white = 255, 255, 255
width = 62
height = 80

screen = pygame.display.set_mode((display_w, display_h))
#pictures
bassDrum = pygame.image.load("bassDrum.png")

gameState = 'game'

def musicRooms():
    x = 220
    y = 230
    bassR1 = [1,2,3,4]
    mousePos = pygame.mouse.get_pos()
    if gameState == 'game':
        screen.fill(white)
        tempoBar_1 = pygame.draw.rect(screen, black, pygame.Rect(222,150, 62,25))
        tempoBar_2 = pygame.draw.rect(screen, black, pygame.Rect(288,150, 62,25))
        tempoBar_3 = pygame.draw.rect(screen, black, pygame.Rect(354,150, 62,25))
        tempoBar_4 = pygame.draw.rect(screen, black, pygame.Rect(420,150, 62,25))
        tempoBar_5 = pygame.draw.rect(screen, black, pygame.Rect(496,150, 62,25))
        tempoBar_6 = pygame.draw.rect(screen, black, pygame.Rect(562,150, 62,25))
        tempoBar_7 = pygame.draw.rect(screen, black, pygame.Rect(628,150, 62,25))
        tempoBar_8 = pygame.draw.rect(screen, black, pygame.Rect(694,150, 62,25))
        tempoBar_9 = pygame.draw.rect(screen, black, pygame.Rect(770,150, 62,25))
        tempoBar_10 = pygame.draw.rect(screen, black, pygame.Rect(836,150, 62,25))
        tempoBar_11 = pygame.draw.rect(screen, black, pygame.Rect(902,150, 62,25))
        tempoBar_12 = pygame.draw.rect(screen, black, pygame.Rect(968,150, 62,25))
        tempoBar_13 = pygame.draw.rect(screen, black, pygame.Rect(1044,150, 62,25))
        tempoBar_14 = pygame.draw.rect(screen, black, pygame.Rect(1110,150, 62,25))
        tempoBar_15 = pygame.draw.rect(screen, black, pygame.Rect(1176,150, 62,25))
        tempoBar_16 = pygame.draw.rect(screen, black, pygame.Rect(1242,150, 62,25))
        bassBar = pygame.draw.rect(screen, light_red, pygame.Rect(30,230, 170,80))
        #bassBar1 = pygame.rect((30,230, 170,80))
        #bassR1B1 = pygame.draw.rect(screen, black, pygame.Rect(220,230, width,height))
        bass4 = [(x,y,width,height),(x+66,y,width,height),(x+132,y,width,height),(x+198,y,width,height)]


        snareBar = pygame.draw.rect(screen, black, pygame.Rect(30,330, 170,80))
        highHatBar = pygame.draw.rect(screen, black, pygame.Rect(30,430, 170,80))
        openHighBar = pygame.draw.rect(screen, black, pygame.Rect(30,530, 170,80))
        tombBar = pygame.draw.rect(screen, black, pygame.Rect(30,630, 170,80))
        screen.blit(bassDrum, (90,250))

        for i in range(4):
            pygame.draw.rect(screen,black,bass4[i])

        if pygame.Rect.collidepoint(bass4, mousePos):
            print('hi')




        pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    print(pygame.mouse.get_pos())
    musicRooms()
    pygame.display.flip()

pygame.quit()
quit()

