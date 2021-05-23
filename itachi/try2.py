import pygame
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((889, 500))
pygame.display.set_caption("First Game")
walkRight = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachi1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi6.png')]
walkLeft = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachi1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi6l.png')]
bg = pygame.image.load(r'C:\Users\alexl\Documents\itachi\background.jpg')
char = pygame.image.load(r'C:\Users\alexl\Desktop\Games\standing.png')
jumpright = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump5.png')]
jumpleft = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump5l.png')]
stance =  [pygame.image.load (r'C:\Users\alexl\Documents\itachi\stance1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance3.png')]
stancel = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\stance1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance3l.png')]
fire = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\fire1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire6.png')]
fireballs = [ pygame.image.load (r'C:\Users\alexl\Documents\itachi\fireball1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball6.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball7.png'),
pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball8.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball9.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball10.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball11.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball12.png')]
x = 50
kunai = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\kunai.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\kunai1.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\kunai2.png')]
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.fireball = False
        self.sr = True
        self.sl = False
        self.walkCount = 0
        self.jumpC = 0
        self.stanceCount = 0
        self.fireCount = 0
        self.fireballCount = 0
        self.screenh = 500
        self.screenw = 889
        self.standing = True
        self.down = ()
    def draw(self, win):
        if self.fireball == False:
            self.fireballCount = 0
            self.fireCount = 0
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.jumpC + 1 >= 14:
            self.jumpC = 0
        if self.fireCount + 1 >=  18:
            self.fireCount = 10
        if self.fireballCount + 1 >= 36:
            self.fireballCount = 26
        if self.stanceCount + 1 >= 9:
            self.stanceCount = 0
        if not(self.standing):
            if self.isJump and self.right:
                win.blit(jumpright[self.jumpC//3], (self.x,self.y))
                self.jumpC += 1
            elif self.isJump and self.left:
                win.blit(jumpleft[self.jumpC//3], (self.x,self.y))
                self.jumpC += 1
            elif self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.fireball:
                if self.fireballCount >= 26:
                    win.blit(fireballs[self.fireballCount//3], (self.x, self.y))
                    win.blit(fire[self.fireCount//3], (self.x + 45 ,self.y - 70))
                    self.fireballCount += 1
                    self.fireCount += 1
                else:
                    win.blit(fireballs[self.fireballCount//3], (self.x, self.y))
                    self.fireballCount += 1
        else:
            if self.left:
                win.blit(stancel[self.stanceCount//3], (self.x, self.y))
                self.stanceCount += 1
            else:
                win.blit(stance[self.stanceCount//3], (self.x, self.y))
                self.stanceCount += 1
class projectile(object):
    def __init__(self,x,y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.velx = 0
        self.vely = 0
        self.kunaiCount = 0
    def draw(self,win):
        if self.kunaiCount + 1 >= 6:
            self.kunaiCount = 0
        win.blit(kunai[self.kunaiCount//2] , (self.x,self.y))
        self.kunaiCount += 1


clock = pygame.time.Clock()


def redrawGameWindow():
    win.blit(bg, (0,0))
    itachi.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

run = True
itachi = player(300, 410, 80, 80)
bullets = []
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    movement = pygame.mouse.get_pos()
    pos = movement
    for bullet in bullets:
        rang = itachi.down[1] - (round(itachi.y + itachi.height//2))
        dist = itachi.down[0] - (round(itachi.x + itachi.width //2))
        tot = (rang ** 2 + dist ** 2) ** 1/2
        total = tot / 2000000
        bullet.velx = total * dist
        bullet.vely = total * rang
        if bullet.x < itachi.screenw and bullet.x > 0 and bullet.y < itachi.screenh and bullet.y > 0:
            bullet.x += bullet.velx
            bullet.y += bullet.vely
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if event.type == pygame.MOUSEBUTTONDOWN:
        itachi.down = movement
        if itachi.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 1:
            bullets.append(projectile(round(itachi.x + itachi.width //2),
             round(itachi.y + itachi.height//2), facing))
    if keys[pygame.K_a]:
        itachi.fireball = True
        itachi.standing = False
        itachi.right = False
        itachi.left = False

    elif keys[pygame.K_LEFT] and itachi.x > itachi.vel:
        itachi.x -= itachi.vel
        itachi.left = True
        itachi.right = False
        itachi.fireball = False
        itachi.standing = False


    elif keys[pygame.K_RIGHT] and itachi.x < itachi.screenw - itachi.vel - itachi.width:
        itachi.x += itachi.vel
        itachi.left = False
        itachi.right = True
        itachi.fireball = False
        itachi.standing = False


    else:
        itachi.standing = True
        itachi.walkCount = 0

    if not(itachi.isJump):
        if keys[pygame.K_UP]:
            itachi.isJump = True
            itachi.left = False
            itachi.right = False
            itachi.walkCount = 0
    else:
        if itachi.jumpCount >= -10:
            itachi.y -= (itachi.jumpCount * abs(itachi.jumpCount)) * 0.5
            itachi.jumpCount -= 1
        else:
            itachi.jumpCount = 10
            itachi.isJump = False

    redrawGameWindow()
