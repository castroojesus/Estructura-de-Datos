import pygame
import constantes
from personajes import Personaje
from maze import GeneradorLaberinto







pygame.init()
generador = GeneradorLaberinto(constantes.tileSize, 20)


def scaleimage(image, scale):
    w = image.get_width()
    h = image.get_height()
    newimage = pygame.transform.scale(image, (w*scale, h*scale))
    return newimage

player_image=pygame.image.load("player/pj_1.png")
player_image= scaleimage(player_image,constantes.ESCALA)
start_pos = generador.obtener_posicion_inicio()


jugador_x = start_pos[1] * generador.cell_size  # Columna * tamaño_celda
jugador_y = start_pos[0] * generador.cell_size  # Fila * tamaño_celda
jugador = Personaje(jugador_x, jugador_y, player_image)

# Generar laberinto completo
generador.generar_completo()



ventana = pygame.display.set_mode(generador.obtener_dimensiones())
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
    generador.dibujar_laberinto(ventana)

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
