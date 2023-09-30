import pygame

pygame.init()

class Input:
    @staticmethod
    def detect(key, action):
        keys = pygame.key.get_pressed()
        if keys[key]:
            action()
