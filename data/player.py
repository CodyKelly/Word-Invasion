import pygame, eztext, math

pygame.font.init()
pygame.mixer.init()

laserSound = pygame.mixer.Sound('data/sfx/laser.ogg')

fontSize = 32
fontFile = "data/cal.ttf"
font_ = pygame.font.Font(fontFile, fontSize)

class Turret(object):
    def __init__(self, windowRect):
        self.x, self.y = windowRect.midbottom
        self.angle = 0
    def shoot(self, pos):
        (x,y) = pos
        diffX = x - self.x
        diffY = y - self.y
        newAngle = math.atan2(diffY, diffX)*180/math.pi


class Player(object):
    def __init__(self, windowRect):
        self.health = 100
        self.isAlive = True
        self.healthBarWidth = 25
        self.windowRect = windowRect
        self.text = eztext.Input(x=5,y=windowRect.height-self.healthBarWidth-32,font=font_, prompt='> ')
        self.lastWord = ''
    def update(self, events, gameObjects):
        self.text.update(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    for obj in gameObjects:
                        if obj.string == self.text.value:
                            # laserSound.play()
                            # this got a little annoying, maybe one day
                            obj.activate()
                    self.lastWord = self.text.value
                    self.text.value = ''
                if event.key == pygame.K_UP:
                    self.text.value = self.lastWord
        if self.health <= 0:
            self.isAlive = False
    def draw(self, screen):
        self.text.draw(screen)
        healthBarY = self.windowRect.height - self.healthBarWidth/2
        healthBarStartPos = (0, healthBarY)
        healthBarEndPos = (self.health * self.windowRect.width / 100, healthBarY)
        pygame.draw.line(screen, (255,0,0), healthBarStartPos, healthBarEndPos, self.healthBarWidth)
    def change_health(self,value):
        if self.health + value > 100:
            self.health = 100
        else:
            self.health += value
