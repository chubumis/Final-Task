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
tempOrg = [(255,99,71),(255,99,71),(255,99,71),(255,99,71)]
tempOrg1 = [(255,99,71),(255,99,71),(255,99,71),(255,99,71)]
tempOrg2 = [(255,99,71),(255,99,71),(255,99,71),(255,99,71)]
tempOrg3 = [(255,99,71),(255,99,71),(255,99,71),(255,99,71)]
tempBlue = [(44,120,255),(44,120,255),(44,120,255),(44,120,255)]
tempBlue1 = [(44,120,255),(44,120,255),(44,120,255),(44,120,255)]
tempBlue2 = [(44,120,255),(44,120,255),(44,120,255),(44,120,255)]
tempBlue3 = [(44,120,255),(44,120,255),(44,120,255),(44,120,255)]
tempMag = [(255, 0,255),(255, 0,255),(255, 0,255),(255, 0,255)]
tempMag1 = [(255, 0,255),(255, 0,255),(255, 0,255),(255, 0,255)]
tempMag2 = [(255, 0,255),(255, 0,255),(255, 0,255),(255, 0,255)]
tempMag3 = [(255, 0,255),(255, 0,255),(255, 0,255),(255, 0,255)]
tempGreen = [(7,209,0),(7,209,0),(7,209,0),(7,209,0)]
tempGreen1 = [(7,209,0),(7,209,0),(7,209,0),(7,209,0)]
tempGreen2 = [(7,209,0),(7,209,0),(7,209,0),(7,209,0)]
tempGreen3 = [(7,209,0),(7,209,0),(7,209,0),(7,209,0)]

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

    global sy
    global tempMag
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
    sy = 330
    hy = 430
    oy = 530
    ty = 630
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
        snare4 = [(x,sy,width,height),(x+66,sy,width,height),(x+132,sy,width,height),(x+198,sy,width,height)]
        snare8 = [(x+274,sy,width,height),(x+340,sy,width,height),(x+406,sy,width,height),(x+472,sy,width,height)]
        snare12 = [(x+548,sy,width,height),(x+614,sy,width,height),(x+680,sy,width,height),(x+746,sy,width,height)]
        snare16 = [(x+822,sy,width,height),(x+888,sy,width,height),(x+954,sy,width,height),(x+1020,sy,width,height)]

        highHatBar = pygame.draw.rect(screen, purple, pygame.Rect(30,430, 170,80))
        highHat4 = [(x,hy,width,height),(x+66,hy,width,height),(x+132,hy,width,height),(x+198,hy,width,height)]
        highHat8 = [(x+274,hy,width,height),(x+340,hy,width,height),(x+406,hy,width,height),(x+472,hy,width,height)]
        highHat12 = [(x+548,hy,width,height),(x+614,hy,width,height),(x+680,hy,width,height),(x+746,hy,width,height)]
        highHat16 = [(x+822,hy,width,height),(x+888,hy,width,height),(x+954,hy,width,height),(x+1020,hy,width,height)]

        openHighBar = pygame.draw.rect(screen, purple, pygame.Rect(30,530, 170,80))
        openHighHat4 = [(x,oy,width,height),(x+66,oy,width,height),(x+132,oy,width,height),(x+198,oy,width,height)]
        openHighHat8 = [(x+274,oy,width,height),(x+340,oy,width,height),(x+406,oy,width,height),(x+472,oy,width,height)]
        openHighHat12 = [(x+548,oy,width,height),(x+614,oy,width,height),(x+680,oy,width,height),(x+746,oy,width,height)]
        openHighHat16 = [(x+822,oy,width,height),(x+888,oy,width,height),(x+954,oy,width,height),(x+1020,oy,width,height)]

        tomBar = pygame.draw.rect(screen, purple, pygame.Rect(30,630, 170,80))
        tom4 = [(x,ty,width,height),(x+66,ty,width,height),(x+132,ty,width,height),(x+198,ty,width,height)]
        tom8 = [(x+274,ty,width,height),(x+340,ty,width,height),(x+406,ty,width,height),(x+472,ty,width,height)]
        tom12 = [(x+548,ty,width,height),(x+614,ty,width,height),(x+680,ty,width,height),(x+746,ty,width,height)]
        tom16 = [(x+822,ty,width,height),(x+888,ty,width,height),(x+954,ty,width,height),(x+1020,ty,width,height)]



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


    #Collision to snare sequencer
        for i in range(4):
            pygame.draw.rect(screen,tempMag[i],snare4[i])
        for i in range(4):
            pygame.draw.rect(screen,tempMag1[i],snare8[i])
        for i in range(4):
            pygame.draw.rect(screen,tempMag2[i],snare12[i])
        for i in range(4):
            pygame.draw.rect(screen,tempMag3[i],snare16[i])

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[0] == (255, 0,255):
                    tempMag[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[0] == (242, 82, 120):
                    tempMag[0] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[1] == (255, 0,255):
                    tempMag[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[1] == (242, 82, 120):
                    tempMag[1] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[2] == (255, 0,255):
                    tempMag[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[2] == (242, 82, 120):
                    tempMag[2] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[3] == (255, 0,255):
                    tempMag[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[3] == (242, 82, 120):
                    tempMag[3] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[0] == (255, 0,255):
                    tempMag1[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[0] == (242, 82, 120):
                    tempMag1[0] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[1] == (255, 0,255):
                    tempMag1[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[1] == (242, 82, 120):
                    tempMag1[1] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[2] == (255, 0,255):
                    tempMag1[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[2] == (242, 82, 120):
                    tempMag1[2] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[3] == (255, 0,255):
                    tempMag1[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[3] == (242, 82, 120):
                    tempMag1[3] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[0] == (255, 0,255):
                    tempMag2[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[0] == (242, 82, 120):
                    tempMag2[0] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[1] == (255, 0,255):
                    tempMag2[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[1] == (242, 82, 120):
                    tempMag2[1] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[2] == (255, 0,255):
                    tempMag2[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[2] == (242, 82, 120):
                    tempMag2[2] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[3] == (255, 0,255):
                    tempMag2[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[3] == (242, 82, 120):
                    tempMag2[3] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[0] == (255, 0,255):
                    tempMag3[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[0] == (242, 82, 120):
                    tempMag3[0] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[1] == (255, 0,255):
                    tempMag3[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[1] == (242, 82, 120):
                    tempMag3[1] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[2] == (255, 0,255):
                    tempMag3[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[2] == (242, 82, 120):
                    tempMag3[2] = 255, 0,255

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[3] == (255, 0,255):
                    tempMag3[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[3] == (242, 82, 120):
                    tempMag3[3] = 255, 0,255


        #Collision to Highhat sequencer
        for i in range(4):
            pygame.draw.rect(screen,tempOrg[i],highHat4[i])
        for i in range(4):
            pygame.draw.rect(screen,tempOrg1[i],highHat8[i])
        for i in range(4):
            pygame.draw.rect(screen,tempOrg2[i],highHat12[i])
        for i in range(4):
            pygame.draw.rect(screen,tempOrg3[i],highHat16[i])

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[0] == (255,99,71):
                    tempOrg[0] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[0] == (255,94,0):
                    tempOrg[0] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[1] == (255,99,71):
                    tempOrg[1] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[1] == (255,94,0):
                    tempOrg[1] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[2] == (255,99,71):
                    tempOrg[2] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[2] == (255,94,0):
                    tempOrg[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[3] == (255,99,71):
                    tempOrg[3] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[3] == (255,94,0):
                    tempOrg[3] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[0] == (255,99,71):
                    tempOrg1[0] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[0] == (255,94,0):
                    tempOrg1[0] = 255,99,71
        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[1] == (255,99,71):
                    tempOrg1[1] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[1] == (255,94,0):
                    tempOrg1[1] = 255,99,71
        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[2] == (255,99,71):
                    tempOrg1[2] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[2] == (255,94,0):
                    tempOrg1[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[3] == (255,99,71):
                    tempOrg1[3] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[3] == (255,94,0):
                    tempOrg1[3] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[0] == (255,99,71):
                    tempOrg2[0] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[0] == (255,94,0):
                    tempOrg2[0] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[1] == (255,99,71):
                    tempOrg2[1] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[1] == (255,94,0):
                    tempOrg2[1] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[2] == (255,99,71):
                    tempOrg2[2] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[2] == (255,94,0):
                    tempOrg2[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[3] == (255,99,71):
                    tempOrg2[3] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[3] == (255,94,0):
                    tempOrg2[3] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[0] == (255,99,71):
                    tempOrg3[0] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[0] == (255,94,0):
                    tempOrg3[0] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[1] == (255,99,71):
                    tempOrg3[1] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[1] == (255,94,0):
                    tempOrg3[1] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[2] == (255,99,71):
                    tempOrg3[2] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[2] == (255,94,0):
                    tempOrg3[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[3] == (255,99,71):
                    tempOrg3[3] = 255,94,0
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[3] == (255,94,0):
                    tempOrg3[3] = 255,99,71


        #Collision to OpenHighhat sequencer
        for i in range(4):
            pygame.draw.rect(screen,tempBlue[i],openHighHat4[i])
        for i in range(4):
            pygame.draw.rect(screen,tempBlue1[i],openHighHat8[i])
        for i in range(4):
            pygame.draw.rect(screen,tempBlue2[i],openHighHat12[i])
        for i in range(4):
            pygame.draw.rect(screen,tempBlue3[i],openHighHat16[i])

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[0] == (44,120,255):
                tempBlue[0] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[0] == (61,243,255):
                tempBlue[0] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[1] == (44,120,255):
                tempBlue[1] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[1] == (61,243,255):
                tempBlue[1] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[2] == (44,120,255):
                tempBlue[2] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[2] == (61,243,255):
                tempBlue[2] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[3] == (44,120,255):
                tempBlue[3] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue[3] == (61,243,255):
                tempBlue[3] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[0] == (44,120,255):
                tempBlue1[0] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[0] == (61,243,255):
                tempBlue1[0] = 44,120,255
    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[1] == (44,120,255):
                tempBlue1[1] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[1] == (61,243,255):
                tempBlue1[1] = 44,120,255
    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[2] == (44,120,255):
                tempBlue1[2] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[2] == (61,243,255):
                tempBlue1[2] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[3] == (44,120,255):
                tempBlue1[3] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue1[3] == (61,243,255):
                tempBlue1[3] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[0] == (44,120,255):
                tempBlue2[0] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[0] == (61,243,255):
                tempBlue2[0] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[1] == (44,120,255):
                tempBlue2[1] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[1] == (61,243,255):
                tempBlue2[1] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[2] == (44,120,255):
                tempBlue2[2] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[2] == (61,243,255):
                tempBlue2[2] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[3] == (44,120,255):
                tempBlue2[3] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue2[3] == (61,243,255):
                tempBlue2[3] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[0] == (44,120,255):
                tempBlue3[0] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[0] == (61,243,255):
                tempBlue3[0] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[1] == (44,120,255):
                tempBlue3[1] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[1] == (61,243,255):
                tempBlue3[1] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[2] == (44,120,255):
                tempBlue3[2] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[2] == (61,243,255):
                tempBlue3[2] = 44,120,255

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[3] == (44,120,255):
                tempBlue3[3] = 61,243,255
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(oy, oy+80)):
            if tempBlue3[3] == (61,243,255):
                tempBlue3[3] = 44,120,255


    #Collision to tom sequencer
    for i in range(4):
        pygame.draw.rect(screen,tempGreen[i],tom4[i])
    for i in range(4):
        pygame.draw.rect(screen,tempGreen1[i],tom8[i])
    for i in range(4):
        pygame.draw.rect(screen,tempGreen2[i],tom12[i])
    for i in range(4):
        pygame.draw.rect(screen,tempGreen3[i],tom16[i])


    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[0] == (7,209,0):
                tempGreen[0] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[0] == (51,255,51):
                tempGreen[0] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[1] == (7,209,0):
                tempGreen[1] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[1] == (51,255,51):
                tempGreen[1] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[2] == (7,209,0):
                tempGreen[2] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[2] == (51,255,51):
                tempGreen[2] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[3] == (7,209,0):
                tempGreen[3] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen[3] == (51,255,51):
                tempGreen[3] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[0] == (7,209,0):
                tempGreen1[0] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[0] == (51,255,51):
                tempGreen1[0] = 7,209,0
    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[1] == (7,209,0):
                tempGreen1[1] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[1] == (51,255,51):
                tempGreen1[1] = 7,209,0
    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[2] == (7,209,0):
                tempGreen1[2] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[2] == (51,255,51):
                tempGreen1[2] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[3] == (7,209,0):
                tempGreen1[3] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen1[3] == (51,255,51):
                tempGreen1[3] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[0] == (7,209,0):
                tempGreen2[0] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[0] == (51,255,51):
                tempGreen2[0] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[1] == (7,209,0):
                tempGreen2[1] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[1] == (51,255,51):
                tempGreen2[1] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[2] == (7,209,0):
                tempGreen2[2] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[2] == (51,255,51):
                tempGreen2[2] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[3] == (7,209,0):
                tempGreen2[3] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen2[3] == (51,255,51):
                tempGreen2[3] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[0] == (7,209,0):
                tempGreen3[0] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[0] == (51,255,51):
                tempGreen3[0] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[1] == (7,209,0):
                tempGreen3[1] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[1] == (51,255,51):
                tempGreen3[1] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[2] == (7,209,0):
                tempGreen3[2] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[2] == (51,255,51):
                tempGreen3[2] = 7,209,0

    if pygame.mouse.get_pressed()[0]:
        if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[3] == (7,209,0):
                tempGreen3[3] = 51,255,51
    if pygame.mouse.get_pressed()[2]:
        if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(ty, ty+80)):
            if tempGreen3[3] == (51,255,51):
                tempGreen3[3] = 7,209,0


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
