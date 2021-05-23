import pygame

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
fire = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\fire1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fire6.png')]
fireballs = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\fireball1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball6.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball7.png'),
pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball8.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball9.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball10.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball11.png'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\fireball12.png')]
x = 50

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



y = 400
screenh = 500
screenw = 889
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
fireball = False
sr = True
sl = False
walkCount = 0
jumpC = 0
stanceCount = 0
fireCount = 0
fireballCount = 0
def redrawGameWindow():
    global walkCount
    global jumpC
    global stanceCount
    global fireCount
    global fireballCount
    global fireball
    win.blit(bg, (0,0))
    if fireball == False:
        fireballCount = 0
        fireCount = 0
    if walkCount + 1 >= 18:
        walkCount = 0
    if jumpC + 1 >= 14:
        jumpC = 0
    if stanceCount + 1 >= 9:
        stanceCount = 0
    if fireCount + 1 >=  18:
        fireCount = 10
    if fireballCount + 1 >= 36:
        fireballCount = 26
    if isJump and right:
        win.blit(jumpright[jumpC//3], (x,y))
        jumpC += 1
    elif isJump and left:
        win.blit(jumpleft[jumpC//3], (x,y))
        jumpC += 1
    elif left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif fireball:
        if fireballCount >= 26:
            win.blit(fireballs[fireballCount//3], (x, y))
            win.blit(fire[fireCount//3], (x + 45 ,y - 70))
            fireballCount += 1
            fireCount += 1
        else:
            win.blit(fireballs[fireballCount//3], (x, y))
            fireballCount += 1

    else:
        win.blit(stance[stanceCount//3], (x, y))
        stanceCount += 1
    pygame.display.update()



run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        fireball = True
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
        fireball = False

    elif keys[pygame.K_RIGHT] and x < screenw - vel - width:
        x += vel
        left = False
        right = True
        fireball = False

    else:
        left = False
        right = False
        walkCount = 0

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    redrawGameWindow()


pygame.quit()
