#Import
import pygame
from pygame.locals import *
import math
from Settings import *

#Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self, hp, speed, money, image, size):
        super().__init__()
        self.hp = hp
        self.hpbar = width/33.3333
        self.hprat = self.hpbar/self.hp
        self.speed = speed
        self.path = path
        self.size = size
        self.money = money
        self.image = pygame.transform.scale(image, (round(WsquareImg*size*Wres), 
                                                    round(HsquareImg*size*Hres)))
        self.x = self.path[0][0] #x-cord of 1st path
        self.y = self.path[0][1] #y-cord of 1st path
        self.d = 0 #Distance
        self.path_pos = 0 #Path position

    def update(self):
        screen.blit(self.image, (self.x - self.image.get_width()/2, 
                                 self.y - self.image.get_height()/2))
        #Health Bar
        self.currenthp = round(self.hprat*self.hp)
        pygame.draw.rect(screen, (red), (self.x - (width/33.3333), self.y - (height/8),
                                           self.hpbar, height/120))
        pygame.draw.rect(screen, (green), (self.x - (width/33.3333), self.y - (height/8),
                                           self.currenthp, height/120))
    
    def move(self, playspeed):
        #Calculating position
        x1, y1 = self.path[self.path_pos] #Starting position
        if self.path_pos + 1 >= len(self.path): #If there is not next position
            pass
        else:
            x2, y2 = self.path[self.path_pos+1] #Next position

        #Calculating moving distance
        #Distance between two positions
        d = ((x2-x1)*2, (y2-y1)*2)
        length = math.sqrt((d[0])**2 + (d[1])**2)
        d = (d[0]/length, d[1]/length)
        #Moving distance
        move_x, move_y = ((self.x + (d[0] * self.speed * playspeed)), 
                            (self.y + (d[1] * self.speed * playspeed)))
        self.x = move_x
        self.y = move_y

        #To next point
        if d[1] >= 0: # Moving down
            if self.x >= x2 and self.y >= y2:
                self.path_pos += 1
        else: #Moving up
            if self.x >= x2 and self.y <= y2:
                self.path_pos += 1

    #Damaged
    def hit(self, damage, defence):
        self.hp -= damage * defence #Tower damage
        if self.hp <= 0:
            self.kill()
            return True, self.money
        return False, 0