#Import
import pygame

#Screen Settings
width = 1000
height = 600
white = (255, 255, 255)
black = (  0,   0,   0)
sky = (126, 247, 227)
fps = 30

pygame.init()

screen = pygame.display.set_mode((width, height), 0, 32) 
clock = pygame.time.Clock()

#Images
Wres = width/1000 #Width resolution ratio
Hres = height/600 #Height resolution ratio
#Cloud
cloudImg = pygame.image.load('Assets/Cloud.png') 
Wcloud = cloudImg.get_rect().width
Hcloud = cloudImg.get_rect().height
#Title image
titleImg = pygame.image.load('Assets/Geometry Defence.png') 
Wtitle = titleImg.get_rect().width
Htitle = titleImg.get_rect().height
#Background
bgIm = pygame.image.load('Assets/background.png') 
WbgImg = bgIm.get_rect().width
HbgImg = bgIm.get_rect().height
bgImg = pygame.transform.scale(bgIm, (round(WbgImg*Wres), round(HbgImg*Hres)))
#Sign/Pre tower
preTImg = pygame.image.load('Assets/Pre Tower.png') 
WpreTImg = preTImg.get_rect().width
HpreTImg = preTImg.get_rect().height
#Sign with lights when hovered
preTImg2 = pygame.image.load('Assets/Pre Tower2.png') 
WpreTImg2 = preTImg2.get_rect().width
HpreTImg2 = preTImg2.get_rect().height
#Bow icon
Iarcher = pygame.image.load('Assets/Iarcher.png') 
WIarcher = Iarcher.get_rect().width
HIarcher = Iarcher.get_rect().height
#Cannon icon
Icannon = pygame.image.load('Assets/Icannon.png')
WIcannon = Icannon.get_rect().width
HIcannon = Icannon.get_rect().height
#Potion icon
Imagic = pygame.image.load('Assets/Imagic.png')
WImagic = Imagic.get_rect().width
HImagic = Imagic.get_rect().height
#Tower menu wooden background
TmenuImg = pygame.image.load('Assets/Tmenu.png')
WTmenuImg = TmenuImg.get_rect().width
HTmenuImg = TmenuImg.get_rect().height
#Coin
moneyImg = pygame.image.load('Assets/coin.png')
WmoneyImg = moneyImg.get_rect().width
HmoneyImg = moneyImg.get_rect().height
#Life/Heart
lifeImg = pygame.image.load('Assets/life.png')
WlifeImg = lifeImg.get_rect().width
HlifeImg = lifeImg.get_rect().height
#Tower
Itower = pygame.image.load('Assets/tower.png')
WItower = Itower.get_rect().width
HItower = Itower.get_rect().height
#Archer sprite
Sarcher = pygame.image.load('Assets/Sarcher.png') #Standing
Aarcher1 = pygame.image.load('Assets/Aarcher1.png') #Attacing
Aarcher2 = pygame.image.load('Assets/Aarcher2.png')
Aarcher3 = pygame.image.load('Assets/Aarcher3.png')
Aarcher4 = pygame.image.load('Assets/Aarcher4.png')
Aarcher5 = pygame.image.load('Assets/Aarcher5.png')
WITarcher = Sarcher.get_rect().width
HITarcher = Sarcher.get_rect().height
Larcher_animation = [Sarcher, Aarcher1, Aarcher2, Aarcher3, Aarcher4, Aarcher5] #List of attacking
#Cannon sprite
Scannon = pygame.image.load('Assets/Scannon.png')
Acannon1 = pygame.image.load('Assets/Acannon1.png')
Acannon2 = pygame.image.load('Assets/Acannon2.png')
Acannon3 = pygame.image.load('Assets/Acannon3.png')
Acannon4 = pygame.image.load('Assets/Acannon4.png')
Acannon5 = pygame.image.load('Assets/Acannon5.png')
WITcannon = Scannon.get_rect().width
HITcannon = Scannon.get_rect().height
Lcannon_animation = [Scannon, Acannon1, Acannon2, Acannon3, Acannon4, Acannon5]
#Magician sprite
Smagician = pygame.image.load('Assets/Smagician.png')
Amagician1 = pygame.image.load('Assets/Amagician1.png')
Amagician2 = pygame.image.load('Assets/Amagician2.png')
Amagician3 = pygame.image.load('Assets/Amagician3.png')
Amagician4 = pygame.image.load('Assets/Amagician4.png')
Amagician5 = pygame.image.load('Assets/Amagician5.png')
WITmagician = Smagician.get_rect().width
HITmagician = Smagician.get_rect().height
Lmagician_animation = [Smagician, Amagician1, Amagician2, Amagician3, Amagician4, Amagician5]
#Play button
butPlay = pygame.image.load('Assets/play.png')
WbutPlay = butPlay.get_rect().width
HbutPlay = butPlay.get_rect().height
#Pause button
butPause = pygame.image.load('Assets/pause.png')
WbutPause = butPause.get_rect().width
HbutPause = butPause.get_rect().height
#2x speed button
butSpeed = pygame.image.load('Assets/speed.png')
WbutSpeed = butSpeed.get_rect().width
HbutSpeed = butSpeed.get_rect().height
#Pressed 2x speed button
butSpeed2 = pygame.image.load('Assets/speed2.png')
#Enemies
triangleImg = pygame.image.load('Assets/triangle.png') #Triangle
squareImg = pygame.image.load('Assets/square.png') #Square
hexagonImg = pygame.image.load('Assets/hexagon.png') #Hexagon
WsquareImg = squareImg.get_rect().width
HsquareImg = squareImg.get_rect().height
#Settings image
butSettings = pygame.image.load('Assets/settings.png')
WbutSettings = butSettings.get_rect().width
HbutSettings = butSettings.get_rect().height

#Button Settings
#Color
Lgray = (170, 170, 170) #Light gray
Dgray = (100, 100, 100) #Dark gray
yellow = (255, 221, 0) #Yellow
red = (224, 16, 16) #Red
green = (98, 184, 33) #Green
purple = (108, 0, 150) #Purple
#Font Size
fontsize = round(width/25)
#Variables
visible = True 
construct = False

#Groups
#Main Menu
buttons = pygame.sprite.Group()
clouds = pygame.sprite.Group()
titles = pygame.sprite.Group()
shapes = pygame.sprite.Group()
texts = pygame.sprite.Group()
splashs = pygame.sprite.Group()
#Game
loads = pygame.sprite.Group()
preTs = pygame.sprite.Group()
#Towers
Tmenus = pygame.sprite.Group() #Tower menus
Aarchers = pygame.sprite.Group() #Archer sprite
Acannons = pygame.sprite.Group()
Amagicians = pygame.sprite.Group()
Aarchers2 = pygame.sprite.Group() #Towers in front of enemies
Acannons2 = pygame.sprite.Group()
Atowers = pygame.sprite.Group()
Amagicians2 = pygame.sprite.Group()
Tupgrades = pygame.sprite.Group()
#Enemy
Genemy = pygame.sprite.Group()
#Settings
Gplaypause = pygame.sprite.Group()
Gplayspeed = pygame.sprite.Group()
GTgameover = pygame.sprite.Group()
GBgameover = pygame.sprite.Group()
Gvolumebar = pygame.sprite.Group()
Gsettings = pygame.sprite.Group()
GBsettings = pygame.sprite.Group()
GTsettings = pygame.sprite.Group()

#Volume
mVolume = 0.5

#Coordinates
#path = [(-33, 286), (147, 302), (284, 156), 
        #(400, 141), (460, 200), (519, 417), 
        #(622, 444), (673, 401), (724, 271), 
        #(788, 243), (1020, 288)]
#Enemy pathway
path = [(round(-width/30), round(height/2.1)), (round(width/6.89), round(height/2)), (round(width/3.5), round(height/3.87)), 
        (round(width/2.5), round(height/4.25)), (round(width/2.17), round(height/3)), (round(width/1.9267), round(height/1.44)), 
        (round(width/1.6077), round(height/1.3483)), (round(width/1.4858), round(height/1.5)), (round(width/1.3812), round(height/2.2)), 
        (round(width/1.2658), round(height/2.45)), (round(width/0.9803), round(height/2.06))]
#corTower = [(12, 360), (76, 190), (266, 210),
            #(325, 42), (390, 397), (487, 118),
            #(550, 473), (553, 280), (685, 425),
            #(728, 147), (755, 302), (937, 183)]
#Tower coordinates
corTower = [(round(width/100), round(height/1.6666)), (round(width/13.3333), round(height/3.1579)), (round(width/3.7735), round(height/2.8571)),
            (round(width/3.0769), round(height/15)), (round(width/2.5641), round(height/1.5)), (round(width/2.0618), round(height/5)),
            (round(width/1.8182), round(height/1.2631)), (round(width/1.8083), round(height/2.1428)), (round(width/1.4598), round(height/1.4117)),
            (round(width/1.3698), round(height/4.1379)), (round(width/1.3245), round(height/2)), (round(width/1.0695), round(height/3.3333))]
#Towers infront of enemies
corTowerbelow = [(round(width/100), round(height/1.6666)), (round(width/3.7735), round(height/2.8571)), (round(width/2.5641), round(height/1.5)),
                 (round(width/1.8182), round(height/1.2631)), (round(width/1.4598), round(height/1.4117)), (round(width/1.3245), round(height/2))]

#Waves
#Each represents different enemies
#weak tri, weak square, weak hex, boss tri, norm tri, norm square, norm hex, boss sqaure, strong tri, strong square, strong hex
waves = [[20, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0], #1
    [50, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0],
    [30, 20, 0, 0, 0, 0 ,0 ,0, 0, 0, 0, 0],
    [30, 30, 20, 0, 0, 0 ,0 ,0, 0, 0, 0, 0],
    [15, 15, 15, 1, 0, 0 ,0 ,0, 0, 0, 0, 0], #5
    [0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0], #6
    [0, 0, 0, 0, 50, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 30, 20, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 20, 20, 20, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 15, 15, 15, 1, 0, 0, 0, 0], #10
    [0, 0, 0, 0, 0, 0, 0, 0, 20, 20, 20, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 5, 5, 5, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 5, 5, 5, 0],
    [0, 0, 0, 2, 0, 0, 0, 2, 5, 5, 5, 0],
    [0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 1]] #15

#Tower Settings
#Tower Cose
Tacost = 75
Tccost = 100
Tmcost = 125
#Range
Arange = round(width/5)
Crange = round(width/6.6667)
Mrange = round(width/5.5556)
#Initial Damage
Adamage = 10
Cdamage = 10
Mdamage = 5
#Number of Upgrades
Uarcher = 0
Ucannon = 0
Umagician = 0
#Initial Upgrade Cost
TUacost = 50
TUccost = 60
TUmcost = 60

#Gameplay Settings
#Defece
defence = 1 #Varies by difficulty
#Play Speed
playspeed = 1 #1x play speed

#Sounds
clicksound = pygame.mixer.Sound('Assets/ButtonPlate Click (Minecraft Sound) - Sound Effect for editing.wav')
archersound = pygame.mixer.Sound('Assets/Arrow Shot.wav')
cannonsound = pygame.mixer.Sound('Assets/Cannon Shot.wav')
magiciansound = pygame.mixer.Sound('Assets/Minecraft Fireball Sound Effect.wav')
sounds = [clicksound, archersound, cannonsound, magiciansound]
for i in sounds:
    i.set_volume(mVolume)
#Volume Bar in settings page for controlling volume
#Draw light gray rectangles based on the volume
class VolumeBar(pygame.sprite.Sprite):
    def __init__(self, position, bg):
        super().__init__()
        self.bg = bg
        self.x, self.y = position
        self.position = position
        Gvolumebar.add(self)

    def update(self, volume):
        for i in range(10):
            if i < round(volume*10):
                pygame.draw.rect(screen, self.bg, [self.x + (i*45), self.y, width/40, height/15])
            else:
                pygame.draw.rect(screen, Dgray, [self.x + (i*45), self.y, width/40, height/15])
