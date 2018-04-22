import os
import pygame

pygame.init()
size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)  # define o tamanho da tela
ball = pygame.image.load("ball.pnj")    # carrega a imagem da bola
ballrect = ball.get_rect()
while (1):                                # cria um loop infinito
    for event in pygame.event.get():    # se houver algum evento do usuário,
        if event.type == pygame.QUIT:   # o programa termina
           sys.exit()

# movimentação da bola e atualização da tela
    ballrect = ballrect.move(speed)
    if (ballrect.left < 0 or ballrect.right > width):
       speed[0] = -speed[0]
    if (ballrect.top < 0 or ballrect.bottom > height):
       speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
