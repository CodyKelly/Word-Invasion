__author__ = 'lizardfingers'

import pygame, sys
import generator
import player

pygame.init()

windowRect = pygame.Rect((0,0),(1000, 800))

screen = pygame.display.set_mode(windowRect.size)

WHITE = (255,255,255)

clock = pygame.time.Clock()

caption = 'Word Invasion'
pygame.display.set_caption(caption)

def run():

    #initialize everything
    player_ = player.Player(windowRect)
    generator.init(windowRect, player_)
    gameObjects = pygame.sprite.Group()

    #game loop
    while(player_.isAlive):
        clock.tick(60)
        screen.fill(WHITE)

        events = pygame.event.get()

        #gotta check for quit
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #update everything
        generator.update(gameObjects)
        player_.update(events, gameObjects)
        gameObjects.update()

        #draw everything
        player_.draw(screen)
        gameObjects.draw(screen)

        pygame.display.update()