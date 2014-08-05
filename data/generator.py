__author__ = 'lizardfingers'

import pygame, random, wordobjects

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

wordList = read_words('data/words.txt')

class Generator(object):
    def __init__(self, windowRect, player):
        self.player = player
        self.rect = pygame.Rect
        self.windowRect = windowRect
        self.delay = 100
        self.frames = 0
        self.wordObject = None
    def update(self, wordGroup):
        if self.frames < self.delay:
            self.frames += 1
        else:
            self.frames = 0
            word = self.get_random_word()
            wordGroup.add(self.wordObject(word, self.player, self.windowRect, wordGroup))
    def get_wordObject(self):
        return random.choice(self.wordObjectTypes)
    def get_random_word(self):
        return random.choice(wordList)

class SpecialWordGenerator(Generator):
    def __init__(self, windowRect, player):
        Generator.__init__(self, windowRect, player)
        self.delay = 2500 #2500
        self.wordObjects = [
            wordobjects.BombWord,
            # wordobjects.SlowMotionWord # still have to work out some kinks
        ]
    def update(self, wordGroup):
        if self.frames < self.delay:
            self.frames += 1
        else:
            self.frames = 0
            word = self.get_random_word()
            wordObject = random.choice(self.wordObjects)
            wordGroup.add(wordObject(word, self.player, self.windowRect, wordGroup))

class HealthWordGenerator(Generator):
    def __init__(self, windowRect, player):
        Generator.__init__(self, windowRect, player)
        self.wordObject = wordobjects.HealthWord
        self.delay = 800

class WordGenerator(Generator):
    def __init__(self, windowRect, player):
        Generator.__init__(self, windowRect, player)
        self.wordObject = wordobjects.NormalWord
        self.delay = 150 #150

generators = []
def init(windowRect, player):
    global generators
    generators = [
    WordGenerator(windowRect, player),
    HealthWordGenerator(windowRect, player),
    SpecialWordGenerator(windowRect, player)
    ]

def update(wordGroup):
    for g in generators:
        g.update(wordGroup)