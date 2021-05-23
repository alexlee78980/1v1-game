import pygame
from pygame.locals import *
pygame.init()
win = pygame.display.set_mode((889, 500))
pygame.display.set_caption("First Game")
#basics
bg = pygame.image.load(r'C:\Users\alexl\Documents\itachi\background.jpg')
hs = pygame.image.load(r'C:\Users\alexl\Documents\itachi\homescreen.gif')
sb = pygame.image.load(r'C:\Users\alexl\Documents\itachi\startbutton.png')
sbi = pygame.image.load(r'C:\Users\alexl\Documents\itachi\startbutton2.png')
score = 0

#Characters
#-Itachi
class CharacterItachi():
    def __init__(self):
        self.pf = pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachipf.png')
        self.walkRight = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachi1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi6.png')]
        self.walkLeft = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachi1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\itachi6l.png')]
        self.jumpright = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump5.png')]
        self.jumpleft = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump4l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\jump5l.png')]
        self.stance =  [pygame.image.load (r'C:\Users\alexl\Documents\itachi\stance1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance3.png')]
        self.stancel = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\stance1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\stance3l.png')]
        self.specialmove = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\fire1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire6.png')]
        self.specialmovel = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\fire1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire6l.png')]
        self.specialmoveattack = [ pygame.image.load (r'C:\Users\alexl\Documents\itachi\fireball1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball6.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball7.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball8.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball9.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball10.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball11.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball12.png')]
        self.specialmoveattackl = [ pygame.image.load (r'C:\Users\alexl\Documents\itachi\fireball1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball6l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball7l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball8l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball9l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball10l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball11l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball12l.png')]
        self.kunai = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\kunai.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\kunai1.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\kunai2.png')]
        self.throw = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw1.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw2.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw3.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw4.png')]
        self.throwl = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw1l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw2l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\throw4l.png')]
        self.specialability = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport1.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport2.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport3.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport4.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport5.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport6.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport8.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport9.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport10.png')]
        self.specialability1 = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport10.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport9.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport8.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport6.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport5.png'), pygame.image.load                  (r'C:\Users\alexl\Documents\itachi\teleport4.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport3.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport2.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport1.png')]
        self.specialabilityl = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport1l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport2l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport4l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport5l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport6l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport8l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport9l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport10l.png')]
        self.specialability1l = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport10l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport9l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport8l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport6l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport5l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport4l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport2l.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\teleport1l.png')]

charitachi = CharacterItachi()
#sound
handsign = pygame.mixer.Sound(r'C:\Users\alexl\Documents\itachi\handsigns.wav')

class player(object):
    def __init__(self,x,y,width,height, pf,  walkRight, walkLeft, jumpright, jumpleft, stance, stancel,specialmove, specialmovel, specialmoveattack, specialmoveattackl, kunai, throw, throwl, specialability, specialabilityl, specialability1, specialability1l):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.jumpright = jumpright
        self.jumpleft = jumpleft
        self.stance = stance
        self.stancel =stancel
        self.specialmove = specialmove
        self.specialmovel = specialmovel
        self.specialmovel = specialmovel
        self.specialmoveattack = specialmoveattack
        self.specialmoveattackl = specialmoveattackl
        self.kunai = kunai
        self.throw = throw
        self.throwl = throwl
        self.specialability = specialability
        self.specialabilityl = specialabilityl
        self.specialability1 = specialability1
        self.specialability1l = specialability1l
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.fireball = False
        self.sr = False
        self.sl = False
        self.walkCount = 0
        self.jumpC = 0
        self.stanceCount = 0
        self.fireCount = 0
        self.fireballCount = 0
        self.firebox = (0, 0, 0, 0)
        self.fireincreasex = 0
        self.fireincreasey = 0
        self.screenh = 500
        self.screenw = 889
        self.standing = True
        self.down = ()
        self.created = False
        self.throwCount = 0
        self.off = True
        self.throwt = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible  = True
        self.pf = pf
        self.teleport = False
        self.teleportCount = 0
        self.reappearCount = 0
        self.reappear = False
        self.teleportr = False
        self.teleportl = False
    def draw(self, win):
        if self.fireball == False:
            self.fireballCount = 0
            self.fireCount = 0
            handsign.stop()
            self.fireincreasex = 0
            self.fireincreasey = 0
            self.firebox = (0, 0, 0, 0)
        if self.reappearCount + 1 >= 30:
            self.reappear = False
            self.reappearCount = 0
            self.teleportr = False
            self.teleportl = False
        if self.teleportCount + 1 >= 30:
            if self.teleportl:
                if self.x - 300 < 0:
                    self.x = 0
                else:
                    self.x -= 300
            else:
                if self.x + 300 > self.screenw:
                    self.x = self.screenw - 80
                else:
                    self.x += 300
            self.teleport = False
            self.teleportCount = 0
            self.reappear = True
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
        if self.off == True:
            self.throwCount = 0
        if self.isJump and self.right:
            win.blit(self.jumpright[self.jumpC//3], (self.x,self.y))
            self.jumpC += 1
            self.hitbox = (self.x + 10 , self.y , 60, 80)
        elif self.isJump and self.left:
            win.blit(self.jumpleft[self.jumpC//3], (self.x,self.y))
            self.jumpC += 1
            self.hitbox = (self.x + 10 , self.y , 60, 80)
        elif self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            self.hitbox = (self.x , self.y , 80, 80)
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            self.hitbox = (self.x , self.y , 80, 80)
        elif self.fireball:
            if self.fireballCount == 1:
                handsign.play()
            if self.sl:
                if self.fireballCount >= 26:
                    win.blit(self.specialmoveattackl[self.fireballCount//3], (self.x, self.y))
                    win.blit(self.specialmovel[self.fireCount//3],(self.x -self.fireincreasex +10 ,self.y - 70))
                    self.firebox = (self.x -self.fireincreasex + 10, self.y - 40, self.fireincreasex, 130)
                    self.fireballCount += 1
                    self.fireCount += 1
                    self.hitbox = (self.x  , self.y , 55 , 80)
                    if self.fireincreasex >= 230:
                        self.fireincreasex = 230
                    else:
                        self.fireincreasex += 30
                else:
                    win.blit(self.specialmoveattackl[self.fireballCount//3], (self.x, self.y))
                    self.fireballCount += 1
                    self.hitbox = (self.x  , self.y , 40, 80)
            else:
                if self.fireballCount >= 26:
                    win.blit(self.specialmoveattack[self.fireballCount//3], (self.x, self.y))
                    win.blit(self.specialmove[self.fireCount//3], (self.x + 45 ,self.y - 70))
                    self.firebox = (self.x  + 45   ,self.y - 40, self.fireincreasex , 130)
                    self.fireballCount += 1
                    self.fireCount += 1
                    self.hitbox = (self.x  , self.y , 55 , 80)
                    if self.fireincreasex >= 240:
                        self.fireincreasex = 240
                    else:
                        self.fireincreasex += 30
                else:
                    win.blit(self.specialmoveattack[self.fireballCount//3], (self.x, self.y))
                    self.fireballCount += 1
                    self.hitbox = (self.x  , self.y , 40, 80)
        elif self.teleport:
            if self.sl:
                self.teleportl = True
                win.blit(self.specialabilityl[itachi.teleportCount//3],(self.x, self.y))
            else:
                self.teleportr = True
                win.blit(self.specialability[itachi.teleportCount//3],(self.x, self.y))
            self.teleportCount += 1
            self.hitbox = (0  , 0 , 0, 0)
        elif self.reappear:
            if self.teleportl:
                win.blit(self.specialability1l[itachi.reappearCount//3],(self.x, self.y))
            else:
                win.blit(self.specialability1[itachi.reappearCount//3],(self.x, self.y))
            self.reappearCount += 1
            self.hitbox = (self.x  , self.y , 80, 80)
        elif self.throwt:
            if self.throwCount + 1 >= 12:
                self.throwCount = 11
            if self.sl:
                win.blit(self.throwl[itachi.throwCount//3],(self.x, self.y))
                self.throwCount += 1
                self.hitbox = (self.x , self.y , 40, 80)
            else:
                win.blit(self.throw[itachi.throwCount//3],(self.x, self.y))
                self.throwCount += 1
                self.hitbox = (self.x + 5 , self.y , 40, 80)
        else:
            if self.sl:
                win.blit(self.stancel[self.stanceCount//3], (self.x, self.y))
                self.stanceCount += 1
                self.hitbox = (self.x + 5 , self.y , 40, 80)
            else:
                win.blit(self.stance[self.stanceCount//3], (self.x, self.y))
                self.stanceCount += 1
                self.hitbox = (self.x , self.y , 40, 80)
        pygame.draw.rect(win, (255,0,0), (155, 80 , 300, 30))
        pygame.draw.rect(win, (0,128,0), (155 ,80, 300 - (30 * (10 - self.health)), 30))
    #    pygame.draw.rect(win, (255,0,0), self.hitbox,2)
    #    pygame.draw.rect(win, (255,0,0), self.firebox ,2)

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            global alive
            alive = False
        print("damage")
    def flamedamage(self):
        print ("burn")




class projectile(object):
    def __init__(self,x,y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 8 * facing
        self.kunaiCount = 0
    def draw(self,win):
        if self.kunaiCount + 1 >= 6:
            self.kunaiCount = 0
        win.blit(person.kunai[self.kunaiCount//2] , (self.x ,self.y))
        self.kunaiCount += 1

class enemy(object):
    walkRight = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\kakashi1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi6.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi7.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi8.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi9.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi10.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi11.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi12.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi13.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi14.png')]
    walkLeft = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\kakashi1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi6l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi7l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi8l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi9l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi10l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi11l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi12l.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi13l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\kakashi14l.png')]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        self.vel = -3
        self.hitbox = (self.x + 40 , self.y, 75, 70)
        self.shield = ( self.x + 30 , self.y, 10, 70)
        self.health = 10
        self.visible = True
    def draw(self, win):
        if self.visible:
            self.move()
            if self.walkCount + 1 >= 42:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 30 , self.y + 10, 60, 70)
                self.shield = ( self.x + 90   , self.y + 10, 20, 70)
                if itachi.hitbox[1] + itachi.hitbox[3] > kakashi.shield[1]:
                    if itachi.hitbox[0] < kakashi.shield[0]  and  itachi.hitbox[0] + itachi.hitbox[3] >  kakashi.shield[0] :
                        itachi.hit()

            else:
                win.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
                self.hitbox = (self.x + 20, self.y + 10, 60, 70)
                self.shield = (self.x  , self.y + 10, 20, 70)
                if itachi.hitbox[1] + itachi.hitbox[3] > kakashi.shield[1]:
                    if itachi.hitbox[0] < kakashi.shield[0] +  kakashi.shield[3] and  itachi.hitbox[0] + itachi.hitbox[3] > kakashi.shield[0] +  kakashi.shield[3]:
                        itachi.hit()
            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 80, 7))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 80 - (8 * (10 - self.health)), 7))
        #    pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        #    pygame.draw.rect(win, (255,255,255), self.shield, 2)
        else:
            self.hitbox = (0 , 0, 0, 0)
            self.shield = (0 , 0, 0, 0)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[0] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[1] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
    def hit(self):
        global score
        print("hit")
        score += 1
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False

    def block(self):
        print("block")
    def flamedamage(self):
        global score
        if self.health > 0:
            self.health -= 0.5
            score += 0.5
        else:
            self.visible = False
clock = pygame.time.Clock()


def redrawGameWindow():
    if alive and kakashi.visible:
        win.blit(bg, (0,0))
        text = font.render("Score: " + str(score), 1, (255, 255, 255))
        win.blit(text, (780, 10))
        itachi.draw(win)
        if itachi.created:
            shield.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        kakashi.draw(win)
        win.blit(itachi.pf , (0, 0))
    elif kakashi.visible == False:
        gameover = fontl.render("You Win", 1, (255, 255, 255))
        playagain = font.render("Play Again",  1, (255, 255, 255))
        exit =  font.render("Exit",  1, (255, 255, 255))
        win.blit(gameover, (300, 200))
        win.blit(playagain, (300, 250))
        win.blit(exit, (500, 250))

    else:
        gameover = fontl.render("You Lose", 1, (255, 255, 255))
        playagain = font.render("Play Again",  1, (255, 255, 255))
        exit =  font.render("Exit",  1, (255, 255, 255))
        win.blit(gameover, (300, 200))
        win.blit(playagain, (300, 250))
        win.blit(exit, (500, 250))
    pygame.display.update()
def redrawHomeScreen():
    win.blit(hs, (0,0))
    if move[0] > 400 and move[0] < 830 and move[1]> 100 and move[1] < 375:
        win.blit(sb, (400, 100))
    else:
        win.blit(sbi, (400, 100))

    pygame.display.update()
alive = True
font = pygame.font.SysFont("comicsans", 30, True, True)
fontl = pygame.font.SysFont("comicsans", 60, True, True)
start = True
run = False
characterscreen = False
movement = pygame.mouse.get_pos()
keys = pygame.key.get_pressed()
itachi = player(0, 410, 80, 80, charitachi.pf, charitachi.walkRight, charitachi.walkLeft, charitachi.jumpright, charitachi.jumpleft, charitachi.stance, charitachi.stancel, charitachi.specialmove, charitachi.specialmovel, charitachi.specialmoveattack,  charitachi.specialmoveattackl, charitachi.kunai, charitachi.throw, charitachi.throwl, charitachi.specialability, charitachi.specialabilityl,  charitachi.specialability1, charitachi.specialability1l,)
person = itachi
kakashi = enemy(itachi.screenw - 85, 410, 85, 80,0)
bullets = []

while start:
    clock.tick(25)
    move = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if move[0] > 400 and move[0] < 830 and move[1]> 100 and move[1] < 375:
            run = True
            start = False

    redrawHomeScreen()



while run:
    clock.tick(25)
    movement = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if kakashi.vel > 0:
            if bullet.y - 30  < kakashi.shield[1] + kakashi.shield[3] and bullet.y + 30 > kakashi.shield[1]:
                if bullet.x  < kakashi.shield[0] + kakashi.shield[2] and bullet.x  > kakashi.shield[0]:
                    kakashi.block()
                    bullets.pop(bullets.index(bullet))
                    itachi.off = True
            if bullet.y - 30  < kakashi.hitbox[1] + kakashi.hitbox[3] and bullet.y + 30 > kakashi.hitbox[1]:
                if bullet.x + 30  > kakashi.hitbox[0] and bullet.x + 30 < kakashi.hitbox[0] + kakashi.hitbox[2] :
                    kakashi.hit()
                    bullets.pop(bullets.index(bullet))
                    itachi.off = True
        else:
            if bullet.y - 30  < kakashi.shield[1] + kakashi.shield[3] and bullet.y + 30 > kakashi.shield[1]:
                if bullet.x + 30  > kakashi.shield[0] and bullet.x + 30  < kakashi.shield[0] + kakashi.shield[2]:
                    kakashi.block()
                    bullets.pop(bullets.index(bullet))
                    itachi.off = True
            if bullet.y - 30  < kakashi.hitbox[1] + kakashi.hitbox[3] and bullet.y + 30 > kakashi.hitbox[1]:
                if bullet.x  > kakashi.hitbox[0] and bullet.x < kakashi.hitbox[0] + kakashi.hitbox[2]:
                    kakashi.hit()
                    bullets.pop(bullets.index(bullet))
                    itachi.off = True

        if bullet.x < itachi.screenw and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            itachi.off = True



    itachi.down = movement
    shield = projectile(itachi.down[0] - 15,itachi.down[1] - 15, 1)
    itachi.created = True

    if alive == False or kakashi.visible == False:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if movement[0] > 500 and movement[0] < 550 and movement[1] > 250 and movement[1] < 270:
                run = False
            elif movement[0] > 300 and movement[0] < 430 and movement[1] > 250 and movement[1] < 270:
                person.x = 0
                alive = True
                kakashi = enemy(itachi.screenw - 85, 410, 85, 80,0)

    if keys[pygame.K_SPACE]:
        if itachi.sl:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(itachi.x + itachi.width //2),
            round(itachi.y + itachi.height//3), facing))
        itachi.off = False
        itachi.right = False
        itachi.left = False
        itachi.throwt = True


    elif keys[pygame.K_t]:
        itachi.teleport = True
        itachi.right = False
        itachi.left = False


    elif keys[pygame.K_f]:
        itachi.fireball = True
        itachi.right = False
        itachi.left = False
        if person.sl:
            if kakashi.hitbox[0] + kakashi.hitbox[2] > person.firebox[0] and person.firebox[0] + person.firebox[2] >  kakashi.hitbox[0]:
                if kakashi.hitbox[1] < person.firebox[1] + person.firebox[3]:
                    kakashi.flamedamage()
        else:
            if kakashi.hitbox[0] > person.firebox[0] and person.firebox[0] + person.firebox[2] >  kakashi.hitbox[0]:
                if kakashi.hitbox[1] < person.firebox[1] + person.firebox[3]:
                    kakashi.flamedamage()

    elif (keys[pygame.K_LEFT] or keys[pygame.K_a])   and itachi.x > itachi.vel:
        itachi.x -= itachi.vel
        itachi.left = True
        itachi.right = False
        itachi.fireball = False
        itachi.sl = True
        itachi.sr = False


    elif (keys[pygame.K_RIGHT] or  keys[pygame.K_d]) and itachi.x < itachi.screenw - itachi.vel - itachi.width:
        itachi.x += itachi.vel
        itachi.left = False
        itachi.right = True
        itachi.fireball = False

        itachi.sr = True
        itachi.sl = False


    else:
        itachi.right = False
        itachi.left = False
        itachi.walkCount = 0
        itachi.fireball = False
        itachi.throwt = False

    if not(itachi.isJump):
        if (keys[pygame.K_UP] or  keys[pygame.K_w]):
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


pygame.quit()
