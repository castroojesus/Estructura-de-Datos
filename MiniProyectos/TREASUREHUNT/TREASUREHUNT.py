import pygame
import constantes
from personajes import Personaje

jugador=Personaje(50,50)

pygame.init()


ventana = pygame.display.set_mode((constantes.screenWidth , constantes.screenHeight))
pygame.display.set_caption("TREASURE HUNT")


moveUp = False
moveDown = False
moveLeft = False
moveRight = False

reloj=pygame.time.Clock()
run=True

while run:

    reloj.tick(constantes.FPS)

    ventana.fill(constantes.BackgroundColor)

    deltax=0
    delta_y=0

    if moveLeft == True:
        deltax=-5
    if moveRight == True:
        deltax=5
    if moveDown == True:
        delta_y=5
    if moveUp == True:
        delta_y=-5



    jugador.movement(deltax, delta_y)

    jugador.dibujar(ventana)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moveLeft = True
            if event.key == pygame.K_d:
                moveRight = True
            if event.key == pygame.K_w:
                moveUp = True
            if event.key == pygame.K_s:
                moveDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moveLeft = False
            if event.key == pygame.K_d:
                moveRight = False
            if event.key == pygame.K_w:
                moveUp = False
            if event.key == pygame.K_s:
                moveDown = False

    pygame.display.update()
pygame.quit()
