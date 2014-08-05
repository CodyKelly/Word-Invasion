import pygame, eztext

pygame.font.init()

fontSize = 32
fontFile = "data/cal.ttf"
font_ = pygame.font.Font(fontFile, fontSize)

class Player(object):
    def __init__(self, windowRect):
        self.health = 100
        self.isAlive = True
        self.healthBarWidth = 20
        self.windowRect = windowRect
        self.text = eztext.Input(x=0,y=windowRect.height-self.healthBarWidth-32,font=font_)
    def update(self, events, gameObjects):
        self.text.update(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    for obj in gameObjects:
                        if obj.string == self.text.value:
                            obj.activate()
                    self.text.value = ''
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
