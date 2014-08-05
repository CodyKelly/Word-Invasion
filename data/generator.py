__author__ = 'lizardfingers'

import pygame, random, wordobjects

class Generator(object):
    def __init__(self, windowRect, player):
        self.player = player
        self.rect = pygame.Rect
        self.windowRect = windowRect
        self.wordList = self.read_words('data/words.txt')
        self.delay = 100
        self.frames = 0
        self.wordObjectTypes = [
            wordobjects.NormalWord,
            wordobjects.HealthWord
        ]
    def read_words(self, words_file):
        return [word for line in open(words_file, 'r') for word in line.split()]
    def update(self, gameObjects):
        if self.frames < self.delay:
            self.frames += 1
        else:
            self.frames = 0
            word = self.get_random_word()
            gameObjects.add(self.get_wordObject()(word, self.player, self.windowRect))
    def get_wordObject(self):
        return random.choice(self.wordObjectTypes)
    def get_random_word(self):
        return random.choice(self.wordList)