__author__ = 'lizardfingers'

import pygame, random, wordobjects

def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

wordList = read_words('data/words.txt')

class Generator(object):
    def __init__(self, windowRect, player, wordObject, delay):
        self.player = player
        self.rect = pygame.Rect
        self.windowRect = windowRect
        self.delay = delay
        self.frames = 0
        self.wordObject = wordObject
    def update(self, gameObjects):
        if self.frames < self.delay:
            self.frames += 1
        else:
            self.frames = 0
            word = self.get_random_word()
            gameObjects.add(self.wordObject(word, self.player, self.windowRect, gameObjects))
    def get_wordObject(self):
        return random.choice(self.wordObjectTypes)
    def get_random_word(self):
        return random.choice(wordList)

class BombWordGenerator(Generator):
    def __init__(self, windowRect, player):
        Generator.__init__(self, windowRect, player, wordobjects.BombWord, 2500)

class HealthWordGenerator(Generator):
    def __init__(self, windowRect, player):
        Generator.__init__(self, windowRect, player, wordobjects.HealthWord, 800)

class WordGenerator(Generator):
    def __init__(self, windowRect, player):
        Generator.__init__(self, windowRect, player, wordobjects.NormalWord, 150)

generators = []
def init(windowRect, player):
    global generators
    generators = [
    WordGenerator(windowRect, player),
    HealthWordGenerator(windowRect, player),
    BombWordGenerator(windowRect, player)
    ]

def update(gameObjects):
    for g in generators:
        g.update(gameObjects)