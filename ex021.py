import pygame

pygame.init()
pygame.mixer.music.load('../mhrap.mp3')
pygame.mixer.music.play()
pygame.event.wait()
