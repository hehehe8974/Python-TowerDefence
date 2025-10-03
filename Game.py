import pygame
import sys
import random
import time
from Settings import *
from pygame.locals import *
from Enemy import *

#Base game settings
money = 300
life = 5
pause = True

#Loading Cloud
class Cloud(pygame.sprite.Sprite):
    def __init__(self, position, size, speed):
        super().__init__()
        global cloudImg
        self.x, self.y = position
        self.size = size
        self.speed = speed
        self.cloudImg = pygame.transform.scale(cloudImg, (round(Wcloud*size*Wres), round(Hcloud*size*Hres)))
        clouds.add(self)

    def update(self):
        screen.blit(self.cloudImg, (self.x, self.y))
        self.x += self.speed
        if self.x > width + width/10:
            self.x = -300
            self.speed = random.randint(30, 80)/10
            self.size = random.randint(10, 40)/100

#Loading
class loading(pygame.sprite.Sprite):
    def __init__(self, position, size, speed):
        super().__init__()
        global cloudImg
        self.x, self.y = position
        self.size = size
        self.speed = speed
        self.cloudImg = pygame.transform.scale(cloudImg, (round(Wcloud*size*Wres), round(Hcloud*size*Hres)))
        loads.add(self)

    def update(self):
        screen.blit(self.cloudImg, (self.x, self.y))
        self.x += self.speed

#######################################################################################
#Pre Tower/Sign
class preTower(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.size = size
        self.Img = pygame.transform.scale(preTImg, (round(WpreTImg*size*Wres),  #Normal
                                                    round(HpreTImg*size*Hres)))
        self.Img2 = pygame.transform.scale(preTImg2, (round(WpreTImg2*size*Wres), #Shining
                                                      round(HpreTImg2*size*Hres)))
        self.x, self.y, self.w, self.h = self.Img.get_rect()
        self.x, self.y = position
        self.position = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.clicked = False #Whether the sign is clicked
        preTs.add(self)
    
    def update(self, events, mouse):
        screen.blit(self.Img, (self.x, self.y))
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    clicksound.play()
                    for i in Tmenus:
                        i.kill()
                    self.Tmenu = Tmenu((0, 0), 0.8, 'Construct Tower', self.position, self) #Tower Construct Menu
                    self.clicked = True
                else:
                    self.clicked = False
        if self.rect.collidepoint(mouse) or self.clicked == True:
            screen.blit(self.Img2, (self.x, self.y)) #Shining if clicked or hovered
        else:
            screen.blit(self.Img, (self.x, self.y))

#Tower Menu
class Tmenu(pygame.sprite.Sprite):
    def __init__(self, position, size, text, tpos, s):
        super().__init__()
        self.size = size
        self.Iarcher = pygame.transform.scale(Iarcher, (round(WIarcher*size*Wres), 
                                                        round(HIarcher*size*Hres)))
        self.Icannon = pygame.transform.scale(Icannon, (round(WIcannon*size*Wres), 
                                                        round(HIcannon*size*Hres)))
        self.Imagic = pygame.transform.scale(Imagic, (round(WImagic*size*Wres), 
                                                        round(HImagic*size*Hres)))
        self.Tmenu = pygame.transform.scale(TmenuImg, (round(WTmenuImg*size*Wres*0.85), 
                                                        round(HTmenuImg*size*Hres*0.55)))
        self.xa, self.ya, self.wa, self.ha = self.Iarcher.get_rect() #Archer
        self.xc, self.yc, self.wc, self.hc = self.Icannon.get_rect() #Cannon
        self.xm, self.ym, self.wm, self.hm = self.Imagic.get_rect() #Magician
        self.xt, self.yt, self.wt, self.ht = self.Tmenu.get_rect() #Wooden Background
        self.xa, self.ya = (width/10, height/1.1764)
        self.xc, self.yc = (width/5, height/1.1764)
        self.xm, self.ym = (width/3.333, height/1.1764)
        self.xt, self.yt = (width/20, height/1.25)
        self.recta = pygame.Rect(self.xa, self.ya, self.wa, self.ha)
        self.rectc = pygame.Rect(self.xc, self.yc, self.wc, self.hc)
        self.rectm = pygame.Rect(self.xm, self.ym, self.wm, self.hm)
        self.rectt = pygame.Rect(self.xt, self.yt, self.wt, self.ht)
        self.clicked = False
        self.delay = True
        self.tpos = tpos
        self.x, self.y = tpos
        self.font = pygame.font.SysFont("Verdana", 20)
        self.font2 = pygame.font.SysFont("Verdana", 15)
        self.text = self.font.render(text, 1, white)
        self.xT, self.yT = (width/6.666, height/1.333)
        self.xca, self.yca = (width/10, height/1.05263158)
        self.xcc, self.ycc = (width/5, height/1.05263158)
        self.xcm, self.ycm = (width/3.333, height/1.05263158)
        self.text2 = self.font2.render('1', 1, white)
        self.s = s #Clicked sign
        Tmenus.add(self)

    def update(self, events, mouse):
        global money
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.delay == True: #Prevent from not opening
                    self.delay = False
                else:
                    if self.recta.collidepoint(event.pos): #Archer icon clicked
                        clicksound.play()
                        if money >= Tacost: #If player can afford the tower
                            self.s.kill() #Kill the clicked sign
                            self.clicked = True
                            money -= Tacost #Cost
                            self.archer = Archer(self.tpos, 1) #Archer
                    elif self.rectc.collidepoint(event.pos): #Cannon icon clicked
                        clicksound.play()
                        if money >= Tccost:
                            self.s.kill()
                            self.clicked = True
                            money -= Tccost
                            self.cannon = Cannon(self.tpos, 1)
                    elif self.rectm.collidepoint(event.pos): #Magician icon clicked
                        clicksound.play()
                        if money >= Tmcost:
                            self.s.kill()
                            self.clicked = True
                            money -= Tmcost
                            self.magician = Magician(self.tpos, 1)
                    elif self.rectt.collidepoint(event.pos): #Wooden Background clicked
                        pass
                    else:
                        self.clicked = True
                    if self.clicked == True: #When the menu is opened and the player clicks other place
                        self.clicked = False
                        for i in Tmenus:
                            i.kill()
        screen.blit(self.Tmenu, (self.xt, self.yt))
        if self.recta.collidepoint(mouse): #Hovering archer icon
            pygame.draw.rect(screen, yellow, [self.xa-5, self.ya-5, self.wa+10, self.ha+10]) #Yellow highlight
            surface = pygame.Surface((Arange * 4, Arange * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (Arange, Arange), Arange, 0) #Range
            screen.blit(surface, (self.x - Arange + (WITarcher/2), self.y - Arange + (HITarcher/2)))
        if self.rectc.collidepoint(mouse): #Hovering cannon icon
            pygame.draw.rect(screen, yellow, [self.xc-5, self.yc-5, self.wc+10, self.hc+10])
            surface = pygame.Surface((Crange * 4, Crange * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (Crange, Crange), Crange, 0)
            screen.blit(surface, (self.x - Crange + (WITarcher/2), self.y - Crange + (HITarcher/2)))
        if self.rectm.collidepoint(mouse): #Hovering magician icon
            pygame.draw.rect(screen, yellow, [self.xm-5, self.ym-5, self.wm+10, self.hm+10])
            surface = pygame.Surface((Mrange * 4, Mrange * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (Mrange, Mrange), Mrange, 0)
            screen.blit(surface, (self.x - Mrange + (WITarcher/2), self.y - Mrange + (HITarcher/2)))
        screen.blit(self.Iarcher, (self.xa, self.ya))
        screen.blit(self.Icannon, (self.xc, self.yc))
        screen.blit(self.Imagic, (self.xm, self.ym))
        screen.blit(self.text, (self.xT, self.yT))
        #Change font color based on player's money
        if money >= Tacost: #If the player can buy the tower
            self.acost = self.font2.render(str(Tacost), 1, white) #Fonrcolor = white
        else:
            self.acost = self.font2.render(str(Tacost), 1, red) #If not, Fontcolor = red
        if money >= Tccost:
            self.ccost = self.font2.render(str(Tccost), 1, white)
        else:
            self.ccost = self.font2.render(str(Tccost), 1, red)
        if money >= Tmcost:
            self.mcost = self.font2.render(str(Tmcost), 1, white)
        else:
            self.mcost = self.font2.render(str(Tmcost), 1, red)
        screen.blit(self.acost, (self.xca, self.yca))
        screen.blit(self.ccost, (self.xcc, self.ycc))
        screen.blit(self.mcost, (self.xcm, self.ycm))

#############################################################################################
#Towers
#Archer
class Archer(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.x, self.y = position
        self.position = position
        self.size = size
        self.Itower = pygame.transform.scale(Itower, (round(WItower*size*Wres), 
                                                    round(HItower*size*Hres)))
        self.Iarcher = pygame.transform.scale(Sarcher, (round(WITarcher*size*Wres),
                                                        round(HITarcher*size*Hres)))
        self.xa, self.ya, self.wa, self.ha = self.Iarcher.get_rect()
        self.xt, self.yt, self.wt, self.ht = self.Itower.get_rect()
        self.xa = self.x
        self.ya = self.y - (height/4.8)
        self.xt = self.x - (width/100)
        self.yt = self.y - (height/12)
        self.recta = pygame.Rect(self.xa, self.ya, self.wa, self.ha)
        self.rectt = pygame.Rect(self.xt, self.yt, self.wt, self.ht)
        self.Tback = pygame.transform.scale(TmenuImg, (round(WTmenuImg*1*Wres*0.55), 
                                                    round(HTmenuImg*1*Hres*0.55)))
        self.xT, self.yT, self.wT, self.hT = self.Tback.get_rect()
        self.xT, self.yT = (width/20, height/1.25)
        self.rectT = pygame.Rect(self.xT, self.yT, self.wT, self.hT)
        self.ac = 0 #Archer counter
        self.clicked = False
        self.atkable = False #Enemy in range
        self.left = True #Facing left
        self.archerImg = Larcher_animation[:]
        self.range = Arange
        if self.position in corTowerbelow: #Whether the tower is in front or behind enemies
            Aarchers2.add(self)
        else:
            Aarchers.add(self)
        Atowers.add(self)

    def update(self, events, mouse):
        global playspeed
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.recta.collidepoint(mouse) or self.rectt.collidepoint(mouse):
                    clicksound.play()
                    for i in Tupgrades:
                        i.kill()
                    self.clicked = True
                    Tupgrade((0, 0), 1, 'Upgrade/Sell', self.position, 'archer', self) #Tower Upgrade
                else:
                    if not self.rectT.collidepoint(mouse):
                        self.clicked = False
        #Animation
        if pause == False:
            if self.atkable == True:
                self.ac += 1
                if self.ac >= 24/playspeed: #Playspeed affects animation speed
                    self.ac = 0
            else:
                self.ac = 0
        #Animation based on archer counter
        self.archer = pygame.transform.scale(self.archerImg[int((self.ac/playspeed)/(4/(playspeed**2)))], 
                                        (round(WITarcher*self.size*Wres),
                                        round(HITarcher*self.size*Hres)))
        screen.blit(self.Itower, (self.xt, self.yt))
        screen.blit(self.archer, (self.xa, self.ya))
        if self.clicked == True: #Show range when clicked
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0) #Range
            screen.blit(surface, (self.x - self.range + (WITarcher/2), self.y - self.range + (HITarcher/2)))

    def attack(self, enemies, defence):
        global money
        self.atkable = False #Enemy in range
        self.clsEnemy = [] #Close enemy
        #Calculate distance between every enemy
        for i in enemies: 
            x = i.x
            y = i.y
            d = math.sqrt((self.x + self.wa/2 - i.image.get_width()/2 - x)**2 + 
                          (self.y + self.ha/2 + self.ht/2 - i.image.get_height()/2 - y)**2) 
            if d < self.range: #If the enemy is in the range
                self.atkable = True
                self.clsEnemy.append(i)

        self.clsEnemy.sort(key=lambda x: x.path_pos)
        self.clsEnemy = self.clsEnemy[::-1]
        if len(self.clsEnemy) > 0: #If there is enemy in range
            self.fstEnemy = self.clsEnemy[0] #Attack the closest enemy
            if self.ac == int(23/playspeed): #When done doing animation
                archersound.play() #Sound effect
                self.killed, self.enemy_money = self.fstEnemy.hit(Adamage, defence) #Attack enemy
                if self.killed == True: #If successfully killed, get money
                    money += self.enemy_money
                    enemies.remove(self.fstEnemy)
            #Turn based on the enemy's position
            if self.fstEnemy.x > self.x and not(self.left): #Left
                self.left = True
                for x, img in enumerate(self.archerImg):
                    self.archerImg[x] = pygame.transform.flip(img, True, False)
            elif self.left and self.fstEnemy.x < self.x: #Right
                self.left = False
                for x, img in enumerate(self.archerImg):
                    self.archerImg[x] = pygame.transform.flip(img, True, False)
#Cannon
class Cannon(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.x, self.y = position
        self.position = position
        self.size = size
        self.Itower = pygame.transform.scale(Itower, (round(WItower*size*Wres), 
                                                    round(HItower*size*Hres)))
        self.Icannon = pygame.transform.scale(Scannon, (round(WITcannon*size*Wres),
                                                        round(HITcannon*size*Hres)))
        self.xc, self.yc, self.wc, self.hc = self.Icannon.get_rect()
        self.xt, self.yt, self.wt, self.ht = self.Itower.get_rect()
        self.xc = self.x
        self.yc = self.y - (height/4.8)
        self.xt = self.x - (width/100)
        self.yt = self.y - (height/12)
        self.rectc = pygame.Rect(self.xc, self.yc, self.wc, self.hc)
        self.rectt = pygame.Rect(self.xt, self.yt, self.wt, self.ht)
        self.Tback = pygame.transform.scale(TmenuImg, (round(WTmenuImg*1*Wres*0.55), 
                                                    round(HTmenuImg*1*Hres*0.55)))
        self.xT, self.yT, self.wT, self.hT = self.Tback.get_rect()
        self.xT, self.yT = (width/20, height/1.25)
        self.rectT = pygame.Rect(self.xT, self.yT, self.wT, self.hT)
        self.cc = 0 #Cannon counter
        self.cmove = 0 #Cannon movement for animation
        self.clicked = False
        self.atkable = False
        self.left = True
        self.cannonImg = Lcannon_animation[:]
        self.range = Crange
        if self.position in corTowerbelow:
            Acannons2.add(self)
        else:
            Acannons.add(self)
        Atowers.add(self)
    def update(self, events, mouse):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rectc.collidepoint(mouse) or self.rectt.collidepoint(mouse):
                    clicksound.play()
                    for i in Tupgrades:
                        i.kill()
                    self.clicked = True
                    Tupgrade((0, 0), 1, 'Upgrade/Sell', self.position, 'cannon', self)
                else:
                    if not self.rectT.collidepoint(mouse):
                        self.clicked = False
        if pause == False:
            if self.atkable == True:
                self.cc += 1
                if self.cc == 32/playspeed: #Moves back slightly when firing
                    self.cmove = width/100
                if self.cc >= 48/playspeed:
                    self.cmove = 0
                    self.cc = 0
            else:
                self.cc = 0
        self.cannon = pygame.transform.scale(self.cannonImg[int((self.cc/playspeed)/(8/(playspeed**2)))], 
                                        (round(WITcannon*self.size*Wres),
                                        round(HITcannon*self.size*Hres)))
        screen.blit(self.Itower, (self.xt, self.yt))
        #Move differently based on whether the cannon is facing left or right
        if self.left == True: 
            screen.blit(self.cannon, (self.xc - self.cmove, self.yc))
        else:
            screen.blit(self.cannon, (self.xc + self.cmove, self.yc))
        if self.clicked == True:
            surface = pygame.Surface((Crange * 4, Crange * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (Crange, Crange), Crange, 0)
            screen.blit(surface, (self.x - Crange + (WITcannon/2), self.y - Crange + (HITcannon/2)))
    def attack(self, enemies, defence):
        global money
        self.atkable = False
        self.clsEnemy = []
        for i in enemies:
            x = i.x
            y = i.y

            d = math.sqrt((self.x + self.wc/2 - i.image.get_width()/2 - x)**2 + 
                          (self.y + self.hc/2 + self.ht/2 - i.image.get_height()/2 - y)**2)
            if d < self.range:
                self.atkable = True
                self.clsEnemy.append(i)

        self.clsEnemy.sort(key=lambda x: x.path_pos)
        self.clsEnemy = self.clsEnemy[::-1]
        #Cannon hits 3 closest enemy
        if len(self.clsEnemy) > 0:
            self.fstEnemy = self.clsEnemy[0]
            try: #If there is second enemy, add it to closest enemy
                self.secEnemy = self.clsEnemy[1]
            except IndexError: #Pass if there are none
                self.secEnemy = None
            try: #If there is third enemy, add it to closest enemy
                self.thiEnemy = self.clsEnemy[2]
            except IndexError: #Pass if there are none
                self.thiEnemy = None
            if self.cc == int(47/playspeed):
                cannonsound.play()
                self.killed, self.enemy_money = self.fstEnemy.hit(Cdamage, defence) #1st enemy
                if self.killed == True:
                    money += self.enemy_money
                    enemies.remove(self.fstEnemy)
                if self.secEnemy != None: #Attack 2nd enemy with 50% damage
                    self.killed, self.enemy_money = self.secEnemy.hit(Cdamage*0.5, defence) 
                    if self.killed == True:
                        money += self.enemy_money
                        enemies.remove(self.secEnemy)
                if self.thiEnemy != None: #Attack 3rd enemy with 50% damage
                    self.killed, self.enemy_money = self.thiEnemy.hit(Cdamage*0.5, defence) 
                    if self.killed == True:
                        money += self.enemy_money
                        enemies.remove(self.thiEnemy)

            if self.fstEnemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.cannonImg):
                    self.cannonImg[x] = pygame.transform.flip(img, True, False)
            elif self.left and self.fstEnemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.cannonImg):
                    self.cannonImg[x] = pygame.transform.flip(img, True, False)
#Magician
class Magician(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.x, self.y = position
        self.position = position
        self.size = size
        self.Itower = pygame.transform.scale(Itower, (round(WItower*size*Wres), 
                                                    round(HItower*size*Hres)))
        self.Imagician = pygame.transform.scale(Smagician, (round(WITmagician*size*Wres),
                                                        round(HITmagician*size*Hres)))
        self.xm, self.ym, self.wm, self.hm = self.Imagician.get_rect()
        self.xt, self.yt, self.wt, self.ht = self.Itower.get_rect()
        self.xm = self.x
        self.ym = self.y - (height/4.8)
        self.xt = self.x - (width/100)
        self.yt = self.y - (height/12)
        self.rectm = pygame.Rect(self.xm, self.ym, self.wm, self.hm)
        self.rectt = pygame.Rect(self.xt, self.yt, self.wt, self.ht)
        self.Tback = pygame.transform.scale(TmenuImg, (round(WTmenuImg*1*Wres*0.55), 
                                                    round(HTmenuImg*1*Hres*0.55)))
        self.xT, self.yT, self.wT, self.hT = self.Tback.get_rect()
        self.xT, self.yT = (width/20, height/1.25)
        self.rectT = pygame.Rect(self.xT, self.yT, self.wT, self.hT)
        self.mc = 0 #Magician counter
        self.clicked = False
        self.atkable = False
        self.left = True
        self.magicianImg = Lmagician_animation[:]
        self.range = Mrange
        if self.position in corTowerbelow:
            Amagicians2.add(self)
        else:
            Amagicians.add(self)
        Atowers.add(self)
    def update(self, events, mouse):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rectm.collidepoint(mouse) or self.rectt.collidepoint(mouse):
                    clicksound.play()
                    for i in Tupgrades:
                        i.kill()
                    self.clicked = True
                    Tupgrade((0, 0), 1, 'Upgrade/Sell', self.position, 'magician', self)
                else:
                    if not self.rectT.collidepoint(mouse):
                        self.clicked = False
        if pause == False:
            if self.atkable == True:
                self.mc += 1
                if self.mc >= 36/playspeed:
                    self.mc = 0
            else:
                self.mc = 0
        self.magician = pygame.transform.scale(self.magicianImg[int((self.mc/playspeed)/(6/playspeed**2))], 
                                        (round(WITmagician*self.size*Wres),
                                        round(HITmagician*self.size*Hres)))
        screen.blit(self.Itower, (self.x - (width/100), self.y - (height/12)))
        screen.blit(self.magician, (self.x, self.y - (height/4.8)))
        if self.clicked == True:
            surface = pygame.Surface((Mrange * 4, Mrange * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (Mrange, Mrange), Mrange, 0)
            screen.blit(surface, (self.x - Mrange + (WITcannon/2), self.y - Mrange + (HITcannon/2)))
    
    def attack(self, enemies, defence):
        global money
        self.atkable = False
        self.clsEnemy = []
        for i in enemies:
            x = i.x
            y = i.y

            d = math.sqrt((self.x + self.wm/2 - i.image.get_width()/2 - x)**2 + 
                          (self.y + self.hm/2 + self.ht/2 - i.image.get_height()/2 - y)**2)
            if d < self.range:
                self.atkable = True
                self.clsEnemy.append(i)

        self.clsEnemy.sort(key=lambda x: x.path_pos)
        self.clsEnemy = self.clsEnemy[::-1]
        if len(self.clsEnemy) > 0:
            self.fstEnemy = self.clsEnemy[0]
            if self.mc == int(35/playspeed):
                magiciansound.play()
                self.killed, self.enemy_money = self.fstEnemy.hit(Mdamage, defence)
                if self.killed == True:
                    money += self.enemy_money
                    enemies.remove(self.fstEnemy)

            if self.fstEnemy.x > self.x and not(self.left):
                self.left = True
                for x, img in enumerate(self.magicianImg):
                    self.magicianImg[x] = pygame.transform.flip(img, True, False)
            elif self.left and self.fstEnemy.x < self.x:
                self.left = False
                for x, img in enumerate(self.magicianImg):
                    self.magicianImg[x] = pygame.transform.flip(img, True, False)
#################################################################################################
#Tower Upgrade
class Tupgrade(pygame.sprite.Sprite):
    def __init__(self, position, size, text, tpos, type, s):
        super().__init__()
        self.size = size
        self.type = type
        if type == 'archer': #If player clicked archer, use archer icon
            self.Image = pygame.transform.scale(Iarcher, (round(WIarcher*size*Wres), 
                                                            round(HIarcher*size*Hres)))
        elif type == 'cannon': #Cannon
            self.Image = pygame.transform.scale(Icannon, (round(WIcannon*size*Wres), 
                                                            round(HIcannon*size*Hres)))
        elif type == 'magician': #Magician
            self.Image = pygame.transform.scale(Imagic, (round(WImagic*size*Wres), 
                                                            round(HImagic*size*Hres)))
        self.Isell = pygame.transform.scale(moneyImg, (round(WmoneyImg*size*Wres),  #coin
                                                        round(HmoneyImg*size*Hres)))
        self.Tback = pygame.transform.scale(TmenuImg, (round(WTmenuImg*size*Wres*0.55), #Background
                                                        round(HTmenuImg*size*Hres*0.55)))
        self.x, self.y, self.w, self.h = self.Image.get_rect() #Icon
        self.xs, self.ys, self.ws, self.hs = self.Isell.get_rect() #Sell
        self.xt, self.yt, self.wt, self.ht = self.Tback.get_rect() #Background
        self.x, self.y = (width/10, height/1.1764)
        self.xs, self.ys = (width/5, height/1.1764)
        self.xt, self.yt = (width/20, height/1.25)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.rects = pygame.Rect(self.xs, self.ys, self.ws, self.hs)
        self.rectt = pygame.Rect(self.xt, self.yt, self.wt, self.ht)
        self.clicked = False
        self.delay = True
        self.tpos = tpos #Tower position
        self.xpos, self.ypos = tpos
        self.font = pygame.font.SysFont("Verdana", 20)
        self.font2 = pygame.font.SysFont("Verdana", 15)
        self.text = self.font.render(text, 1, white)
        self.xT, self.yT = (width/7, height/1.333) #Text
        self.xsc, self.ysc = (width/5, height/1.05263158) #Sell cost
        self.xc, self.yc = (width/10, height/1.05263158) #cost
        self.text2 = self.font2.render('1', 1, white)
        self.s = s
        Tupgrades.add(self)

    def update(self, events, mouse):
        global money, Uarcher, Ucannon, Umagician, Adamage, Cdamage, Mdamage, TUacost, TUccost, TUmcost
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.delay == True:
                    self.delay = False
                else:
                    #Upgrade
                    if self.rect.collidepoint(event.pos):
                        clicksound.play()
                        if self.type == 'archer': #If player clicked archer
                            if money >= TUacost: #If player have more money then upgrade cost
                                money -= TUacost #Take away money
                                TUacost += 30 #Increase upgrade cost
                                Uarcher += 1 #Increase number of upgrades
                                Adamage = Adamage + (Uarcher*3) #Increase damage based on number of upgrades
                        elif self.type == 'cannon':
                            if money >= TUccost:
                                money -= TUccost
                                TUccost += 40
                                Ucannon += 1
                                Cdamage = Cdamage + (Ucannon*5)
                        elif self.type == 'magician':
                            if money >= TUmcost:
                                money -= TUmcost
                                TUmcost += 30
                                Umagician += 1
                                Mdamage = Mdamage + (Umagician*8)
                    #Sell
                    elif self.rects.collidepoint(event.pos): 
                        clicksound.play()
                        if self.type == 'archer': #If player clicked archer
                            money += Tacost/2 #Get money by the half of original cost
                            self.s.kill()
                            for i in Tupgrades:
                                i.kill()
                            preTower(self.tpos, 1) #Regenerate pre tower/sing
                        elif self.type == 'cannon':
                            money += Tccost/2
                            self.s.kill()
                            for i in Tupgrades:
                                i.kill()
                            preTower(self.tpos, 1)
                        elif self.type == 'magician':
                            money += Tmcost/2
                            self.s.kill()
                            for i in Tupgrades:
                                i.kill()
                            preTower(self.tpos, 1)
                    elif self.rectt.collidepoint(event.pos): #If clicked the background
                        pass
                    else:
                        self.clicked = True
                    if self.clicked == True:
                        self.clicked = False
                        for i in Tupgrades:
                            i.kill()
        screen.blit(self.Tback, (self.xt, self.yt))
        if self.rect.collidepoint(mouse): #When hovered, highlight yellow
            pygame.draw.rect(screen, yellow, [self.x-5, self.y-5, self.w+10, self.h+10])
        if self.rects.collidepoint(mouse):
            pygame.draw.rect(screen, yellow, [self.xs-5, self.ys-5, self.ws+10, self.hs+10])
        screen.blit(self.Image, (self.x, self.y))
        pygame.draw.rect(screen, green, self.rects)
        screen.blit(self.Isell, (self.xs, self.ys))
        screen.blit(self.text, (self.xT, self.yT))
        #Change font color based on player's money
        if self.type == 'archer':
            if money >= TUacost:
                self.Ucost = self.font2.render(str(TUacost), 1, white)
            else:
                self.Ucost = self.font2.render(str(TUacost), 1, red)
            scost = self.font2.render(str(int(Tacost/2)), 1, yellow)
            self.numUpgrade = self.font2.render(str(Uarcher), 1, purple)
        elif self.type == 'cannon':
            if money >= TUccost:
                self.Ucost = self.font2.render(str(TUccost), 1, white)
            else:
                self.Ucost = self.font2.render(str(TUccost), 1, red)
            scost = self.font2.render(str(int(Tccost/2)), 1, yellow)
            self.numUpgrade = self.font2.render(str(Ucannon), 1, purple)
        elif self.type == 'magician':
            if money >= TUmcost:
                self.Ucost = self.font2.render(str(TUmcost), 1, white)
            else:
                self.Ucost = self.font2.render(str(TUmcost), 1, red)
            scost = self.font2.render(str(int(Tccost/2)), 1, yellow)
            self.numUpgrade = self.font2.render(str(Umagician), 1, purple)
        screen.blit(self.Ucost, (self.xc, self.yc))
        screen.blit(scost, (self.xsc, self.ysc))
        screen.blit(self.numUpgrade, (self.xc, self.y))
############################################################################################
#Pause Button
class PlayPause(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.playImg = pygame.transform.scale(butPlay, (round(WbutPlay*size*Wres), #Play button
                                                        round(HbutPlay*size*Hres)))
        self.pauseImg = pygame.transform.scale(butPause, (round(WbutPause*size*Wres), #Pause button
                                                        round(HbutPause*size*Hres)))
        self.x, self.y, self.w, self.h = self.playImg.get_rect() #Play
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.x2, self.y2, self.w2, self.h2 = self.pauseImg.get_rect() #Pause
        self.x2, self.y2 = position
        self.rect2 = pygame.Rect(self.x2, self.y2, self.w2, self.h2)
        self.position = position
        Gplaypause.add(self)

    def update(self, events, mouse):
        global pause
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos) or self.rect2.collidepoint(event.pos):
                    clicksound.play()
                    if pause == True: #Unpause when paused
                        pause = False
                    else: #Pause when unpaused
                        pause = True
        if self.rect.collidepoint(mouse): #Highlight yellow when hovered
            pygame.draw.rect(screen, yellow, [self.x-5, self.y-5, self.w+10, self.h+10])
        if pause == True: #When paused draw play button
            screen.blit(self.playImg, (self.x, self.y))
        else: #When unpaused draw pause button
            screen.blit(self.pauseImg, (self.x2, self.y2))
#Play Speed Button
class PlaySpeed(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.speedImg = pygame.transform.scale(butSpeed, (round(WbutSpeed*size*Wres), #Normal
                                                        round(HbutSpeed*size*Hres)))
        self.clickedImg = pygame.transform.scale(butSpeed2, (round(WbutSpeed*size*Wres), #Clicked
                                                        round(HbutSpeed*size*Hres)))
        self.x, self.y, self.w, self.h = self.speedImg.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        Gplayspeed.add(self)

    def update(self, events, mouse):
        global playspeed
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    clicksound.play()
                    if playspeed == 1: #If play speed is 1x turn to 2x
                        playspeed = 2
                    else: #If play speed is 2x turn to 1x
                        playspeed = 1
        if self.rect.collidepoint(mouse): #highlight yellow when hovered
            pygame.draw.rect(screen, yellow, [self.x-5, self.y-5, self.w+10, self.h+10])
        if playspeed == 1: #When speed is 1x draw normal
            screen.blit(self.speedImg, (self.x, self.y))
        else: #When speed is 2x draw clicked
            screen.blit(self.clickedImg, (self.x, self.y))
#Text
class Text(pygame.sprite.Sprite):
    def __init__(self, position, text, size, group):
        super().__init__()
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, white)
        self.x, self.y = position
        self.position = position
        group.add(self)

    def update(self):
        screen.blit(self.text_render, (self.x, self.y))
#Button
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, bg, proc, group):
        super().__init__()
        self.bg = bg
        self.proc = proc
        self.font = pygame.font.SysFont("Verdana", size)
        self.text_render = self.font.render(text, 1, white)
        self.image = self.text_render
        self.x, self.y, self.w, self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        group.add(self)

    def update(self, events, mouse):
        global visible
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    clicksound.play()
                    self.proc()
                    visible = False
        if self.rect.collidepoint(mouse):
            pygame.draw.rect(screen, Dgray, [self.x, self.y, self.w, self.h])
        else:
            pygame.draw.rect(screen, self.bg, [self.x, self.y, self.w, self.h])
#Open settings in game
class Settings(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.settingImg = pygame.transform.scale(butSettings, (round(WbutSettings*size*Wres),
                                                        round(HbutSettings*size*Hres)))
        self.x, self.y, self.w, self.h = self.settingImg.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.clicked = False
        Gsettings.add(self)

    def update(self, events, mouse):
        if self.clicked == True: #Transparent background when clicked
            surface = pygame.Surface((width/1.1111, height), pygame.SRCALPHA, 32)
            pygame.draw.rect(surface, (128, 128, 128, 200), [width/10, height/6, width/1.25, height/1.2])
            screen.blit(surface, (0, 0))
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    clicksound.play()
                    if self.clicked == False: #Create buttons when clicked
                        global mVolume
                        bVol = Button((width/2.3, height - (4*height/10)), "Volume", fontsize, Lgray, self.hi, GBsettings)
                        bPlus = Button((width/1.33, height - (3*height/10)), "+", fontsize, Lgray, self.plus, GBsettings)
                        bMinus = Button((width/4, height - (3*height/10)), "-", fontsize, Lgray, self.minus, GBsettings)
                        bBack = Button((width/2.2, height - (2*height/10)), "Back", fontsize, Lgray, self.back, GBsettings)
                        bquit = Button((round(width/2.6315), round(height - (7*height/10))), 'Main Menu', fontsize, Lgray, self.menu, GBsettings)
                        VolumeBar((width/3.3333, height/1.4117), Lgray)
                        self.clicked = True
                    else: #Close if already clicked
                        self.back()
                        self.clicked = False
            elif event.type == pygame.KEYDOWN: #Also when escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    clicksound.play()
                    if self.clicked == False:
                        global mVolume
                        bVol = Button((width/2.3, height - (4*height/10)), "Volume", fontsize, Lgray, self.hi, GBsettings)
                        bPlus = Button((width/1.33, height - (3*height/10)), "+", fontsize, Lgray, self.plus, GBsettings)
                        bMinus = Button((width/4, height - (3*height/10)), "-", fontsize, Lgray, self.minus, GBsettings)
                        bBack = Button((width/2.2, height - (2*height/10)), "Back", fontsize, Lgray, self.back, GBsettings)
                        VolumeBar((width/3.3333, height/1.4117), Lgray)
                        self.clicked = True
                    else:
                        self.back()
                        self.clicked = False
        screen.blit(self.settingImg, (self.x, self.y))

    #Decrease volume
    def minus(self):
        global mVolume
        if round(mVolume, 1) > 0:
            mVolume = mVolume - 0.1
        for i in sounds:
            i.set_volume(mVolume)
        for i in Gvolumebar:
            i.kill()
        pygame.mixer.music.set_volume(mVolume)
        VolumeBar((width/3.3333, height/1.4117), Lgray)

    #Increase volume
    def plus(self):
        global mVolume
        if round(mVolume, 1) < 1:
            mVolume = mVolume + 0.1
        for i in sounds:
            i.set_volume(mVolume)
        for i in Gvolumebar:
            i.kill()
        pygame.mixer.music.set_volume(mVolume)
        VolumeBar((width/3.3333, height/1.4117), Lgray)

    #Close settings
    def back(self):
        self.clicked = False
        for i in GBsettings:
            i.kill()
        for i in Gvolumebar:
            i.kill()

    #HI
    def hi(self):
        print('lol')

    #Resest and go back to main menu
    def menu(self):
        global money, life, Uarcher, Ucannon, Umagician, TUacost, TUccost, TUmcost, playspeed, pause
        self.clicked = False
        lsprite = [Gvolumebar, GBsettings, GTsettings, GTgameover, preTs, Tmenus, Aarchers,
                   Acannons, Amagicians, Aarchers2, Acannons2, Atowers, Amagicians2, Tupgrades,
                   Genemy, Gplaypause, Gplayspeed, GBgameover, Gsettings]
        for i in lsprite:
            for j in i:
                j.kill()
        money = 300
        life = 5
        Uarcher = 0
        Ucannon = 0
        Umagician = 0
        TUacost = 50
        TUccost = 60
        TUmcost = 60
        playspeed = 1
        pause = True

        import Main_menu
        Main_menu.Mainmenu()
############################################################################################
#Difficulty - Easy = 0% defence, Normal = 30% defence, Hard = 50% defence
class difficulty:
    def GameHard(self):
        global defence
        g = Game()
        defence = 0.5
        g.load(defence)
    def GameNormal(self):
        global defence
        g = Game()
        defence = 0.7
        g.load(defence)
    def GameEasy(self):
        global defence
        g = Game()
        defence = 1
        g.load(defence)
#Main Game
class Game():
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.moneyImg = pygame.transform.scale(moneyImg, (round(WmoneyImg*0.5*Wres), #Coin
                                                        round(HmoneyImg*0.5*Hres)))
        self.lifeImg = pygame.transform.scale(lifeImg, (round(WlifeImg*0.5*Wres),  #Heart
                                                        round(HlifeImg*0.5*Hres)))
        self.wavec = 0 #Wave counter
        self.wave = waves
        self.currentwave = self.wave[self.wavec]
        self.timer = time.time() #Enemy spawn timer
    
    #Graphics of the game
    def draw(self, events, mouse):
        global mVolume
        #Background
        screen.blit(bgImg, (0, 0))
        #Sign
        preTs.update(events, mouse)
        #Towers behind enemy
        Aarchers.update(events, mouse)
        Acannons.update(events, mouse)
        Amagicians.update(events, mouse)
        #Enemy
        Genemy.update()
        #Towers front of enemy
        Aarchers2.update(events, mouse)
        Acannons2.update(events, mouse)
        Amagicians2.update(events, mouse)
        #Tower menu, upgrade
        Tmenus.update(events, mouse)
        Tupgrades.update(events, mouse)
        #Buttons
        Gplaypause.update(events, mouse)
        Gplayspeed.update(events, mouse)
        Gsettings.update(events, mouse)
        GBsettings.update(events, mouse)
        GBsettings.draw(screen)
        GTsettings.update()
        Gvolumebar.update(mVolume)
        GBgameover.update(events, mouse)
        GBgameover.draw(screen)
        GTgameover.update()
        #money, life
        self.data()
    #Moeny, Life
    def data(self):
        global money, life
        self.moneytxt = self.font.render(str(int(money)), 1, yellow)
        self.lifetxt = self.font.render(str(life), 1, red)
        screen.blit(self.moneytxt, (width - width/10, height/24))
        screen.blit(self.moneyImg, (width - (1.5*width/10), height/36))
        screen.blit(self.lifetxt, (width - width/10, height/11))
        screen.blit(self.lifeImg, (width - (1.5*width/10), height/14))
    #Loading screen
    def load(self, defence):
        l = [] #list
        t = [] #list 2 (just a random variable name)
        speed = width/33.33 #Cloud speed
        Lcc1 = loading((5*-width, 1.8*-height), 5, speed) #Cloud 1

        #More clouds
        for i in range(3):
            l.append('Lc' + str(i))
            l[i] = loading((2*(width/(random.randint(400, 900)/-500)) - 
                            width - 2*width, height/(i+1)),2.5, speed)

        #Ginormous clouds
        Lcc2 = loading((2*(width/-1.2) - (2*width), height/-2), 2.5, speed)
        Lcc3 = loading((2*(width/-5) - (2*width), height/-2), 2.5, speed)
        Lcc4 = loading((2*(width/-2) - (2*width), height/-2), 2.5, speed)

        #Creating pre towers/signs
        for i in range(len(corTower)):
            t.append('pT' + str(i))
            t[i] = preTower(corTower[i], 1)

        x = 0
        #Stop when cloud get out the screen
        while x < width * 6:
            events = pygame.event.get()
            for event in events: 
                if event.type == QUIT: 
                    pygame.quit() 
                    sys.exit()
            screen.fill(sky)
            clouds.update()
            if x > width * 3: #When the clouds cover the screen draw the background + signs
                screen.blit(bgImg, (0, 0))
                preTs.update(events, (-1000, -1000))
            loads.update()
            x += speed
            pygame.display.update()
            clock.tick(fps)
        for i in loads:
            i.kill()
        for i in clouds:
            i.kill()
        playp = PlayPause((width/1.1235, height/1.2244), 1) #Pause button
        plays = PlaySpeed((width/1.282, height/1.2244), 1) #Play speed button
        sett = Settings((width/100, height/60), 1) #Settings button
        g = Game()
        g.play(defence)

    #Gameplay
    def play(self, defence):
        global life, pause, playspeed
        playing = True
        while playing:
            events = pygame.event.get()
            for event in events: 
                if event.type == QUIT: 
                    pygame.quit() 
                    sys.exit()
            mouse = pygame.mouse.get_pos()
            self.draw(events, mouse) #Graphics

            if pause == False: #If unpaused
                if time.time() - self.timer >= random.randrange(1,6)/3: #Enemy spawn rate
                    self.timer = time.time()
                    self.spawn() #Spawn enemies in order one by one

                dest = [] #Destination
                for i in Genemy:
                    i.move(playspeed) #Move enemies
                    if i.x > round(width/0.9852): #When enemies reach the last point, life - 1
                        dest.append(i)
                for i in dest:
                    life -= 1
                    dest.remove(i)
                    i.kill()
                    if life <= 0: #If life = 0, lose screen
                        pause = True
                        self.gameover('lose')
                #Make the towers attack
                for i in Atowers:
                    i.attack(Genemy, defence)
                
            pygame.display.update()
            clock.tick(fps)
    #Spawn enemies
    def spawn(self):
        global pause
        if sum(self.currentwave) == 0: #When there are no enemies left
            if len(Genemy) == 0: #When all enemies are dead, next wave
                self.wavec += 1
                if self.wavec == 15: #When the play beats wave 15, they win
                    pause = True
                    self.gameover('win')
                try:
                    self.currentwave = self.wave[self.wavec]
                except IndexError:
                    pass
                pause = True
        else:
            #Upcoming enemy based on the settings. Health, speed, money, image, size
            self.upcoming = [Enemy(30*(self.wavec+1), 1.2 + (random.randint(1, (self.wavec+1)*8))/100, 
                                   10 + self.wavec, triangleImg, 1),
                            Enemy(40*(self.wavec+1.5), 1 + (random.randint(1, (self.wavec+1)*6))/100, 
                                  20 + self.wavec, squareImg, 1),
                            Enemy(50*(self.wavec+2), 1 + (random.randint(1, (self.wavec+1)*4))/100, 
                                  30 + self.wavec, hexagonImg, 1),
                            Enemy(2000*((self.wavec+1)/5)*5, 1 + ((random.randint(1, (self.wavec+1)*2))/100),
                                  200 * ((self.wavec+1)/5)*5, triangleImg, 2),
                            #After 5 waves
                            Enemy(40*(self.wavec+1), 1.2 + (random.randint(30, (self.wavec+30)*2))/100, 
                                   15 + self.wavec, triangleImg, 1),
                            Enemy(50*(self.wavec+1.5), 1 + (random.randint(24, (self.wavec+24)*2))/100, 
                                  25 + self.wavec, squareImg, 1),
                            Enemy(60*(self.wavec+2), 1 + (random.randint(15, (self.wavec+15)*2))/100, 
                                  35 + self.wavec, hexagonImg, 1),
                            Enemy(3000*((self.wavec+1)/5)*5, 1 + ((random.randint(10, (self.wavec+10)*2))/100),
                                  300 * ((self.wavec+1)/5)*5, squareImg, 2),
                            #After 10 waves
                            Enemy(60*(self.wavec+1), 1.2 + (random.randint(60, (self.wavec+60)*2))/100, 
                                   20 + self.wavec, triangleImg, 1),
                            Enemy(80*(self.wavec+1.5), 1 + (random.randint(50, (self.wavec+50)*2))/100, 
                                  30 + self.wavec, squareImg, 1),
                            Enemy(100*(self.wavec+2), 1 + (random.randint(30, (self.wavec+30)*2))/100, 
                                  40 + self.wavec, hexagonImg, 1),
                            Enemy(5000*((self.wavec+1)/5)*5, 1 + ((random.randint(20, int((self.wavec+20)*1.5)))/100),
                                  400 * ((self.wavec+1)/5)*5, hexagonImg, 2),
                            ]
            #Summon enemies one by one starting from the weakest
            for i in range(len(self.currentwave)):
                if self.currentwave[i] != 0:
                    Genemy.add(self.upcoming[i])
                    self.currentwave[i] -= 1
                    break
    #Gameover
    def gameover(self, game):
        if game == 'lose': #Print defeat when lost and vicroy when won
            Text((round(width/3.3333), 100), 'DEFEAT', round(width/10), GTgameover)
        else:
            Text((round(width/3.3333), 100), 'VICTORY', round(width/10), GTgameover)
        #Main menu button
        Button((round(width/2.6315), round(height - (3*height/10))), 'Main Menu', fontsize, Lgray, self.menu, GBgameover)
    #Reset and go back to the main menu
    def menu(self):
        global money, life, Uarcher, Ucannon, Umagician, TUacost, TUccost, TUmcost, playspeed, pause
        self.clicked = False
        lsprite = [Gvolumebar, GBsettings, GTsettings, GTgameover, preTs, Tmenus, Aarchers,
                   Acannons, Amagicians, Aarchers2, Acannons2, Atowers, Amagicians2, Tupgrades,
                   Genemy, Gplaypause, Gplayspeed, GBgameover, Gsettings]
        for i in lsprite:
            for j in i:
                j.kill()
        money = 300
        life = 5
        Uarcher = 0
        Ucannon = 0
        Umagician = 0
        TUacost = 50
        TUccost = 60
        TUmcost = 60
        playspeed = 1
        pause = True

        import Main_menu
        Main_menu.Mainmenu()