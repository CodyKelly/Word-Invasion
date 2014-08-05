import pygame, random

pygame.font.init()

fontSize = 25
fontFile = "data/cal.ttf"
font = pygame.font.Font(fontFile, fontSize)

class SlowMotionTimer(pygame.sprite.Sprite):
    def __init__(self, delay, gameObjects, multiplier):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect()
        self.delay = delay
        self.frames = 0
        self.gameObjects = gameObjects
        for obj in self.gameObjects:
            obj.speedMultiplier = multiplier
    def update(self):
        if self.frames < self.delay:
            self.frames += 1
        else:
            for obj in self.gameObjects:
                obj.speedMultiplier = 1
            self.kill()

class WordObject(pygame.sprite.Sprite):
    def __init__(self, string, player, windowRect, gameObjects):
        pygame.sprite.Sprite.__init__(self)
        self.gameObjects = gameObjects
        self.windowRect = windowRect #rect to check if out of bounds
        self.string = string
        self.image = font.render(self.string, 1, (0,0,0), (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.windowRect.width - self.rect.width)
        self.rect.y = 0-self.rect.height
        self.speed = random.randint(1,3)
        self.speedMultiplier = 1.0 #to change speed
        self.player = player #the player instance
        self.hurtValue = -15 #damage done to player
    def set_bgcolor(self, color):
        self.image = font.render(self.string, 1, (0,0,0), color)
    def set_speed_multiplier(self, multiplier):
        self.speedMultiplier = multiplier
    def update(self):
        if self.rect.y > self.windowRect.height:
            self.player.change_health(self.hurtValue)
            self.kill()
        else:
            self.rect.y += self.speed * self.speedMultiplier

class NormalWord(WordObject):
    def __init__(self, string, player, windowRect, gameObjects):
        WordObject.__init__(self, string, player, windowRect, gameObjects)
    def activate(self):
        self.kill()

class HealthWord(WordObject):
    def __init__(self, string, player, windowRect, gameObjects):
        WordObject.__init__(self, string, player, windowRect, gameObjects)
        self.set_bgcolor((255,150,150))
        self.healValue = 15
    def activate(self):
        self.player.change_health(self.healValue)
        self.kill()

class BombWord(WordObject):
    def __init__(self, string, player, windowRect, gameObjects):
        WordObject.__init__(self, string, player, windowRect, gameObjects)
        self.set_bgcolor((150,150,255))
    def activate(self):
        self.gameObjects.empty()
        self.kill()

class SlowMotionWord(WordObject):
    def __init__(self, string, player, windowRect, gameObjects):
        WordObject.__init__(self, string, player, windowRect, gameObjects)
        self.set_bgcolor((150,255,150))
    def activate(self):
        self.gameObjects.add(SlowMotionTimer(1000, self.gameObjects, 0.5))
        self.kill()