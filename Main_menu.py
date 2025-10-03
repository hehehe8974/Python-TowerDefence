#Import
import pygame
import sys
import random
from Game import difficulty as dif #Game
from pygame.locals import *
from Settings import * #Settings

#Classes
#Creating Button
class Button(pygame.sprite.Sprite):
    def __init__(self, screen, position, text, size, bg, proc):
        super().__init__()
        self.bg = bg #Background color
        self.proc = proc #Procedure
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, white)
        self.image = self.text_render
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        buttons.add(self)

    #Kills all other sprites
    def hide(self):
        for i in buttons:
            i.kill()
        for i in titles:
            i.kill()
        for i in splashs:
            i.kill()
        for i in texts:
            i.kill()
        for i in Gvolumebar:
            i.kill()

    def update(self, events, mouse):
        global visible
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos): #If the button is clicked
                    clicksound.play()
                    self.hide()
                    self.proc()
                    visible = False
        if self.rect.collidepoint(mouse): #If the mouse hovers over the button
            pygame.draw.rect(screen, Dgray, [self.x, self.y, self.w, self.h]) #Background = Dark Gray
        else:
            pygame.draw.rect(screen, self.bg, [self.x, self.y, self.w, self.h]) #Background = Light Gray

#Creating/Moving clouds in the background
class Cloud(pygame.sprite.Sprite):
    def __init__(self, position, size, speed):
        super().__init__()
        global cloudImg
        self.x, self.y = position
        self.size = size
        self.speed = speed
        self.cloudImg = pygame.transform.scale(cloudImg, (round(Wcloud*size*Wres), 
                                                          round(Hcloud*size*Hres)))
        clouds.add(self)

    #Moving the cloud
    def update(self):
        screen.blit(self.cloudImg, (self.x, self.y))
        self.x += self.speed
        if self.x > width + width/10:
            self.x = -300
            self.speed = random.randint(30, 80)/10
            self.size = random.randint(10, 40)/100

#Creating the title image
class Title(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        global titleImg
        self.x, self.y = position
        self.size = size
        titleImg = pygame.transform.scale(titleImg, (round(Wtitle*size*Wres), round(Htitle*size*Hres)))
        titles.add(self)
    
    def update(self):
        screen.blit(titleImg, (self.x, self.y))

#Creating shapes using points
class Shape(pygame.sprite.Sprite):
    def __init__(self, points, bg):
        super().__init__()
        self.points = points
        self.bg = bg
        shapes.add(self)

    def update(self):
        pygame.draw.polygon(screen, self.bg, self.points)

#Creating textbox
class Text(pygame.sprite.Sprite):
    def __init__(self, position, text, size, bg):
        super().__init__()
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, white)
        self.image = self.text_render
        self.bg = bg
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        texts.add(self)

    def update(self):
        pygame.draw.rect(screen, self.bg, [self.x, self.y, self.w, self.h])

#Creating splash (i.e. the yellow word getting bigger & smaller like Minecraft)
class Splash(pygame.sprite.Sprite):
    def __init__(self, position, text, size):
        super().__init__()
        self.t = text
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, yellow)
        self.x, self.y = position
        self.text = pygame.transform.rotate(self.text_render, 20)
        self.position = position
        self.grow = True
        self.s = 70 #size
        splashs.add(self)

    def update(self):
        self.font = pygame.font.SysFont("Verdana", round(width/(self.s*0.25)))
        self.text_render = self.font.render(self.t, 1, yellow)
        self.text = pygame.transform.rotate(self.text_render, 20)
        screen.blit(self.text, (self.x, self.y))
        if self.grow == True:
            self.s +=1
            if self.s == 80:
                self.grow = False
        elif self.grow == False:
            self.s -=1
            if self.s == 60:
                self.grow = True

###########################################################################
#Functions/Procedures
#Quit
def Quit():
    pygame.quit()
    sys.exit()

#About Page
def pgAbout():
    sBg = Shape(((width/10, height/8), (width/1.1, height/8), (width/1.1, height/1.15,), (width/10, height/1.15)), Lgray)
    taboutH = Text((width/2.3, height/7), "About", fontsize, Dgray)
    tabout1 = Text((width/6, height - (15*height/20)), "Everything made by : Brian Lee", fontsize, Dgray)
    tabout2 = Text((width/6, height - (11*height/20)), "2023-06-02", fontsize, Dgray)
    tabout3 = Text((width/6, height - (9*height/20)), "London, ON", fontsize, Dgray)
    bBack = Button(screen, (width/20, height/1.1), "Back", fontsize, Lgray, back)

#Settings Page
def pgSet():
    global mVolume
    bVol = Button(screen, (width/2.3, height - (4*height/10)), "Volume", fontsize, Lgray, hi)
    bPlus = Button(screen, (width/1.33, height - (3*height/10)), "+", fontsize, Lgray, plus)
    bMinus = Button(screen, (width/4, height - (3*height/10)), "-", fontsize, Lgray, minus)
    bBack = Button(screen, (width/2.2, height - (2*height/10)), "Back", fontsize, Lgray, back)
    VolumeBar((width/3.3333, height/1.4117), Lgray)

#Help Page
def pgHelp():
    sBg = Shape(((width/10, height/8), (width/1.1, height/8), (width/1.1, height/1.15,), (width/10, height/1.15)), Lgray)
    tHelpH = Text((width/3, height/7), "How to Play", fontsize, Dgray)
    tHelp1 = Text((width/6, height - (15*height/20)), "This is a tower defence game.", round(width/50), Dgray)
    tHelp2 = Text((width/6, height - (14*height/20)), "Click the signs on the map to build one of the three towers.", round(width/50), Dgray)
    tHelp3 = Text((width/6, height - (13*height/20)), "Players are able to see the range of the tower by clicking it.", round(width/50), Dgray)
    tHelp4 = Text((width/6, height - (12*height/20)), "Click the towers to upgrade and increase their damage.", round(width/50), Dgray)
    tHelp5 = Text((width/6, height - (11*height/20)), "Upgrades are permanent and it will apply to all the same towers.", round(width/50), Dgray)
    tHelp6 = Text((width/6, height - (10*height/20)), "Upgrades gets more expensive as you upgrade (espicially cannon).", round(width/50), Dgray)
    tHelp7 = Text((width/6, height - (9*height/20)), "Players may sell their towers half the price of the tower.", round(width/50), Dgray)
    tHelp8 = Text((width/6, height - (8*height/20)), "Click the play button on the lower right corner to move to the next wave.", round(width/50), Dgray)
    tHelp9 = Text((width/6, height - (7*height/20)), "Enemies get stronger proportional to the number of waves.", round(width/50), Dgray)
    tHelp10 = Text((width/3, height - (5*height/20)), "Good Luck!", fontsize, Dgray)
    bBack = Button(screen, (width/20, height/1.1), "Back", fontsize, Lgray, back)

#Play Page
def pgPlay():
    di = dif()
    bBack = Button(screen, (width/2.2, height - height/10), "Back", fontsize, Lgray, back)
    bHard = Button(screen, (width/2.2, height - (2*height/10)), "Hard", fontsize, Lgray, di.GameHard)
    bNorm = Button(screen, (width/2.3, height - (3*height/10)), "Normal", fontsize, Lgray, di.GameNormal)
    bEasy = Button(screen, (width/2.2, height - (4*height/10)), "Easy", fontsize, Lgray, di.GameEasy)

#HI
def hi():
    print('hi')

#Reduce volume
def minus():
    global mVolume
    if round(mVolume, 1) > 0:
        mVolume = mVolume - 0.1
    for i in sounds:
        i.set_volume(mVolume)
    pygame.mixer.music.set_volume(mVolume)
    bVol = Button(screen, (width/2.3, height - (4*height/10)), "Volume", fontsize, Lgray, hi)
    bPlus = Button(screen, (width/1.33, height - (3*height/10)), "+", fontsize, Lgray, plus)
    bMinus = Button(screen, (width/4, height - (3*height/10)), "-", fontsize, Lgray, minus)
    bBack = Button(screen, (width/2.2, height - (2*height/10)), "Back", fontsize, Lgray, back)
    VolumeBar((width/3.3333, height/1.4117), Lgray)

#Increase volume
def plus():
    global mVolume
    if round(mVolume, 1) < 1:
        mVolume = mVolume + 0.1
    for i in sounds:
        i.set_volume(mVolume)
    pygame.mixer.music.set_volume(mVolume)
    bVol = Button(screen, (width/2.3, height - (4*height/10)), "Volume", fontsize, Lgray, hi)
    bPlus = Button(screen, (width/1.33, height - (3*height/10)), "+", fontsize, Lgray, plus)
    bMinus = Button(screen, (width/4, height - (3*height/10)), "-", fontsize, Lgray, minus)
    bBack = Button(screen, (width/2.2, height - (2*height/10)), "Back", fontsize, Lgray, back)
    VolumeBar((width/3.3333, height/1.4117), Lgray)

#Go back
def back():
    bAbout = Button(screen, (round(width/1.1363), round(height/24)), 'About', fontsize, Lgray, pgAbout)
    bQuit = Button(screen, (width/2.2, height - height/10), "Quit", fontsize, Lgray, Quit)
    bSet = Button(screen, (width/2.4, height - (2*height/10)), "Settings", fontsize, Lgray, pgSet)
    bHelp = Button(screen, (width/2.2, height - (3*height/10)), "Help", fontsize, Lgray, pgHelp)
    bPlay = Button(screen, (width/2.2, height - (4*height/10)), "Play", fontsize, Lgray, pgPlay)
    tTitle = Title((round(width/3.6), height/5), 1)
    sHi = Splash((round(width/4), height/7), "Hi", fontsize)
    for i in texts:
        i.kill()
    for i in shapes:
        i.kill()
    for i in Gvolumebar:
        i.kill()

#Main menu
def Mainmenu():
    global mVolume
    pygame.mixer.music.load('Assets/Dungreed Soundtrack - 10. Little Forest.mp3') #Main music
    pygame.mixer.music.play(-1) #Loop forever
    pygame.mixer.music.set_volume(mVolume)
    #Main Menu Page
    bQuit = Button(screen, (round(width/2.2), round(height - height/10)), "Quit", fontsize, Lgray, Quit)
    bSet = Button(screen, (round(width/2.4), round(height - (2*height/10))), "Settings", fontsize, Lgray, pgSet)
    bHelp = Button(screen, (round(width/2.2), round(height - (3*height/10))), "Help", fontsize, Lgray, pgHelp)
    bPlay = Button(screen, (round(width/2.2), round(height - (4*height/10))), "Play", fontsize, Lgray, pgPlay)
    bAbout = Button(screen, (round(width/1.1363), round(height/24)), 'About', fontsize, Lgray, pgAbout)
    c1 = Cloud((round(width/2), round(height/2)), random.randint(10, 40)/100, random.randint(1, 80)/10)
    c2 = Cloud((round(width/5), round(height/12)), random.randint(10, 40)/100, random.randint(1, 80)/10)
    c3 = Cloud((round(width/12), round(height/1.4)), random.randint(10, 40)/100, random.randint(1, 80)/10)
    c4 = Cloud((round(width - width*1.2), round(height/2.6)), random.randint(10, 40)/100, random.randint(1, 80)/10)
    c5 = Cloud((round(width - width*1.5), round(height/4)), random.randint(10, 40)/100, random.randint(1, 80)/10)
    tTitle = Title((round(width/4), height/7), 1.1)
    sHi = Splash((round(width/4), height/7), "Hi", fontsize)
    while True:
        events = pygame.event.get()
        for event in events: 
            if event.type == QUIT: 
                pygame.quit() 
                sys.exit()
        screen.fill(sky) #Background color = sky blue
        mouse = pygame.mouse.get_pos() #Get mouse position

        #Update every groups (i.e. loop everything)
        clouds.update()
        shapes.update()
        buttons.update(events, mouse)
        buttons.draw(screen)
        titles.update()
        splashs.update()
        texts.update()
        texts.draw(screen)
        Gvolumebar.update(mVolume)
        pygame.display.update()
        clock.tick(fps)
