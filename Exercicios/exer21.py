import pygame # pip3 install pygame --upgrade


pygame.init()
pygame.mixer.music.load('m01.mp3')
pygame.mixer.music.play()
pygame.event.wait()
