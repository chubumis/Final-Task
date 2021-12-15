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
purple = 159, 43, 104
white = 255, 255, 255
purple1 = 159, 43, 104
purple2 = 159, 43, 104
purple3 = 159, 43, 104
purple4 = 159, 43, 104
purpleL = [(159, 43, 104),(159, 43, 104),(159, 43, 104),(159, 43, 104)]
purpleL1 = [(159, 43, 104),(159, 43, 104),(159, 43, 104),(159, 43, 104)]
purpleL2 = [(159, 43, 104),(159, 43, 104),(159, 43, 104),(159, 43, 104)]
tempPurp = [(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80),(255,127,80)]

magenta = 255,0,255
width = 62
height = 80
timer = 0




screen = pygame.display.set_mode((display_w, display_h))
#pictures
bassDrum = pygame.image.load("bassDrum.png")

gameState = 'game'




def musicRooms():
    global timer
    timer += 1
    print(timer)
    global tempPurp
    global purple
    global purple1
    global purple2
    global purple3
    global purple4
    global clicked
    global i
    global mouse_pos




    x = 220
    y = 230
    bassR1 = [1,2,3,4]
    mousePos = pygame.mouse.get_pos()
    if gameState == 'game':
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(black)
        tempoBar_1 = pygame.draw.rect(screen, tempPurp[0], pygame.Rect(222,150, 62,25))
        tempoBar_2 = pygame.draw.rect(screen, tempPurp[1], pygame.Rect(288,150, 62,25))
        tempoBar_3 = pygame.draw.rect(screen, tempPurp[2], pygame.Rect(354,150, 62,25))
        tempoBar_4 = pygame.draw.rect(screen, tempPurp[3], pygame.Rect(420,150, 62,25))
        tempoBar_5 = pygame.draw.rect(screen, tempPurp[4], pygame.Rect(496,150, 62,25))
        tempoBar_6 = pygame.draw.rect(screen, tempPurp[5], pygame.Rect(562,150, 62,25))
        tempoBar_7 = pygame.draw.rect(screen, tempPurp[6], pygame.Rect(628,150, 62,25))
        tempoBar_8 = pygame.draw.rect(screen, tempPurp[7], pygame.Rect(694,150, 62,25))
        tempoBar_9 = pygame.draw.rect(screen, tempPurp[8], pygame.Rect(770,150, 62,25))
        tempoBar_10 = pygame.draw.rect(screen, tempPurp[9], pygame.Rect(836,150, 62,25))
        tempoBar_11 = pygame.draw.rect(screen, tempPurp[10], pygame.Rect(902,150, 62,25))
        tempoBar_12 = pygame.draw.rect(screen, tempPurp[11], pygame.Rect(968,150, 62,25))
        tempoBar_13 = pygame.draw.rect(screen, tempPurp[12], pygame.Rect(1044,150, 62,25))
        tempoBar_14 = pygame.draw.rect(screen, tempPurp[13], pygame.Rect(1110,150, 62,25))
        tempoBar_15 = pygame.draw.rect(screen, tempPurp[14], pygame.Rect(1176,150, 62,25))
        tempoBar_16 = pygame.draw.rect(screen, tempPurp[15], pygame.Rect(1242,150, 62,25))

        if timer > 100:
            tempPurp[0] = 230, 0, 0
        if timer > 200:
            tempPurp[0] = 255,127,80
            tempPurp[1] = 230, 0, 0
        if timer > 300:
            tempPurp[1] = 255,127,80
            tempPurp[2] = 230, 0, 0
        if timer > 400:
            tempPurp[2] = 255,127,80
            tempPurp[3] = 230, 0, 0
        if timer > 500:
            tempPurp[3] = 255,127,80
            tempPurp[4] = 230, 0, 0
        if timer > 600:
            tempPurp[4] = 255,127,80
            tempPurp[5] = 230, 0, 0
        if timer > 700:
            tempPurp[5] = 255,127,80
            tempPurp[6] = 230, 0, 0
        if timer > 800:
            tempPurp[6] = 255,127,80
            tempPurp[7] = 230, 0, 0
        if timer > 900:
            tempPurp[7] = 255,127,80
            tempPurp[8] = 230, 0, 0
        if timer > 1000:
            tempPurp[8] = 255,127,80
            tempPurp[9] = 230, 0, 0
        if timer > 1100:
            tempPurp[9] = 255,127,80
            tempPurp[10] = 230, 0, 0
        if timer > 1200:
            tempPurp[10] = 255,127,80
            tempPurp[11] = 230, 0, 0
        if timer > 1300:
            tempPurp[11] = 255,127,80
            tempPurp[12] = 230, 0, 0
        if timer > 1400:
            tempPurp[12] = 255,127,80
            tempPurp[13] = 230, 0, 0
        if timer > 1500:
            tempPurp[13] = 255,127,80
            tempPurp[14] = 230, 0, 0
        if timer > 1600:
            tempPurp[14] = 255,127,80
            tempPurp[15] = 230, 0, 0
        if timer > 1700:
            tempPurp[15] = 255,127,80
            timer = 100



        bassBar = pygame.draw.rect(screen, purple, pygame.Rect(30,230, 170,80))
        bass4 = [(x,y,width,height),(x+66,y,width,height),(x+132,y,width,height),(x+198,y,width,height)]
        bass8 = [(x+274,y,width,height),(x+340,y,width,height),(x+406,y,width,height),(x+472,y,width,height)]
        bass12 = [(x+548,y,width,height),(x+614,y,width,height),(x+680,y,width,height),(x+746,y,width,height)]
        bass16 = [(x+822,y,width,height),(x+888,y,width,height),(x+954,y,width,height),(x+1020,y,width,height)]

        snareBar = pygame.draw.rect(screen, purple, pygame.Rect(30,330, 170,80))
        snare4 = [(x,y,width,height),(x+66,y,width,height),(x+132,y,width,height),(x+198,y,width,height)]
        snare8 = [(x+274,y,width,height),(x+340,y,width,height),(x+406,y,width,height),(x+472,y,width,height)]
        snare12 = [(x+548,y,width,height),(x+614,y,width,height),(x+680,y,width,height),(x+746,y,width,height)]
        snare16 = [(x+822,y,width,height),(x+888,y,width,height),(x+954,y,width,height),(x+1020,y,width,height)]

        highHatBar = pygame.draw.rect(screen, purple, pygame.Rect(30,430, 170,80))
        openHighBar = pygame.draw.rect(screen, purple, pygame.Rect(30,530, 170,80))
        tombBar = pygame.draw.rect(screen, purple, pygame.Rect(30,630, 170,80))
        screen.blit(bassDrum, (90,250))

        pygame.draw.rect(screen,purple1,bass4[0])
        pygame.draw.rect(screen,purple2,bass4[1])
        pygame.draw.rect(screen,purple3,bass4[2])
        pygame.draw.rect(screen,purple4,bass4[3])

        for i in range(4):
            pygame.draw.rect(screen,purpleL[i],bass8[i])
        for i in range(4):
            pygame.draw.rect(screen,purpleL1[i],bass12[i])
        for i in range(4):
            pygame.draw.rect(screen,purpleL2[i],bass16[i])


        #if event.type == pygame.MOUSEMOTION:
            ##
        if pygame.mouse.get_pressed()[0]:

            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(230, 310)):
                if purple1 == (159, 43, 104):
                    purple1 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(230, 310)):
                if purple1 == (0, 43, 104):
                    purple1 = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(230, 310)):
                if purple2 == (159, 43, 104):
                    purple2 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(230, 310)):
                if purple2 == (0, 43, 104):
                    purple2 = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(230, 310)):
                if purple3 == (159, 43, 104):
                    purple3 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(230, 310)):
                if purple3 == (0, 43, 104):
                    purple3 = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(230, 310)):
                if purple4 == (159, 43, 104):
                    purple4 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(230, 310)):
                if purple4 == (0, 43, 104):
                    purple4 = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[0] == (159, 43, 104):
                    purpleL[0] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[0] == (0, 43, 104):
                    purpleL[0] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[1] == (159, 43, 104):
                    purpleL[1] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[1] == (0, 43, 104):
                    purpleL[1] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[2] == (159, 43, 104):
                    purpleL[2] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[2] == (0, 43, 104):
                    purpleL[2] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[3] == (159, 43, 104):
                    purpleL[3] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[3] == (0, 43, 104):
                    purpleL[3] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[0] == (159, 43, 104):
                    purpleL1[0] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[0] == (0, 43, 104):
                    purpleL1[0] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[1] == (159, 43, 104):
                    purpleL1[1] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[1] == (0, 43, 104):
                    purpleL1[1] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[2] == (159, 43, 104):
                    purpleL1[2] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[2] == (0, 43, 104):
                    purpleL1[2] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[3] == (159, 43, 104):
                    purpleL1[3] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[3] == (0, 43, 104):
                    purpleL1[3] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[0] == (159, 43, 104):
                    purpleL2[0] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[0] == (0, 43, 104):
                    purpleL2[0] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[1] == (159, 43, 104):
                    purpleL2[1] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[1] == (0, 43, 104):
                    purpleL2[1] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[2] == (159, 43, 104):
                    purpleL2[2] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[2] == (0, 43, 104):
                    purpleL2[2] = 159, 43, 104

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[3] == (159, 43, 104):
                    purpleL2[3] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[3] == (0, 43, 104):
                    purpleL2[3] = 159, 43, 104



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

