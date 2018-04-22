import pygame


pygame.init()
pygame.mixer.music.load('m01.mp3')
pygame.mixer.music.play()
pygame.event.wait()
