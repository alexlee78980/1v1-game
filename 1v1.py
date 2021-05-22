import pygame
from pygame.locals import *
pygame.init()
win = pygame.display.set_mode((889, 500))
pygame.display.set_caption("1 V 1")
#basics
bg = [pygame.image.load(r'C:\Users\alexl\Documents\akame\background1.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\background2.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\background3.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\background4.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\background5.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\background6.gif')]
hs = pygame.image.load(r'C:\Users\alexl\Documents\itachi\homescreen.png')
sb = pygame.image.load(r'C:\Users\alexl\Documents\itachi\startbutton.png')
sbi = pygame.image.load(r'C:\Users\alexl\Documents\itachi\startbutton2.png')
csb = pygame.image.load(r'C:\Users\alexl\Documents\itachi\csb.jpg')
cape = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\cape1.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\cape2.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\cape3.png'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\cape4.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\cape5.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\cape6.png'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\cape7.png')]
susanoo = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\p1.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p2.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p3.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p4.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p5.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p6.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p7.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p8.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p9.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p10.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p11.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p12.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p13.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p14.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p15.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p16.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p17.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p18.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p19.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p20.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p21.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p22.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p23.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p24.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p25.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p26.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p27.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p28.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p29.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p30.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p31.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p32.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p33.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p34.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p35.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p36.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p37.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p38.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p39.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p40.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p41.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p42.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p43.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p44.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p45.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p46.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p47.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p48.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p49.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p50.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p51.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p52.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p53.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p54.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p55.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p56.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p57.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p58.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p59.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p60.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p61.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p62.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p63.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p64.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p65.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p66.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\p67.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p68.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p69.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p70.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p71.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\p72.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\p73.gif')]
selectcharacter1 =  pygame.image.load(r'C:\Users\alexl\Documents\itachi\select.1.png')
selectcharacter2 =  pygame.image.load(r'C:\Users\alexl\Documents\itachi\select.2.png')
itachidisplaypictures = [pygame.image.load (r'C:\Users\alexl\Documents\itachi\dp1.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp2.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp3.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp4.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp5.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp6.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\dp7.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp8.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp9.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp10.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp11.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp12.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\dp13.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp14.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp15.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp16.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp17.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp18.gif'), pygame.image.load (r'C:\Users\alexl\Documents\itachi\dp19.gif'), pygame.image.load(r'C:\Users\alexl\Documents\itachi\dp20.gif')]
border = pygame.image.load(r'C:\Users\alexl\Documents\itachi\border.png')
score = 0
sasukedisplaypictures = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\dp1.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp2.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp3.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp4.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp5.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp6.gif'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\dp7.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp8.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp9.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp10.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp11.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp12.gif'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\dp1.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp2.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp3.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp4.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp5.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp6.gif'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\dp7.gif'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\dp8.gif')]
Akamedisplaypictures = [pygame.image.load (r'C:\Users\alexl\Documents\akame\dp1.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp2.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp3.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\dp4.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp5.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\dp6.gif'), pygame.image.load (r'C:\Users\alexl\Documents\akame\dp7.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp8.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp9.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\dp10.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp11.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\dp12.gif'), pygame.image.load (r'C:\Users\alexl\Documents\akame\dp13.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp14.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp15.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\dp16.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp17.gif'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\dp18.gif'), pygame.image.load (r'C:\Users\alexl\Documents\akame\dp19.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp20.gif') ,  pygame.image.load (r'C:\Users\alexl\Documents\akame\dp21.gif'), pygame.image.load(r'C:\Users\alexl\Documents\akame\dp22.gif')]
#Characters
#-Itachi
class CharacterItachi():
    def __init__(self):
        self.pf = pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachipf.png')
        self.displayimage = pygame.image.load (r'C:\Users\alexl\Documents\itachi\itachipf.jpg')
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
# Sasuke
class CharacterSasuke():
    def __init__(self):
        self.walkRight =[pygame.image.load (r'C:\Users\alexl\Documents\sasuke\run1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run2.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run3.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\run1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run2.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run3.png')]
        self.walkLeft =[pygame.image.load (r'C:\Users\alexl\Documents\sasuke\run1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\run1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\run3l.png')]
        self.jumpright = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1.png')]
        self.jumpleft = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\jump1l.png')]
        self.stance =  [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\stance1.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\stance2.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\stance3.png')]
        self.stancel = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\stance1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\stance2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\sasuke\stance3l.png')]
        self.specialmove =[ pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirin1.png'),  pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirin1.png'),  pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirin1.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirin2.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirin3.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirin4.png')]
        self.specialmoveattack = [ pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance1.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance2.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance3.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance4.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance5.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance6.png'), pygame.image.load
        (r'C:\Users\alexl\Documents\sasuke\kirinstance7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance8.png'),  pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance9.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance8.png'),  pygame.image.load (r'C:\Users\alexl\Documents\sasuke\kirinstance9.png')]
        self.throw = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw1.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw2.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw3.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw3.png')]
        self.throwl = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw1l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw2l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\throw3l.png')]
        self.specialability = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport1.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport2.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport3.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport4.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport5.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport6.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png')]
        self.specialability1 = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport6.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport5.png'), pygame.image.load                  (r'C:\Users\alexl\Documents\sasuke\teleport4.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport3.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport2.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport1.png')]
        self.specialabilityl = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport1l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport2l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport4l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport5l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport6l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png')]
        self.specialability1l = [pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport7l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport6l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport5l.png'), pygame.image.load
        (r'C:\Users\alexl\Documents\sasuke\teleport4l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport3l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport2l.png'), pygame.image.load (r'C:\Users\alexl\Documents\sasuke\teleport1l.png')]

charSasuke = CharacterSasuke()
#Akame
class CharacterAkame():
    def __init__(self):
        self.walkRight = [pygame.image.load (r'C:\Users\alexl\Documents\akame\run1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\run4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run5.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\run6.png')]
        self.walkLeft = [pygame.image.load (r'C:\Users\alexl\Documents\akame\run1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\run4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\run6l.png')]
        self.jumpright = [pygame.image.load (r'C:\Users\alexl\Documents\akame\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump5.png')]
        self.jumpleft = [pygame.image.load (r'C:\Users\alexl\Documents\akame\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump5l.png')]
        self.stance =  [pygame.image.load (r'C:\Users\alexl\Documents\akame\stance3.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2.png')]
        self.stancel = [pygame.image.load (r'C:\Users\alexl\Documents\akame\stance3l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2l.png')]
        self.specialmoveattack =  [ pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png'),  pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png')]
        self.specialmoveattackl =  [ pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png'),  pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png')]
        self.specialability = [pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash5.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash2.png')]
        self.specialabilityl = [pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl5.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl2.png')]
charAkame = CharacterAkame()
# levi
class CharacterLevi():
    def __init__(self):
        self.walkRight = [pygame.image.load (r'C:\Users\alexl\Documents\levi\run1.png'), pygame.image.load(r'C:\Users\alexl\Documents\levi\run2.png'), pygame.image.load(r'C:\Users\alexl\Documents\levi\run3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\levi\run1.png'), pygame.image.load(r'C:\Users\alexl\Documents\levi\run2.png'),  pygame.image.load(r'C:\Users\alexl\Documents\levi\run3.png')]
        self.walkLeft = [pygame.image.load (r'C:\Users\alexl\Documents\akame\run1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\run4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\run5l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\run6l.png')]
        self.jumpright = [pygame.image.load (r'C:\Users\alexl\Documents\akame\jump1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump5.png')]
        self.jumpleft = [pygame.image.load (r'C:\Users\alexl\Documents\akame\jump1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\jump3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump4l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\jump5l.png')]
        self.stance =  [pygame.image.load (r'C:\Users\alexl\Documents\akame\stance3.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2.png')]
        self.stancel = [pygame.image.load (r'C:\Users\alexl\Documents\akame\stance3l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\stance2l.png')]
        self.specialmoveattack =  [ pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png'),  pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2.png')]
        self.specialmoveattackl =  [ pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png'),  pygame.image.load (r'C:\Users\alexl\Documents\akame\slash1l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash4l.png'), pygame.image.load(r'C:\Users\alexl\Documents\akame\slash3l.png'),  pygame.image.load(r'C:\Users\alexl\Documents\akame\slash2l.png')]
        self.specialability = [pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash5.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslash2.png')]
        self.specialabilityl = [pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl5.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl4.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl3.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl2.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl1.png'), pygame.image.load (r'C:\Users\alexl\Documents\akame\stationaryslashl2.png')]
charLevi = CharacterLevi()

#sound
handsign1 = pygame.mixer.Sound(r'C:\Users\alexl\Documents\itachi\handsigns.wav')
handsign2 = pygame.mixer.Sound(r'C:\Users\alexl\Documents\itachi\handsigns.wav')

class player1(object):
    def __init__(self,x,y, width,height, vel, jumpCount, hasprojectile, hasslash, hasteleport, pf,  walkRight, walkLeft, jumpright, jumpleft, stance, stancel,specialmove, specialmovex, specialmovey, specialmovel, specialmoveattack, specialmoveattackl, kunai, throw, throwl, specialability, specialabilityl, specialability1, specialability1l):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hasprojectile = hasprojectile
        self.hasslash = hasslash
        self.hasteleport = hasteleport
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.jumpright = jumpright
        self.jumpleft = jumpleft
        self.stance = stance
        self.stancel =stancel
        self.specialmove = specialmove
        self.specialmovel = specialmovel
        self.specialmovex =  specialmovex
        self.specialmovey =  specialmovey
        self.specialmovel = specialmovel
        self.specialmoveattack = specialmoveattack
        self.specialmoveattackl = specialmoveattackl
        self.kunai = kunai
        self.cooldown = 10
        self.throw = throw
        self.throwl = throwl
        self.specialability = specialability
        self.specialabilityl = specialabilityl
        self.specialability1 = specialability1
        self.specialability1l = specialability1l
        self.vel = vel
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = jumpCount
        self.jumpCountO = jumpCount
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
        self.facing = 1
        self.throwCount = 0
        self.off = True
        self.throws = False
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
        self.slash = False
        self.slashCount = 0
    def draw(self, win):
        if self.cooldown > 10:
            self.cooldown = 0
        if self.cooldown > 0:
            self.cooldown += 1
        if self.fireball == False:
            self.fireballCount = 0
            self.fireCount = 0
            handsign1.stop()
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
        if self.slashCount + 1 >= 36:
            self.slashCount = 26
        if self.stanceCount + 1 >= 9:
            self.stanceCount = 0
        if self.slash and self.right and self.hasslash:
            win.blit(self.specialmoveattack[self.slashCount//3], (self.x,self.y))
            self.firebox = ((self.x + 90), self.y + 40, 10, 1)
            self.hitbox = (self.x + 10 , self.y , 50, 80)
            self.slashCount += 1
            self.slash = False
        elif self.slash and self.left and self.hasslash:
            win.blit(self.specialmoveattackl[self.slashCount//3], (self.x -50 ,self.y))
            self.hitbox = (self.x -10  , self.y , 60, 80)
            self.firebox = ((self.x - 55), self.y + 40, 10, 1)
            self.slashCount += 1
            self.slash = False
        elif self.isJump and self.right:
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

        elif self.teleport and self.hasteleport:
            if self.sl:
                self.teleportl = True
                win.blit(self.specialabilityl[self.teleportCount//3],(self.x, self.y))
            else:
                self.teleportr = True
                win.blit(self.specialability[self.teleportCount//3],(self.x, self.y))
            self.teleportCount += 1
            self.hitbox = (0  , 0 , 0, 0)

        elif self.reappear and self.hasteleport:
            if self.teleportl:
                win.blit(self.specialability1l[self.reappearCount//3],(self.x, self.y))
            else:
                win.blit(self.specialability1[self.reappearCount//3],(self.x, self.y))
            self.reappearCount += 1
            self.hitbox = (self.x  , self.y , 80, 80)

        elif self.fireball and self.hasprojectile:
            if self.fireballCount == 1:
                handsign1.play()
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
                    win.blit(self.specialmove[self.fireCount//3], (self.x + self.specialmovex ,self.y + self.specialmovey))
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

        elif self.throwt and self.hasprojectile:
            if self.throwCount + 1 >= 12:
                self.throwCount = 0
            if self.sl:
                win.blit(self.throwl[self.throwCount//3],(self.x, self.y))
                self.throwCount += 1
                self.hitbox = (self.x , self.y , 40, 80)
                self.throwt = False
            else:
                win.blit(self.throw[self.throwCount//3],(self.x, self.y))
                self.throwCount += 1
                self.hitbox = (self.x + 5 , self.y , 40, 80)
                self.throwt = False
        else:
            if self.sl:
                if self.slash and self.hasslash:
                    win.blit(self.specialabilityl[self.stanceCount//3], (self.x - 50, self.y))
                    self.stanceCount += 1
                    self.firebox = ((self.x - 50), self.y + 40, 10, 1)
                    self.slash = False
                    self.hitbox = (self.x - 15 , self.y , 40, 80)
                else:
                    win.blit(self.stancel[self.stanceCount//3], (self.x, self.y))
                    self.stanceCount += 1
                    self.hitbox = (self.x + 5 , self.y , 40, 80)
            else:
                if self.slash and self.hasslash:
                    win.blit(self.specialability[self.stanceCount//3], (self.x, self.y))
                    self.stanceCount += 1
                    self.firebox = ((self.x + 90), self.y + 40, 10, 1)
                    self.hitbox = (self.x + 20 , self.y , 40, 80)
                    self.slash = False
                else:
                    win.blit(self.stance[self.stanceCount//3], (self.x, self.y))
                    self.stanceCount += 1
                    self.hitbox = (self.x , self.y , 40, 80)
        if self.throws and self.hasprojectile:
            if self.sl:
                facing =- 1
            else:
                facing = 1
            if len(bullets1) < 100 and self.cooldown == 0:
                bullets1.append(projectile(round(self.x + self.width //2),
                round(self.y + self.height//3), facing))
                self.cooldown = 3
            self.throws = False

        pygame.draw.rect(win, (255,0,0), (100, 40 , 200, 30))
        pygame.draw.rect(win, (0,128,0), (100 ,40, 200 - (20 * (10 - self.health)), 30))
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #pygame.draw.rect(win, (255,0,0), self.firebox ,2)
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            global alive2
            alive2 = False
        print("damage")

    def flamedamage(self):
        global person2
        if person2.health <= 0:
            global alive2
            alive2 = False
        else:
            person2.health -= 0.5

    def throwdamage(self):
        global person2
        if person2.health <= 0:
            global alive2
            alive2 = False
        else:
            person2.health -= 1
class player2(object):
    def __init__(self,x,y,width,height, vel, jumpCount, hasprojectile,  hasslash, hasteleport, pf,   walkRight, walkLeft, jumpright, jumpleft, stance, stancel,specialmove, specialmovex, specialmovey, specialmovel, specialmoveattack, specialmoveattackl, kunai, throw, throwl, specialability, specialabilityl, specialability1, specialability1l):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hasprojectile = hasprojectile
        self.hasslash =hasslash
        self.hasteleport = hasteleport
        self.walkRight = walkRight
        self.walkLeft = walkLeft
        self.jumpright = jumpright
        self.jumpleft = jumpleft
        self.stance = stance
        self.stancel =stancel
        self.specialmove = specialmove
        self.specialmovex =  specialmovex
        self.specialmovey =  specialmovey
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
        self.vel = vel
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = jumpCount
        self.jumpCountO = jumpCount
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
        self.cooldown = 10
        self.facing = -1
        self.throwt = False
        self.throws = False
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
        self.slash = False
        self.slashCount = 0
    def draw(self, win):
        if self.cooldown > 10:
            self.cooldown = 0
        if self.cooldown > 0:
            self.cooldown += 1
        if self.fireball == False:
            self.fireballCount = 0
            self.fireCount = 0
            handsign2.stop()
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
        if self.slashCount + 1 >= 36:
            self.slashCount = 26
        if self.stanceCount + 1 >= 9:
            self.stanceCount = 0
        if self.slash and self.right and self.hasslash:
            win.blit(self.specialmoveattack[self.slashCount//3], (self.x,self.y))
            self.firebox = ((self.x + 90), self.y + 40, 10, 1)
            self.hitbox = (self.x + 10 , self.y , 50, 80)
            self.slashCount += 1
            self.slash = False
        elif self.slash and self.left and self.hasslash:
            win.blit(self.specialmoveattackl[self.slashCount//3], (self.x -50 ,self.y))
            self.hitbox = (self.x -10  , self.y , 60, 80)
            self.firebox = ((self.x - 55), self.y + 40, 10, 1)
            self.slashCount += 1
            self.slash = False
        elif self.isJump and self.right:
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
        elif self.fireball and self.hasprojectile:
            if self.fireballCount == 1:
                handsign2.play()
            if self.sr:
                if self.fireballCount >= 26:
                    win.blit(self.specialmoveattack[self.fireballCount//3], (self.x, self.y))
                    win.blit(self.specialmove[self.fireCount//3], (self.x + self.specialmovex ,self.y + self.specialmovey))
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
            else:
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

        elif self.teleport and self.hasteleport:
            if self.sr:
                self.teleportr = True
                win.blit(self.specialability[self.teleportCount//3],(self.x, self.y))
            else:
                self.teleportl = True
                win.blit(self.specialabilityl[self.teleportCount//3],(self.x, self.y))

            self.teleportCount += 1
            self.hitbox = (0  , 0 , 0, 0)

        elif self.reappear and self.hasteleport:
            if self.teleportl:
                win.blit(self.specialability1l[self.reappearCount//3],(self.x, self.y))
            else:
                win.blit(self.specialability1[self.reappearCount//3],(self.x, self.y))
            self.reappearCount += 1
            self.hitbox = (self.x  , self.y , 80, 80)

        elif self.throwt and self.hasprojectile:
            if self.throwCount + 1 >= 12:
                self.throwCount = 0
            if self.sr:
                win.blit(self.throw[self.throwCount//3],(self.x, self.y))
                self.throwCount += 1
                self.hitbox = (self.x + 5 , self.y , 40, 80)
                self.throwt = False
            else:
                win.blit(self.throwl[self.throwCount//3],(self.x, self.y))
                self.throwCount += 1
                self.hitbox = (self.x , self.y , 40, 80)
                self.throwt = False


        else:
            if self.sr:
                if self.hasslash and self.slash:
                    win.blit(self.specialability[self.stanceCount//3], (self.x, self.y))
                    self.stanceCount += 1
                    self.firebox = ((self.x + 90), self.y + 40, 10, 1)
                    self.hitbox = (self.x + 20 , self.y , 40, 80)
                    self.slash = False
                else:
                    win.blit(self.stance[self.stanceCount//3], (self.x, self.y))
                    self.stanceCount += 1
                    self.hitbox = (self.x , self.y , 40, 80)
            else:
                if self.hasslash and self.slash:
                    win.blit(self.specialabilityl[self.stanceCount//3], (self.x - 50, self.y))
                    self.stanceCount += 1
                    self.firebox = ((self.x - 50), self.y + 40, 10, 1)
                    self.slash = False
                    self.hitbox = (self.x - 15 , self.y , 40, 80)
                else:
                    win.blit(self.stancel[self.stanceCount//3], (self.x, self.y))
                    self.stanceCount += 1
                    self.hitbox = (self.x + 5 , self.y , 40, 80)

        if self.hasprojectile and self.throws:
            if self.sr:
                facing = 1
            else:
                facing = -1
            if len(bullets1) < 100 and self.cooldown == 0:
                bullets2.append(projectile(round(self.x + self.width //2),
                round(self.y + self.height//3), facing))
                self.cooldown = 3
            self.throws = False




        pygame.draw.rect(win, (255,0,0), (600, 40, 200, 30))
        pygame.draw.rect(win, (0,128,0), (600 , 40, 200 - (20 * (10 - self.health)), 30))
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)
        #pygame.draw.rect(win, (255,0,0), self.firebox ,

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            global alive2
            alive2 = False
        print("damage")

    def flamedamage(self):
        global person1
        if person1.health <= 0:
            global alive1
            alive1 = False
        else:
            person1.health -= 0.5
    def throwdamage(self):
        global person1
        if person1.health <= 0:
            global alive1
            alive1 = False
        else:
            person1.health -= 1





class projectile(object):
    def __init__(self,x,y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 7 * facing
        self.kunaiCount = 0
    def draw(self,win):
        global person1

        if self.kunaiCount + 1 >= 6:
            self.kunaiCount = 0
        win.blit(person1.kunai[self.kunaiCount//2] , (self.x ,self.y))
        self.kunaiCount += 1


clock = pygame.time.Clock()

#homescreen
capeCount = 0
taptostartCount = 0

def helphomeScreen():
    global capeCount
    global kirinCount
    global taptostartCount
    taptostart = [font.render("Click to Start",  1, (255, 255, 255)), font.render("",  1, (255, 255, 255))]
    win.blit(hs, (0,0))
    if capeCount >= 21:
        capeCount = 0
    if taptostartCount >= 50:
        taptostartCount = 0
#    if move[0] > 400 and move[0] < 830 and move[1]> 100 and move[1] < 375:
#        win.blit(sb, (400, 100))
#    else:
#        win.blit(sbi, (400, 100))
    win.blit(cape[capeCount//3], (70, 120))
    win.blit(taptostart[taptostartCount//25], (500, 350))
    taptostartCount += 1
    capeCount += 1




#charcacter selection
select = 0
susanooCount = 0
itachidpCount = 0
sasukedpCount = 0
akamedpCount = 0
itachidp = False
sasukedp = False
akamedp = False
presseditachi = False
pressedsasuke = False
pressedakame = False

def helpcharacterScreen():
    global selectcharacter1
    global selectcharacter2
    global susanooCount
    global itachidp
    global sasukedp
    global akamedp
    global itachidpCount
    global sasukedpCount
    global akamedpCount
    global pressedsasuke
    global presseditachi
    global pressedakame
    if susanooCount + 1 >= 74:
        susanooCount = 0
    if itachidpCount + 1 >= 21:
        itachidpCount = 19
    if sasukedpCount + 1 >= 21:
        sasukedpCount = 19
    if akamedpCount + 1 >= 21:
        akamedpCount = 20
    if not(itachidp):
        itachidpCount = 0
    if not(sasukedp):
        sasukedpCount = 0
    if not(akamedp):
        akamedpCount = 0

    win.blit(susanoo[susanooCount], (0,0))
    win.blit(select, (200, 10))
    if itachidp:
        win.blit(itachidisplaypictures[itachidpCount], (10, 100))
    else:
        win.blit(itachidisplaypictures[0], (10, 100))
    if sasukedp:
        win.blit(sasukedisplaypictures[sasukedpCount], (120, 100))
    else:
        win.blit(sasukedisplaypictures[0], (120, 100))
    if akamedp:
        win.blit(Akamedisplaypictures[akamedpCount], (230, 100))
    else:
        win.blit(Akamedisplaypictures[akamedpCount], (230, 100))
    if presseditachi:
        win.blit(border, (- 40 , 50))
    elif pressedsasuke:
        win.blit(border, ( 80 , 50))
    elif pressedakame:
        win.blit(border, (185, 50))
    itachidpCount += 1
    sasukedpCount += 1
    akamedpCount += 1
    susanooCount +=1

def redrawHomeScreen():
    helphomeScreen()
    pygame.display.update()

def redrawHelpScreen():
    win.blit(bg, (0,0))
    player1 = font.render("Player 1", 1, (255, 255, 255))
    player2 = font.render("Player 2", 1 ,(255, 255, 255))
    pygame.display.update()




def redrawCharacterScreen():
    helpcharacterScreen()
    pygame.display.update()

def redrawGameWindow():
    if alive1 and alive2:
        global backgroundCount
        if backgroundCount + 1 > 6:
            backgroundCount = 0
        win.blit(bg[backgroundCount], (0,0))
        person1.draw(win)
        person2.draw(win)
        if person1.created:
            shield.draw(win)
        for bullet in bullets1:
            bullet.draw(win)
        for bullet in bullets2:
            bullet.draw(win)
        win.blit(person1.pf , (0, 0))
        win.blit(person2.pf , (889- 110, 0))
        backgroundCount += 1

    elif not(alive1) and not(alive2):
        gameover = fontl.render("Tie", 1, (255, 255, 255))
        playagain = font.render("Play Again",  1, (255, 255, 255))
        exit =  font.render("Exit",  1, (255, 255, 255))
        win.blit(gameover, (300, 200))
        win.blit(playagain, (300, 250))
        win.blit(exit, (500, 250))

    elif not(alive1):
        gameover = fontl.render("Player2 Wins", 1, (255, 255, 255))
        playagain = font.render("Play Again",  1, (255, 255, 255))
        exit =  font.render("Exit",  1, (255, 255, 255))
        win.blit(gameover, (300, 200))
        win.blit(playagain, (300, 250))
        win.blit(exit, (500, 250))
    else:
        gameover = fontl.render("Player1 Wins", 1, (255, 255, 255))
        playagain = font.render("Play Again",  1, (255, 255, 255))
        exit =  font.render("Exit",  1, (255, 255, 255))
        win.blit(gameover, (300, 200))
        win.blit(playagain, (300, 250))
        win.blit(exit, (500, 250))
    pygame.display.update()


alive1 = True
alive2 = True
font = pygame.font.SysFont("comicsans", 30, True, True)
fontl = pygame.font.SysFont("comicsans", 60, True, True)
start = True
helpScreen = False
run = False
characterscreen = False
characterscreen1 = False
movement = pygame.mouse.get_pos()
keys = pygame.key.get_pressed()
itachi1 = player1(0, 410, 80, 80, 5, 10, True, False, True, charitachi.pf, charitachi.walkRight, charitachi.walkLeft, charitachi.jumpright, charitachi.jumpleft, charitachi.stance, charitachi.stancel, charitachi.specialmove, 45, -70, charitachi.specialmovel, charitachi.specialmoveattack, charitachi.specialmoveattackl, charitachi.kunai, charitachi.throw, charitachi.throwl, charitachi.specialability, charitachi.specialabilityl,  charitachi.specialability1, charitachi.specialability1l)
itachi2 = player2(889 - 80, 410, 80, 80, 5, 10, True, False, True, charitachi.pf, charitachi.walkRight, charitachi.walkLeft, charitachi.jumpright, charitachi.jumpleft, charitachi.stance, charitachi.stancel, charitachi.specialmove, 45, -70, charitachi.specialmovel, charitachi.specialmoveattack, charitachi.specialmoveattackl, charitachi.kunai, charitachi.throw, charitachi.throwl, charitachi.specialability, charitachi.specialabilityl,  charitachi.specialability1, charitachi.specialability1l)
sasuke1 = player1(0, 410, 80, 80,5, 10, True, False, True,charitachi.pf, charSasuke.walkRight, charSasuke.walkLeft, charSasuke.jumpright, charSasuke.jumpleft, charSasuke.stance, charSasuke.stancel, charSasuke.specialmove, 45, -350, charitachi.specialmovel, charSasuke.specialmoveattack,  charitachi.specialmoveattackl, charitachi.kunai,  charSasuke.throw, charSasuke.throwl, charSasuke.specialability, charSasuke.specialabilityl,  charSasuke.specialability1, charSasuke.specialability1l)
sasuke2 = player2(889 -80,  410, 80, 80,5, 10, True, False, True, charitachi.pf, charSasuke.walkRight, charSasuke.walkLeft, charSasuke.jumpright, charSasuke.jumpleft, charSasuke.stance, charSasuke.stancel, charSasuke.specialmove, 45, -350, charitachi.specialmovel, charSasuke.specialmoveattack,  charitachi.specialmoveattackl, charitachi.kunai, charSasuke.throw, charSasuke.throwl, charSasuke.specialability, charSasuke.specialabilityl,  charSasuke.specialability1, charSasuke.specialability1l)
akame1 = player1(0, 410, 80, 80, 10, 12, False, True, False, charitachi.pf, charAkame.walkRight, charAkame.walkLeft, charAkame.jumpright, charAkame.jumpleft, charAkame.stance, charAkame.stancel, charSasuke.specialmove, 45, -350, charitachi.specialmovel, charAkame.specialmoveattack,  charAkame.specialmoveattackl, charitachi.kunai,  charSasuke.throw, charSasuke.throwl, charAkame.specialability, charAkame.specialabilityl,  charSasuke.specialability1, charSasuke.specialability1l)
akame2 = player2(889 - 80, 410, 80, 80, 10, 12, False, True, False, charitachi.pf, charAkame.walkRight, charAkame.walkLeft, charAkame.jumpright, charAkame.jumpleft, charAkame.stance, charAkame.stancel, charSasuke.specialmove, 45, -350, charitachi.specialmovel, charAkame.specialmoveattack,  charAkame.specialmoveattackl, charitachi.kunai,  charSasuke.throw, charSasuke.throwl, charAkame.specialability, charAkame.specialabilityl,  charSasuke.specialability1, charSasuke.specialability1l)
bullets1 = []
bullets1 = []
bullets2 = []
cooldown1 = 0
cooldown2 = 0
backgroundCount = 0

while start:
    clock.tick(25)
    move = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    if event.type == pygame.MOUSEBUTTONDOWN:
    #    if move[0] > 400 and move[0] < 830 and move[1]> 100 and move[1] < 375:
        characterscreen = True
        start = False
    redrawHomeScreen()

while helpScreen:
    clock.tick(25)
    move3 = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            helpScreen = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        helpScreen = False
        start = True
    redrawHelpScreen()

counterstart1 = False
counterstart2 = False
counterstart3 = False
counter1 = 0
counter2 = 0
counter3 = 0
while characterscreen:
    clock.tick(25)
    move1 = pygame.mouse.get_pos()
    select = selectcharacter1

    if counterstart1:
        counter1 += 1
    else:
        counter1 = 0

    if counterstart2:
        counter2 += 1
    else:
        counter2 = 0

    if counterstart3:
        counter3 += 1
    else:
        counter3 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            characterscreen = False
        if move1[0] > 10 and  move1[0] < 110 and move1[1] > 100 and move1[1] < 200:
            itachidp = True
            sasukedp = False
            akamedp = False
        elif  move1[0] > 120 and  move1[0] < 220 and move1[1] > 100 and move1[1] < 200:
            itachidp = False
            sasukedp = True
            akamedp = False
        elif  move1[0] > 230 and  move1[0] < 330 and move1[1] > 100 and move1[1] < 200:
            itachidp = False
            sasukedp = False
            akamedp = True
        else:
            itachidp = False
            sasukedp = False
            akamedp = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move1[0] > 10 and  move1[0] < 110 and move1[1] > 100 and move1[1] < 200:
                presseditachi = True
                counterstart1 = True
                counterstart2 = False
                pressedsasuke = False
        if presseditachi:
                if event.type == pygame.MOUSEBUTTONDOWN and counter1 > 10:
                    if move1[0] > 10 and  move1[0] < 110 and move1[1] > 100 and move1[1] < 200:
                        characterscreen = False
                        person1 = itachi1
                        counter1 = 0
                        presseditachi = False
                        counterstart1 = False
                        counterstart2 = False
                        characterscreen1 = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move1[0] > 120 and  move1[0] < 220 and move1[1] > 100 and move1[1] < 200:
                pressedsasuke = True
                pressedakame = False
                presseditachi = False
                counterstart2 = True
                counterstart1 = False
                counterstart3 = False
        if pressedsasuke:
            if event.type == pygame.MOUSEBUTTONDOWN and counter2 > 10:
                if move1[0] > 120 and  move1[0] < 220 and move1[1] > 100 and move1[1] < 200:
                        characterscreen = False
                        person1 = sasuke1
                        counter2 = 0
                        counterstart1 = False
                        counterstart2 = False
                        counterstart3 = False
                        pressedsasuke = False
                        characterscreen1 = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move1[0] > 230 and  move1[0] < 330 and move1[1] > 100 and move1[1] < 200:
                presseditachi = False
                pressedsasuke = False
                pressedakame = True
                counterstart1 = False
                counterstart2 = False
                counterstart3 = True
        if pressedakame:
                if event.type == pygame.MOUSEBUTTONDOWN and counter3 > 10:
                    if move1[0] > 230 and  move1[0] < 330 and move1[1] > 100 and move1[1] < 200:
                        person1 = akame1
                        counter3 = 0
                        pressedakame = False
                        counterstart1 = False
                        counterstart2 = False
                        counterstart3 = False
                        characterscreen = False
                        characterscreen1 = True
    redrawCharacterScreen()

while characterscreen1:
    clock.tick(25)
    move1 = pygame.mouse.get_pos()
    select = selectcharacter2
    if counterstart1:
        counter1 += 1
    else:
        counter1 = 0
    if counterstart2:
        counter2 += 1
    else:
        counter2 = 0
    if counterstart3:
        counter3 += 1
    else:
        counter3 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            characterscreen1 = False
    if move1[0] > 10 and  move1[0] < 110 and move1[1] > 100 and move1[1] < 200:
        itachidp = True
        sasukedp = False
        akamedp = False
    elif  move1[0] > 120 and  move1[0] < 220 and move1[1] > 100 and move1[1] < 200:
        itachidp = False
        sasukedp = True
        akamedp = False
    elif  move1[0] > 230 and  move1[0] < 330 and move1[1] > 100 and move1[1] < 200:
        itachidp = False
        sasukedp = False
        akamedp = True
    else:
        itachidp = False
        sasukedp = False
        akamedp = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        if move1[0] > 10 and  move1[0] < 110 and move1[1] > 100 and move1[1] < 200:
            presseditachi = True
            counterstart1 = True
            counterstart2 = False
            pressedsasuke = False
    if presseditachi:
            if event.type == pygame.MOUSEBUTTONDOWN and counter1 > 10:
                if move1[0] > 10 and  move1[0] < 110 and move1[1] > 100 and move1[1] < 200:
                    characterscreen1 = False
                    person2 = itachi2
                    counter1 = 0
                    presseditachi = False
                    counterstart1 = False
                    counterstart2 = False
                    run = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if move1[0] > 120 and  move1[0] < 220 and move1[1] > 100 and move1[1] < 200:
            pressedsasuke = True
            pressedakame = False
            presseditachi = False
            counterstart2 = True
            counterstart1 = False
            counterstart3 = False
    if pressedsasuke:
        if event.type == pygame.MOUSEBUTTONDOWN and counter2 > 10:
            if move1[0] > 120 and  move1[0] < 220 and move1[1] > 100 and move1[1] < 200:
                    characterscreen1 = False
                    person2 = sasuke2
                    counter2 = 0
                    counterstart1 = False
                    counterstart2 = False
                    counterstart3 = False
                    pressedsasuke = False
                    run = True
    if event.type == pygame.MOUSEBUTTONDOWN:
        if move1[0] > 230 and  move1[0] < 330 and move1[1] > 100 and move1[1] < 200:
            presseditachi = False
            pressedsasuke = False
            pressedakame = True
            counterstart1 = False
            counterstart2 = False
            counterstart3 = True
    if pressedakame:
            if event.type == pygame.MOUSEBUTTONDOWN and counter3 > 10:
                if move1[0] > 230 and  move1[0] < 330 and move1[1] > 100 and move1[1] < 200:
                    person2 = akame2
                    counter3 = 0
                    pressedakame = False
                    counterstart1 = False
                    counterstart2 = False
                    counterstart3 = False
                    characterscreen1 = False
                    run = True
    redrawCharacterScreen()


while run:
    clock.tick(25)
    movement = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if alive1 == False or alive2 == False:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if movement[0] > 500 and movement[0] < 550 and movement[1] > 250 and movement[1] < 270:
                run = False
            elif movement[0] > 300 and movement[0] < 430 and movement[1] > 250 and movement[1] < 270:
                person1.x = 0
                person1.sr = True
                person1.sl = False
                person2.sr = False
                person2.sl = True
                person2.x = person2.screenw - 80
                bullets1 = []
                bullets2 = []
                person1.health = 10
                person2.health = 10
                alive1 = True
                alive2 = True

    for bullet in bullets1:
        if person1.sl:
            if bullet.y < person2.firebox[1] + person2.firebox[3] and bullet.y + 30 > person2.firebox[1]:
                if bullet.x  < person2.firebox[0] + person2.firebox[2] and bullet.x  > person2.firebox[0]:
                    print("block")
                    bullets1.pop(bullets1.index(bullet))
            if bullet.y   < person2.hitbox[1] + person2.hitbox[3] and bullet.y + 30 > person2.hitbox[1]:
                if bullet.x  > person2.hitbox[0] and bullet.x < person2.hitbox[0] + person2.hitbox[2] :
                    person1.throwdamage()
                    bullets1.pop(bullets1.index(bullet))
                    print("hello")
            for bullet2 in bullets2:
                    if bullet.y + 30 > bullet2.y  and bullet.y < bullet2.y + 30:
                        if bullet.x   < bullet2.x + 30 and bullet2.x < bullet.x + 30:
                            bullets2.pop(bullets2.index(bullet2))
                            bullets1.pop(bullets1.index(bullet))
                            print("block")
        else:
            if bullet.y <  person2.firebox[1] +  person2.firebox[3] and bullet.y + 30 >  person2.firebox[1]:
                if bullet.x + 30  >  person2.firebox[0] and bullet.x + 30  <  person2.firebox[0] + person2.firebox[2]:
                    print("block")
                    bullets1.pop(bullets1.index(bullet))
            if bullet.y < person2.hitbox[1] + person2.hitbox[3] and bullet.y + 30 > person2.hitbox[1]:
                if bullet.x + 30  > person2.hitbox[0] and bullet.x + 30 < person2.hitbox[0] + person2.hitbox[2]:
                    person1.throwdamage()
                    bullets1.pop(bullets1.index(bullet))
            for bullet2 in bullets2:
                    if bullet.y + 30 > bullet2.y  and bullet.y < bullet2.y + 30:
                        if bullet2.x   < bullet.x + 30 and bullet.x < bullet2.x + 30:
                            bullets2.pop(bullets2.index(bullet2))
                            bullets1.pop(bullets1.index(bullet))
                            print("block")
                            person1.off =  True
        if bullet.x < person1.screenw + 50 and bullet.x > -50:
            bullet.x += bullet.vel
        else:
            bullets1.pop(bullets1.index(bullet))



    person1.down = movement
    shield = projectile(person1.down[0] - 15, person1.down[1] - 15, 1)
    person1.created = True

    if alive1 and alive2:
        if  person2.hitbox[0] + person2.hitbox[2] > person1.firebox[0] and person1.firebox[0] + person1.firebox[2] >  person2.hitbox[0]:
            if person2.hitbox[1] < person1.firebox[1] + person1.firebox[3] and person2.hitbox[1]+ person2.hitbox[3] > person1.firebox[1]:
                person1.flamedamage()

        if person2.hitbox[0] > person1.firebox[0] and person1.firebox[0] + person1.firebox[2] >  person2.hitbox[0]:
            if person2.hitbox[1] < person1.firebox[1] + person1.firebox[3] and person2.hitbox[1]+ person2.hitbox[3] > person1.firebox[1]:
                person1.flamedamage()


    if keys[pygame.K_SPACE]:
        person1.throwt = True
        person1.throws = True
        person1.slash = True

    if keys[pygame.K_t]:
        person1.teleport = True
        person1.right = False
        person1.left = False


    elif keys[pygame.K_f]:
        person1.fireball = True
        person1.right = False
        person1.left = False


    elif  keys[pygame.K_a]   and person1.x > person1.vel:
        person1.x -= person1.vel
        person1.left = True
        person1.right = False
        person1.fireball = False
        person1.sl = True
        person1.sr = False


    elif keys[pygame.K_d] and person1.x < person1.screenw - person1.vel - person1.width:
        person1.x += person1.vel
        person1.left = False
        person1.right = True
        person1.fireball = False
        person1.sr = True
        person1.sl = False


    else:
        person1.right = False
        person1.left = False
        person1.walkCount = 0
        person1.fireball = False

    if not(person1.isJump):
        if  keys[pygame.K_w]:
            person1.isJump = True
            person1.left = False
            person1.right = False
            person1.walkCount = 0
    else:
        if person1.jumpCount >= -person1.jumpCountO:
            person1.y -= (person1.jumpCount * abs(person1.jumpCount)) * 0.5
            person1.jumpCount -= 1
        else:
            person1.jumpCount = person1.jumpCountO
            person1.isJump = False

    #person2

    for bullet in bullets2:
        if person2.sr:
            if bullet.y - 30  < person1.firebox[1] + person1.firebox[3] and bullet.y + 30 > person1.firebox[1]:
                if bullet.x  < person1.firebox[0] + person1.firebox[2] and bullet.x  > person1.firebox[0]:
                    print("block")
                    bullets2.pop(bullets2.index(bullet))
                    person1.off = True
            if bullet.y  < person1.hitbox[1] + person1.hitbox[3] and bullet.y + 30 > person1.hitbox[1]:
                if bullet.x + 30  > person1.hitbox[0] and bullet.x < person1.hitbox[0] + person1.hitbox[2] :
                    person2.throwdamage()
                    bullets2.pop(bullets2.index(bullet))
                    person1.off = True
        else:
            if bullet.y  <  person1.firebox[1] +  person1.firebox[3] and bullet.y + 30 >  person1.firebox[1]:
                if bullet.x + 30  >  person1.firebox[0] and bullet.x <  person1.firebox[0] + person1.firebox[2]:
                    print("block")
                    bullets2.pop(bullets2.index(bullet))
                    person1.off = True
            if bullet.y  < person1.hitbox[1] + person1.hitbox[3] and bullet.y + 30 > person1.hitbox[1]:
                if bullet.x + 30  > person1.hitbox[0] and bullet.x < person1.hitbox[0] + person1.hitbox[2]:
                    person2.throwdamage()
                    bullets2.pop(bullets2.index(bullet))
                    person1.off =  True

        if bullet.x < person2.screenw + 50 and bullet.x > - 50:
            bullet.x += bullet.vel
        else:
            bullets2.pop(bullets2.index(bullet))
            person2.off = True

    if person2.sl:
        if  person1.hitbox[0] + person1.hitbox[2] > person2.firebox[0] and person2.firebox[0] + person2.firebox[2] >  person1.hitbox[0]:
            if person1.hitbox[1] < person2.firebox[1] + person2.firebox[3] and person1.hitbox[1]+ person1.hitbox[3] > person2.firebox[1]:
                person2.flamedamage()
    else:
        if person1.hitbox[0] > person2.firebox[0] and person2.firebox[0] + person2.firebox[2] >  person1.hitbox[0]:
            if person1.hitbox[1] < person2.firebox[1] + person2.firebox[3] and person1.hitbox[1]+ person1.hitbox[3] > person2.firebox[1]:
                person2.flamedamage()

    if keys[pygame.K_RCTRL]:
        person2.throwt = True
        person2.throws = True
        person2.slash = True


    if keys[pygame.K_COMMA]:
        person2.teleport = True
        person2.right = False
        person2.left = False


    elif keys[pygame.K_PERIOD]:
        person2.fireball = True
        person2.right = False
        person2.left = False

    elif keys[pygame.K_LEFT]  and person2.x > person2.vel:
        person2.x -= person2.vel
        person2.left = True
        person2.right = False
        person2.fireball = False
        person2.sl = True
        person2.sr = False


    elif keys[pygame.K_RIGHT] and person2.x < person2.screenw - person2.vel - person2.width:
        person2.x += person2.vel
        person2.left = False
        person2.right = True
        person2.fireball = False
        person2.sr = True
        person2.sl = False


    else:
        person2.right = False
        person2.left = False
        person2.walkCount = 0
        person2.fireball = False


    if not(person2.isJump):
        if keys[pygame.K_UP]:
            person2.isJump = True
            person2.left = False
            person2.right = False
            person2.walkCount = 0
    else:
        if person2.jumpCount >= -person2.jumpCountO:
            person2.y -= (person2.jumpCount * abs(person2.jumpCount)) * 0.5
            person2.jumpCount -= 1
        else:
            person2.jumpCount = person2.jumpCountO
            person2.isJump = False


    redrawGameWindow()


pygame.quit()
