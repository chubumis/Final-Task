#import modueles
import pygame, sys, random, time
pygame.init()
#contains the width and height
display_w = 1400
display_h = 800

#-------classes--------#
#Mouse Cursor
class Mouse(pygame.sprite.Sprite):
    '''
    Makes a rect for the mouse
    Takes in cordinate of the cursor and follows
    it so it can click various of buttons.
    Parameters
    ----------
    pygame.sprite.Sprite = image
    Takes an image and makes it into a
    sprite.
    returns
    -------
    None
    '''
    def __init__(self,picture_path):
        '''
        Add the picture to the object
        Loads an image and puts it in obect.
        Parameters
        ----------
        self = self represents the instance of the class
        picture_path = loads the image
        returns
        -------
        None
        '''
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        '''
        Adds cordinates
        Gives cursor mouse cordinates.
        Parameters
        ----------
        self = self represents the instance of the class
        returns
        -------
        None
        '''
class Button(pygame.sprite.Sprite):
    '''
    Makes sprite for buttons
    Creates various templates for
    different buttons.
    Parameters
    ----------
    pygame.sprite.Sprite = image
    Takes an image and makes it into a
    sprite.
    returns
    -------
    None
    '''
    def __init__(self,picture_path,pos_x,pos_y):
        '''
        Add the picture to the object
        Loads an image and puts it in obect
        and gives cordinates.
        Parameters
        ----------
        self = self represents the instance of the class
        picture_path = loads the image
        pos_x,pos_y = Gives sprites cordinates
        returns
        -------
        None
        '''
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]


#------Cursor image------#
cursor = Mouse("cursor.png")
#Makes a sprite group
cursor_group = pygame.sprite.Group()
#Adds image to group
cursor_group.add(cursor)

#---Button for starting the music---#
button = Button("playMusic.png",1075,77)
button_group = pygame.sprite.Group()
button_group.add(button)

#---Button for stopping the music---#
stop = Button("stopMusic.png",1285,77)
stop_group = pygame.sprite.Group()
stop_group.add(stop)

#---Button for clearing the music---#
clear = Button("clearAll.png",185,77)
clear_group = pygame.sprite.Group()
clear_group.add(clear)

#---Button for adding steady beat the music---#
steady = Button("repeat.png",385,77)
steady_group = pygame.sprite.Group()
steady_group.add(steady)

#---Button for going back to first screen---#
menuB = Button("menuB.png",755,77)
menuB_group = pygame.sprite.Group()
menuB_group.add(menuB)

#---Button for starting the game---#
start = Button("startButton.png",690,312)
start_group = pygame.sprite.Group()
start_group.add(start)

#---Button for starting the game---#
helpB = Button("helpButton.png",690,452)
helpB_group = pygame.sprite.Group()
helpB_group.add(helpB)

#---Button for back to menu screen---#
backB = Button("backButton.png",1195,732)
backB_group = pygame.sprite.Group()
backB_group.add(backB)



pygame.mixer.music.load("repeatBass.wav") #steady bass loop
snare_sound = pygame.mixer.Sound("snare.wav") #snare beat
high_sound = pygame.mixer.Sound("high.wav") #high-hat beat
openHigh_sound = pygame.mixer.Sound("openHigh.wav") #open high-hat beat
bass_sound = pygame.mixer.Sound("bass.wav") #bass drum beat
tom_sound = pygame.mixer.Sound("tom.wav") #cowbell beat
click_sound = pygame.mixer.Sound("click.wav") #clicking noise for each button in menu screen
#----------Many different variable for colors----------#
backYellow = 255,255,0
helpYellow = 255,255,0
startYellow = 255,255,0
dark_red = 180, 0, 0
endRed = 250,0,0
clearBlue = 44,120,255
light_red = 230, 0, 0
black = 0, 0, 0
grey = 25,25,25
yellow = 255,255,0
gold = 211, 175, 55
orange = 255,99,71
Mag = 255, 0,255
blue = 44,120,255
startGreen = 50,255,100
purple = 159, 43, 104
white = 255, 255, 255
menuOrange = 255,99,71
#---------All variables underneath this comment and associated with color are in lists to make it easier to input-------#
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
tempo = 10 #tempo for which the bars play the music
magenta = 255,0,255
width = 62 #width for music buttons
height = 80 #height for music buttons
timer = 0 #timer to also play the tempo
play = False #starts off as false so the tempo doesn't go off when you start the program
noteY = 250 #Y pos for music note animation
note2Y = 180 #Y pos for music note animation
moveY = -5 #movement of Y pos of music note
move2Y = 5 #movement of Y pos of music note


screen = pygame.display.set_mode((display_w, display_h))
#pictures
#bassDrum = pygame.image.load("bassDrum.png")
gameState = 'startScreen'
#function containing the different gamestates
def musicRooms():
#---------global statements allowing me to use them in different gamestates--------#
    global gameState # variable for different states
    global tempo
    global timer
    global play
    global startGreen
    global noteY
    global note2Y
    global moveY
    global move2Y
    print(tempo)
    global sy
    global menuOrange
    global tempMag
    global tempPurp
    global purple
    global purple1
    global purple2
    global purple3
    global purple4
    global purpleL
    global clicked
    global i
    global endRed
    global clearBlue
    global mouse_pos
    global yellow
    global steadyBeat
    green = 7,209,0

    x = 220#x pos for sound buttons
    y = 230#y pos for sound buttons
    sy = 330#snare pos
    hy = 430#high-hat pos
    oy = 530#open high-hat pos
    ty = 630#cowbell pos
    #variable for mouse pos
    mousePos = pygame.mouse.get_pos()

    if gameState == 'game':#sound board gamestate

        mouse_pos = pygame.mouse.get_pos()
        screen.fill(grey)
        if play == False:
            timer = 0
        if play == True:#play = true allows tempo to start
            timer += tempo#how fast the tempo is


 #-------------------------tempo bars showing where the current beat is-------------------#
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
        tempoButton = pygame.draw.rect(screen, orange, pygame.Rect(30, 130, 170, 75))
        #-----------buttons for various of controls through out the sound board--------------------#
        startButton = pygame.draw.rect(screen, startGreen, pygame.Rect(1000, 50, 150, 55))#starts the tempo bars
        endButton = pygame.draw.rect(screen, endRed, pygame.Rect(1210, 50, 150, 55))#stops the tempo bars
        clearButton = pygame.draw.rect(screen, clearBlue, pygame.Rect(110, 50, 150, 55))#clears the music buttons
        bassButton = pygame.draw.rect(screen, yellow, pygame.Rect(310, 50, 150, 55))#adds stead beat
        menuButton = pygame.draw.rect(screen, menuOrange, pygame.Rect(680, 50, 150, 55))#goes back to main screen
        #draws the needed buttons

        button_group.draw(screen)
        stop_group.draw(screen)
        clear_group.draw(screen)
        steady_group.draw(screen)
        menuB_group.draw(screen)
        cursor_group.draw(screen)
        cursor_group.update()

#--Block of code underneath makes it so when the timer hits the specific time and the music button is turned on by being a specific color make that assigned sound effect--#
        if timer == 110:#if timer is this time and button is this color make a snare sound
            if tempMag[0] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 210:#if timer is this time and button is this color make a snare sound
            if tempMag[1] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 310:#if timer is this time and button is this color make a snare sound
            if tempMag[2] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 410:#if timer is this time and button is this color make a snare sound
            if tempMag[3] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 510:#if timer is this time and button is this color make a snare sound
            if tempMag1[0] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 610:#if timer is this time and button is this color make a snare sound
            if tempMag1[1] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 710:#if timer is this time and button is this color make a snare sound
            if tempMag1[2] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 810:#if timer is this time and button is this color make a snare sound
            if tempMag1[3] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 910:#if timer is this time and button is this color make a snare sound
            if tempMag2[0] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1010:#if timer is this time and button is this color make a snare sound
            if tempMag2[1] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1110:#if timer is this time and button is this color make a snare sound
            if tempMag2[2] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1210:#if timer is this time and button is this color make a snare sound
            if tempMag2[3] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1310:#if timer is this time and button is this color make a snare sound
            if tempMag3[0] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1410:#if timer is this time and button is this color make a snare sound
            if tempMag3[1] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1510:#if timer is this time and button is this color make a snare sound
            if tempMag3[2] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)
        if timer == 1610:#if timer is this time and button is this color make a snare sound
            if tempMag3[3] == (242, 82, 120):
                pygame.mixer.Sound.play(snare_sound)

        if timer == 110:#if timer is this time and button is this color make a highhat sound
            if tempOrg[0] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 210:#if timer is this time and button is this color make a highhat sound
            if tempOrg[1] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 310:#if timer is this time and button is this color make a highhat sound
            if tempOrg[2] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 410:#if timer is this time and button is this color make a highhat sound
            if tempOrg[3] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 510:#if timer is this time and button is this color make a highhat sound
            if tempOrg1[0] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 610:#if timer is this time and button is this color make a highhat sound
            if tempOrg1[1] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 710:#if timer is this time and button is this color make a highhat sound
            if tempOrg1[2] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 810:#if timer is this time and button is this color make a highhat sound
            if tempOrg1[3] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 910:#if timer is this time and button is this color make a highhat sound
            if tempOrg2[0] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1010:#if timer is this time and button is this color make a highhat sound
            if tempOrg2[1] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1110:#if timer is this time and button is this color make a highhat sound
            if tempOrg2[2] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1210:#if timer is this time and button is this color make a highhat sound
            if tempOrg2[3] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1310:#if timer is this time and button is this color make a highhat sound
            if tempOrg3[0] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1410:#if timer is this time and button is this color make a highhat sound
            if tempOrg3[1] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1510:#if timer is this time and button is this color make a highhat sound
            if tempOrg3[2] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)
        if timer == 1610:#if timer is this time and button is this color make a highhat sound
            if tempOrg3[3] == (255,0,0):
                pygame.mixer.Sound.play(high_sound)

        if timer == 110:#if timer is this time and button is this color make a bass sound
            if purple1 == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 210:#if timer is this time and button is this color make a bass sound
            if purple2 == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 310:#if timer is this time and button is this color make a bass sound
            if purple3 == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 410:#if timer is this time and button is this color make a bass sound
            if purple4 == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 510:#if timer is this time and button is this color make a bass sound
            if purpleL[0] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 610:#if timer is this time and button is this color make a bass sound
            if purpleL[1] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 710:#if timer is this time and button is this color make a bass sound
            if purpleL[2] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 810:#if timer is this time and button is this color make a bass sound
            if purpleL[3] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 910:#if timer is this time and button is this color make a bass sound
            if purpleL1[0] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1010:#if timer is this time and button is this color make a bass sound
            if purpleL1[1] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1110:#if timer is this time and button is this color make a bass sound
            if purpleL1[2] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1210:#if timer is this time and button is this color make a bass sound
            if purpleL1[3] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1310:#if timer is this time and button is this color make a bass sound
            if purpleL2[0] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1410:#if timer is this time and button is this color make a bass sound
            if purpleL2[1] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1510:#if timer is this time and button is this color make a bass sound
            if purpleL2[2] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)
        if timer == 1610:#if timer is this time and button is this color make a bass sound
            if purpleL2[3] == (0, 43, 104):
                pygame.mixer.Sound.play(bass_sound)

        if timer == 110:#if timer is this time and button is this color make a open highhat sound
            if tempBlue[0] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 210:#if timer is this time and button is this color make a open highhat sound
            if tempBlue[1] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 310:#if timer is this time and button is this color make a open highhat sound
            if tempBlue[2] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 410:#if timer is this time and button is this color make a open highhat sound
            if tempBlue[3] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 510:#if timer is this time and button is this color make a open highhat sound
            if tempBlue1[0] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 610:#if timer is this time and button is this color make a open highhat sound
            if tempBlue1[1] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 710:#if timer is this time and button is this color make a open highhat sound
            if tempBlue1[2] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 810:#if timer is this time and button is this color make a open highhat sound
            if tempBlue1[3] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 910:#if timer is this time and button is this color make a open highhat sound
            if tempBlue2[0] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1010:#if timer is this time and button is this color make a open highhat sound
            if tempBlue2[1] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1110:#if timer is this time and button is this color make a open highhat sound
            if tempBlue2[2] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1210:#if timer is this time and button is this color make a open highhat sound
            if tempBlue2[3] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1310:#if timer is this time and button is this color make a open highhat sound
            if tempBlue3[0] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1410:#if timer is this time and button is this color make a open highhat sound
            if tempBlue3[1] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1510:#if timer is this time and button is this color make a open highhat sound
            if tempBlue3[2] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)
        if timer == 1610:#if timer is this time and button is this color make a open highhat sound
            if tempBlue3[3] == (61,243,255):
                pygame.mixer.Sound.play(openHigh_sound)

        if timer == 110:#if timer is this time and button is this color make a cowbell sound
            if tempGreen[0] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 210:#if timer is this time and button is this color make a cowbell sound
            if tempGreen[1] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 310:#if timer is this time and button is this color make a cowbell sound
            if tempGreen[2] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 410:#if timer is this time and button is this color make a cowbell sound
            if tempGreen[3] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 510:#if timer is this time and button is this color make a cowbell sound
            if tempGreen1[0] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 610:#if timer is this time and button is this color make a cowbell sound
            if tempGreen1[1] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 710:#if timer is this time and button is this color make a cowbell sound
            if tempGreen1[2] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 810:#if timer is this time and button is this color make a cowbell sound
            if tempGreen1[3] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 910:#if timer is this time and button is this color make a cowbell sound
            if tempGreen2[0] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1010:#if timer is this time and button is this color make a cowbell sound
            if tempGreen2[1] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1110:#if timer is this time and button is this color make a cowbell sound
            if tempGreen2[2] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1210:#if timer is this time and button is this color make a cowbell sound
            if tempGreen2[3] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1310:#if timer is this time and button is this color make a cowbell sound
            if tempGreen3[0] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1410:#if timer is this time and button is this color make a cowbell sound
            if tempGreen3[1] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1510:#if timer is this time and button is this color make a cowbell sound
            if tempGreen3[2] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)
        if timer == 1610:#if timer is this time and button is this color make a cowbell sound
            if tempGreen3[3] == (200,255,0):
                pygame.mixer.Sound.play(tom_sound)






#---Associating tempo bar with the timer when its on. It shows the ryhtm/beats---#
#if timer reaches a point tempo bar will switch colors than back to its original color
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

        #drawing bass buttons
        bassBar = pygame.draw.rect(screen, purple, pygame.Rect(30,230, 170,80))
        bass4 = [(x,y,width,height),(x+66,y,width,height),(x+132,y,width,height),(x+198,y,width,height)]
        bass8 = [(x+274,y,width,height),(x+340,y,width,height),(x+406,y,width,height),(x+472,y,width,height)]
        bass12 = [(x+548,y,width,height),(x+614,y,width,height),(x+680,y,width,height),(x+746,y,width,height)]
        bass16 = [(x+822,y,width,height),(x+888,y,width,height),(x+954,y,width,height),(x+1020,y,width,height)]
         #drawing snare buttons
        snareBar = pygame.draw.rect(screen, Mag, pygame.Rect(30,330, 170,80))
        snare4 = [(x,sy,width,height),(x+66,sy,width,height),(x+132,sy,width,height),(x+198,sy,width,height)]
        snare8 = [(x+274,sy,width,height),(x+340,sy,width,height),(x+406,sy,width,height),(x+472,sy,width,height)]
        snare12 = [(x+548,sy,width,height),(x+614,sy,width,height),(x+680,sy,width,height),(x+746,sy,width,height)]
        snare16 = [(x+822,sy,width,height),(x+888,sy,width,height),(x+954,sy,width,height),(x+1020,sy,width,height)]
         #drawing highhat buttons
        highHatBar = pygame.draw.rect(screen, orange, pygame.Rect(30,430, 170,80))
        highHat4 = [(x,hy,width,height),(x+66,hy,width,height),(x+132,hy,width,height),(x+198,hy,width,height)]
        highHat8 = [(x+274,hy,width,height),(x+340,hy,width,height),(x+406,hy,width,height),(x+472,hy,width,height)]
        highHat12 = [(x+548,hy,width,height),(x+614,hy,width,height),(x+680,hy,width,height),(x+746,hy,width,height)]
        highHat16 = [(x+822,hy,width,height),(x+888,hy,width,height),(x+954,hy,width,height),(x+1020,hy,width,height)]
         #drawing open highhat buttons
        openHighBar = pygame.draw.rect(screen, blue, pygame.Rect(30,530, 170,80))
        tombBar = pygame.draw.rect(screen, purple, pygame.Rect(30,630, 170,80))
        openHighHat4 = [(x,oy,width,height),(x+66,oy,width,height),(x+132,oy,width,height),(x+198,oy,width,height)]
        openHighHat8 = [(x+274,oy,width,height),(x+340,oy,width,height),(x+406,oy,width,height),(x+472,oy,width,height)]
        openHighHat12 = [(x+548,oy,width,height),(x+614,oy,width,height),(x+680,oy,width,height),(x+746,oy,width,height)]
        openHighHat16 = [(x+822,oy,width,height),(x+888,oy,width,height),(x+954,oy,width,height),(x+1020,oy,width,height)]
         #drawing cowbell buttons
        tomBar = pygame.draw.rect(screen, green, pygame.Rect(30,630, 170,80))
        tom4 = [(x,ty,width,height),(x+66,ty,width,height),(x+132,ty,width,height),(x+198,ty,width,height)]
        tom8 = [(x+274,ty,width,height),(x+340,ty,width,height),(x+406,ty,width,height),(x+472,ty,width,height)]
        tom12 = [(x+548,ty,width,height),(x+614,ty,width,height),(x+680,ty,width,height),(x+746,ty,width,height)]
        tom16 = [(x+822,ty,width,height),(x+888,ty,width,height),(x+954,ty,width,height),(x+1020,ty,width,height)]




        #draws first four bars for bass buttons. Different from the rest of code as I learnt an easier way to do it with lists
        pygame.draw.rect(screen,purple1,bass4[0])
        pygame.draw.rect(screen,purple2,bass4[1])
        pygame.draw.rect(screen,purple3,bass4[2])
        pygame.draw.rect(screen,purple4,bass4[3])
#------Uses for loops and lists so whenever I left click a square it change its color using the list and when I right click it, it goes back to its original color-----#
        for i in range(4):
            pygame.draw.rect(screen,purpleL[i],bass8[i])
        for i in range(4):
            pygame.draw.rect(screen,purpleL1[i],bass12[i])
        for i in range(4):
            pygame.draw.rect(screen,purpleL2[i],bass16[i])
        #bass drum color changes
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(230, 310)):
                if purple1 == (159, 43, 104):
                    purple1 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(230, 310)):
                if purple1 == (0, 43, 104):
                    purple1 = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(230, 310)):
                if purple2 == (159, 43, 104):
                    purple2 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(230, 310)):
                if purple2 == (0, 43, 104):
                    purple2 = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(230, 310)):
                if purple3 == (159, 43, 104):
                    purple3 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(230, 310)):
                if purple3 == (0, 43, 104):
                    purple3 = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(230, 310)):
                if purple4 == (159, 43, 104):
                    purple4 = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(230, 310)):
                if purple4 == (0, 43, 104):
                    purple4 = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[0] == (159, 43, 104):
                    purpleL[0] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[0] == (0, 43, 104):
                    purpleL[0] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[1] == (159, 43, 104):
                    purpleL[1] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[1] == (0, 43, 104):
                    purpleL[1] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[2] == (159, 43, 104):
                    purpleL[2] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[2] == (0, 43, 104):
                    purpleL[2] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[3] == (159, 43, 104):
                    purpleL[3] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL[3] == (0, 43, 104):
                    purpleL[3] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[0] == (159, 43, 104):
                    purpleL1[0] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[0] == (0, 43, 104):
                    purpleL1[0] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[1] == (159, 43, 104):
                    purpleL1[1] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[1] == (0, 43, 104):
                    purpleL1[1] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[2] == (159, 43, 104):
                    purpleL1[2] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[2] == (0, 43, 104):
                    purpleL1[2] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[3] == (159, 43, 104):
                    purpleL1[3] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL1[3] == (0, 43, 104):
                    purpleL1[3] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[0] == (159, 43, 104):
                    purpleL2[0] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[0] == (0, 43, 104):
                    purpleL2[0] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[1] == (159, 43, 104):
                    purpleL2[1] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[1] == (0, 43, 104):
                    purpleL2[1] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[2] == (159, 43, 104):
                    purpleL2[2] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[2] == (0, 43, 104):
                    purpleL2[2] = 159, 43, 104
        if pygame.mouse.get_pressed()[0]:#when left click bass drum turns on
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(230, 310)):
                if purpleL2[3] == (159, 43, 104):
                    purpleL2[3] = 0, 43, 104
        if pygame.mouse.get_pressed()[2]:#when right click bass drum turns off
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
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[0] == (255, 0,255):
                    tempMag[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[0] == (242, 82, 120):
                    tempMag[0] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[1] == (255, 0,255):
                    tempMag[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[1] == (242, 82, 120):
                    tempMag[1] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[2] == (255, 0,255):
                    tempMag[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[2] == (242, 82, 120):
                    tempMag[2] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[3] == (255, 0,255):
                    tempMag[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag[3] == (242, 82, 120):
                    tempMag[3] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[0] == (255, 0,255):
                    tempMag1[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[0] == (242, 82, 120):
                    tempMag1[0] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[1] == (255, 0,255):
                    tempMag1[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[1] == (242, 82, 120):
                    tempMag1[1] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[2] == (255, 0,255):
                    tempMag1[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[2] == (242, 82, 120):
                    tempMag1[2] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[3] == (255, 0,255):
                    tempMag1[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag1[3] == (242, 82, 120):
                    tempMag1[3] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[0] == (255, 0,255):
                    tempMag2[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[0] == (242, 82, 120):
                    tempMag2[0] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[1] == (255, 0,255):
                    tempMag2[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[1] == (242, 82, 120):
                    tempMag2[1] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[2] == (255, 0,255):
                    tempMag2[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[2] == (242, 82, 120):
                    tempMag2[2] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[3] == (255, 0,255):
                    tempMag2[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag2[3] == (242, 82, 120):
                    tempMag2[3] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[0] == (255, 0,255):
                    tempMag3[0] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[0] == (242, 82, 120):
                    tempMag3[0] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[1] == (255, 0,255):
                    tempMag3[1] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[1] == (242, 82, 120):
                    tempMag3[1] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[2] == (255, 0,255):
                    tempMag3[2] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[2] == (242, 82, 120):
                    tempMag3[2] = 255, 0,255
        if pygame.mouse.get_pressed()[0]:#when left click snare drum turns on
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(sy, sy+80)):
                if tempMag3[3] == (255, 0,255):
                    tempMag3[3] = 242, 82, 120
        if pygame.mouse.get_pressed()[2]:#when right click snare drum turns off
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

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[0] == (255,99,71):
                    tempOrg[0] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[0] == (255,0,0):
                    tempOrg[0] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[1] == (255,99,71):
                    tempOrg[1] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[1] == (255,0,0):
                    tempOrg[1] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[2] == (255,99,71):
                    tempOrg[2] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[2] == (255,0,0):
                    tempOrg[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[3] == (255,99,71):
                    tempOrg[3] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg[3] == (255,0,0):
                    tempOrg[3] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[0] == (255,99,71):
                    tempOrg1[0] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[0] == (255,0,0):
                    tempOrg1[0] = 255,99,71
        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[1] == (255,99,71):
                    tempOrg1[1] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[1] == (255,0,0):
                    tempOrg1[1] = 255,99,71
        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[2] == (255,99,71):
                    tempOrg1[2] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[2] == (255,0,0):
                    tempOrg1[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[3] == (255,99,71):
                    tempOrg1[3] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg1[3] == (255,0,0):
                    tempOrg1[3] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[0] == (255,99,71):
                    tempOrg2[0] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[0] == (255,0,0):
                    tempOrg2[0] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[1] == (255,99,71):
                    tempOrg2[1] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[1] == (255,0,0):
                    tempOrg2[1] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[2] == (255,99,71):
                    tempOrg2[2] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[2] == (255,0,0):
                    tempOrg2[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[3] == (255,99,71):
                    tempOrg2[3] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg2[3] == (255,0,0):
                    tempOrg2[3] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[0] == (255,99,71):
                    tempOrg3[0] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[0] == (255,0,0):
                    tempOrg3[0] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[1] == (255,99,71):
                    tempOrg3[1] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[1] == (255,0,0):
                    tempOrg3[1] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[2] == (255,99,71):
                    tempOrg3[2] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[2] == (255,0,0):
                    tempOrg3[2] = 255,99,71

        if pygame.mouse.get_pressed()[0]:#when left click  highhat turns on
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[3] == (255,99,71):
                    tempOrg3[3] = 255,0,0
        if pygame.mouse.get_pressed()[2]:#when right click  highhat turns off
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(hy, hy+80)):
                if tempOrg3[3] == (255,0,0):
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

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[0] == (44,120,255):
                    tempBlue[0] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[0] == (61,243,255):
                    tempBlue[0] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[1] == (44,120,255):
                    tempBlue[1] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[1] == (61,243,255):
                    tempBlue[1] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[2] == (44,120,255):
                    tempBlue[2] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[2] == (61,243,255):
                    tempBlue[2] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[3] == (44,120,255):
                    tempBlue[3] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue[3] == (61,243,255):
                    tempBlue[3] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[0] == (44,120,255):
                    tempBlue1[0] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[0] == (61,243,255):
                    tempBlue1[0] = 44,120,255
        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[1] == (44,120,255):
                    tempBlue1[1] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[1] == (61,243,255):
                    tempBlue1[1] = 44,120,255
        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[2] == (44,120,255):
                    tempBlue1[2] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[2] == (61,243,255):
                    tempBlue1[2] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[3] == (44,120,255):
                    tempBlue1[3] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue1[3] == (61,243,255):
                    tempBlue1[3] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[0] == (44,120,255):
                    tempBlue2[0] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[0] == (61,243,255):
                    tempBlue2[0] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[1] == (44,120,255):
                    tempBlue2[1] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[1] == (61,243,255):
                    tempBlue2[1] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[2] == (44,120,255):
                    tempBlue2[2] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[2] == (61,243,255):
                    tempBlue2[2] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[3] == (44,120,255):
                    tempBlue2[3] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue2[3] == (61,243,255):
                    tempBlue2[3] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[0] == (44,120,255):
                    tempBlue3[0] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[0] == (61,243,255):
                    tempBlue3[0] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[1] == (44,120,255):
                    tempBlue3[1] = 61,243,255
        if pygame.mouse.get_pressed()[2]:
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[1] == (61,243,255):
                    tempBlue3[1] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[2] == (44,120,255):
                    tempBlue3[2] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[2] == (61,243,255):
                    tempBlue3[2] = 44,120,255

        if pygame.mouse.get_pressed()[0]:#when left click open highhat turns on
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(oy, oy+80)):
                if tempBlue3[3] == (44,120,255):
                    tempBlue3[3] = 61,243,255
        if pygame.mouse.get_pressed()[2]:#when right click open highhat turns off
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


        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[0] == (7,209,0):
                    tempGreen[0] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220, 280)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[0] == (200,255,0):
                    tempGreen[0] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[1] == (7,209,0):
                    tempGreen[1] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+66, 280+66)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[1] == (200,255,0):
                    tempGreen[1] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[2] == (7,209,0):
                    tempGreen[2] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+132, 280+132)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[2] == (200,255,0):
                    tempGreen[2] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[3] == (7,209,0):
                    tempGreen[3] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+198, 280+198)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen[3] == (200,255,0):
                    tempGreen[3] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[0] == (7,209,0):
                    tempGreen1[0] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+274, 280+274)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[0] == (200,255,0):
                    tempGreen1[0] = 7,209,0
        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[1] == (7,209,0):
                    tempGreen1[1] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+340, 280+340)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[1] == (200,255,0):
                    tempGreen1[1] = 7,209,0
        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[2] == (7,209,0):
                    tempGreen1[2] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+406, 280+406)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[2] == (200,255,0):
                    tempGreen1[2] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[3] == (7,209,0):
                    tempGreen1[3] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+472, 280+472)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen1[3] == (200,255,0):
                    tempGreen1[3] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[0] == (7,209,0):
                    tempGreen2[0] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+548, 280+548)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[0] == (200,255,0):
                    tempGreen2[0] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[1] == (7,209,0):
                    tempGreen2[1] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+614, 280+614)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[1] == (200,255,0):
                    tempGreen2[1] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[2] == (7,209,0):
                    tempGreen2[2] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+680, 280+680)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[2] == (200,255,0):
                    tempGreen2[2] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[3] == (7,209,0):
                    tempGreen2[3] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+746, 280+746)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen2[3] == (200,255,0):
                    tempGreen2[3] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[0] == (7,209,0):
                    tempGreen3[0] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+822, 280+822)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[0] == (200,255,0):
                    tempGreen3[0] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[1] == (7,209,0):
                    tempGreen3[1] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+888, 280+888)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[1] == (200,255,0):
                    tempGreen3[1] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[2] == (7,209,0):
                    tempGreen3[2] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+954, 280+954)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[2] == (200,255,0):
                    tempGreen3[2] = 7,209,0

        if pygame.mouse.get_pressed()[0]:#when left click cowbell turns on
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[3] == (7,209,0):
                    tempGreen3[3] = 200,255,0
        if pygame.mouse.get_pressed()[2]:#when right click cowbell turns off
            if mouse_pos[0] in list(range(220+1020, 280+1020)) and mouse_pos[1] in list(range(ty, ty+80)):
                if tempGreen3[3] == (200,255,0):
                    tempGreen3[3] = 7,209,0


########Block of code loads various of images than draws them to label each button########
        tempoL = pygame.image.load('tempoL.png')
        screen.blit(tempoL, (31,132))#label tempo button
        bassL = pygame.image.load('bassL.png')
        screen.blit(bassL, (31,232))#label bass button
        snareL = pygame.image.load('snareL.png')
        screen.blit(snareL, (31,332))#label snare button
        highL = pygame.image.load('highL.png')
        screen.blit(highL, (31,432))#label highhat button
        openL = pygame.image.load('openL.png')
        screen.blit(openL, (31,532))#label open highhat button
        cowL = pygame.image.load('cowL.png')
        screen.blit(cowL, (31,632))#label cowbell button
        bassB = pygame.image.load('bassB.png')
        screen.blit(bassB, (310,52))#label steady bass button
        clearB = pygame.image.load('clearB.png')
        screen.blit(clearB, (113,52))#label clear all button
        startB = pygame.image.load('startB.png')
        screen.blit(startB, (1002,52))#label start button
        stopB = pygame.image.load('stopB.png')
        screen.blit(stopB, (1215,52))#label stop button
        pygame.display.flip()

#############GameState for start screen########
    if gameState == 'startScreen':
        #global variables to be called in this gameState
        global startYellow
        global helpYellow
        noteY += moveY#allows music note animation to move up
        note2Y += move2Y#allows music note animation to move down
        #note2Y += 5
        if noteY < 20:#allows music note animation to move down
            move2Y = -5
            moveY = 5
        if noteY > 350:#allows music note animation to move up
            move2Y = 5
            moveY = -5
        mouse_pos = pygame.mouse.get_pos()#give variable to mouse pos
        screen.fill(grey)#fills screen grey
        Title = pygame.image.load('musicMachine.png')#loads title
        screen.blit(Title, (0,0))#draws the title
        musicNote = pygame.image.load("musicNote.png")#loads music note
        screen.blit(musicNote,(10,noteY))#draws music note
        secondNote = pygame.image.load("secondNote.png")#load second music note
        screen.blit(secondNote,(1000,note2Y))#draws second music note
        play = pygame.draw.rect(screen, startYellow, pygame.Rect(545, 275, 290, 75))#play button
        play2 = pygame.draw.rect(screen, helpYellow, pygame.Rect(545, 415, 290, 75))#help button
        start_group.draw(screen)#draws play button
        helpB_group.draw(screen)#draws help button
        cursor_group.update()#updates cursor movement
        #for loop to change gamestates to help screen and music screen
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(cursor,start_group,False):#switches gamestate to music board state
                    pygame.mixer.Sound.play(click_sound)
                    gameState = 'game'

                if pygame.sprite.spritecollide(cursor,helpB_group,False):#switches gamestate to help state
                    pygame.mixer.Sound.play(click_sound)
                    gameState = 'helpState'
            if event.type == pygame.MOUSEMOTION:
                if mouse_pos[0] in list(range(545, 835)) and mouse_pos[1] in list(range(275, 350)):#indicates when you hover over button
                    startYellow = 100,100,0
                else:
                    startYellow = 255,255,0
                if mouse_pos[0] in list(range(545, 835)) and mouse_pos[1] in list(range(415, 490)):#indicates when you hover over button
                    helpYellow = 100,100,0
                else:
                    helpYellow = 255,255,0
#game state is help state
    if gameState == 'helpState':
        global backYellow
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(grey)
        instuctions = pygame.image.load('instruction.png')#loads instruction image
        screen.blit(instuctions, (0,0))#draws instruction image. I decided to make instructions into draw as its less lines of code and less work than using the text command
        backHelp = pygame.draw.rect(screen, backYellow, pygame.Rect(1050, 695, 290, 75))#back button to start screen
        backB_group.draw(screen)#draws back button
        cursor_group.update()#updates cursor
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.sprite.spritecollide(cursor,backB_group,False):#collision with back button
                    pygame.mixer.Sound.play(click_sound)
                    gameState = 'startScreen'
            if event.type == pygame.MOUSEMOTION:
                if mouse_pos[0] in list(range(1050, 1340)) and mouse_pos[1] in list(range(695, 770)):#indicates hovering over back button
                    backYellow = 100,100,0
                else:
                    backYellow = 255,255,0

#program running loop
while True:
#for loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#click x to quit program
            pygame.quit()
            sys.exit()
    print(pygame.mouse.get_pos())
    musicRooms()#uses gamestates function
    #--------------This for loop makes it whenever a control button in the sound board state is clicked make it do a certain action-------#
    #this block has to be in the while true loop without a function as it becomes really laggy if i put it in a function
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mouse collision for restarting the music
                if pygame.sprite.spritecollide(cursor,button_group,False): #when mouse clicks the green start button
                    play = True #starts the tempo
                #mouse collision for stopping the music
                if pygame.sprite.spritecollide(cursor,stop_group,False):#when mouse clicks the red stop button
                    play = False#stops the tempo
                #mouse collision for clear all music
                if pygame.sprite.spritecollide(cursor,clear_group,False):#when cursor clicks blue clear button it turns all the button to specific color de-activating them
                    purple1 = 159, 43, 104
                    purple2 = 159, 43, 104
                    purple3 = 159, 43, 104
                    purple4 = 159, 43, 104
                    for i in range(len(purpleL and purpleL1 and purpleL2 and tempMag and tempMag1 and tempMag2 and tempMag3 and tempGreen and tempGreen1 and tempGreen2 and tempGreen3)):
                        purpleL[i] = 159, 43, 104
                        purpleL1[i] = 159, 43, 104
                        purpleL2[i] = 159, 43, 104
                        tempMag[i] = 255, 0,255
                        tempMag1[i] = 255, 0,255
                        tempMag2[i] = 255, 0,255
                        tempMag3[i] = 255, 0,255
                        tempGreen[i] = 7,209,0
                        tempGreen1[i] = 7,209,0
                        tempGreen2[i] = 7,209,0
                        tempGreen3[i] = 7,209,0
                    for i in range(len(tempBlue and tempBlue1 and tempBlue2 and tempBlue3 and tempOrg and tempOrg1 and tempOrg2 and tempOrg3)):
                        tempBlue[i] = 44,120,255
                        tempBlue1[i] = 44,120,255
                        tempBlue2[i] = 44,120,255
                        tempBlue3[i] = 44,120,255
                        tempOrg[i] = 255,99,71
                        tempOrg1[i] = 255,99,71
                        tempOrg2[i] = 255,99,71
                        tempOrg3[i] = 255,99,71
                if pygame.mouse.get_pressed()[0]:
                    if pygame.sprite.spritecollide(cursor,steady_group,False):
                        pygame.mixer.music.play(-1)
                if pygame.mouse.get_pressed()[2]:
                    if pygame.sprite.spritecollide(cursor,steady_group,False):
                        pygame.mixer.music.stop()
                if pygame.sprite.spritecollide(cursor,menuB_group,False):
                    pygame.mixer.Sound.play(click_sound)
                    gameState = 'startScreen'

#--This event makes it so when I hove the control button is the music board state it will change colors indication collision is happening with that button--#
            elif event.type == pygame.MOUSEMOTION:
                if mouse_pos[0] in list(range(1000, 1150)) and mouse_pos[1] in list(range(50, 100)):#indicating interaction with start button
                    startGreen = 0,100,0
                else:
                    startGreen = 50,255,100
                if mouse_pos[0] in list(range(1210, 1360)) and mouse_pos[1] in list(range(50, 100)):#indicating interaction with stop button
                    endRed = 100,0,0
                else:
                    endRed = 255,0,0
                if mouse_pos[0] in list(range(110, 260)) and mouse_pos[1] in list(range(50, 100)):#indicating interaction with clear button
                    clearBlue = 0,0,255
                else:
                    clearBlue = 44,120,255
                if mouse_pos[0] in list(range(310, 460)) and mouse_pos[1] in list(range(50, 100)):#indicating interaction with bass tempo button
                    yellow = 184,184,0
                else:
                    yellow = 255,255,0
                if mouse_pos[0] in list(range(680, 830)) and mouse_pos[1] in list(range(50, 100)):#indicating interaction with menu button
                    menuOrange = 200,20,0
                else:
                    menuOrange = 255,99,71
    pygame.display.flip()

pygame.quit()
quit()
