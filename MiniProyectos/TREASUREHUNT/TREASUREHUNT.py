# PRIMERA REVISION 14/10/25

import pygame
import constantes
from personajes import Personaje
from maze import MazeGenerator
from items import GeneradorTrampas
from Iluminacion import SistemaIluminacion
from exploracion import MapaExploracion
from items import GeneradorTesoros

def verificar_salida(jugador_x, jugador_y, salida_pos, tile_size):
    """Verifica si el jugador llegó a la salida con tolerancia"""
    # Convertirtodo a coordenadas de celdas
    jugador_celda_x = jugador_x // tile_size
    jugador_celda_y = jugador_y // tile_size

    # Salida está en formato (fila, columna), convertir a (columna, fila)
    salida_celda_x = salida_pos[1]  # columna
    salida_celda_y = salida_pos[0]  # fila

    # Verificar coincidencia
    en_salida = (jugador_celda_x == salida_celda_x and jugador_celda_y == salida_celda_y)

    if en_salida:
        print(
            f"✅ ¡Salida encontrada! Jugador: ({jugador_celda_x}, {jugador_celda_y}), Salida: ({salida_celda_x}, {salida_celda_y})")

    return en_salida

pygame.init()
# asigno mi clase a la variable generador
generador = MazeGenerator(20, 20)
celdas_visitadas = []

sistema_iluminacion = SistemaIluminacion(20, 20, constantes.tileSize)
# variable para obtener la posicion de la salida
salida=generador.get_exit_pos()

# entrada del laberinto
entrada=generador.get_entry_pos()

celdas_visitadas.append(entrada)
mapa_exploracion=MapaExploracion(20,20,constantes.tileSize)
# variable que hereda de la clase de trampas
trampas = GeneradorTrampas.crear_trampas(generador.get_maze(), 5,entrada, salida)
tesoros=GeneradorTesoros.crear_tesoros(generador.get_maze(), 5, entrada, salida)


# funcion para escalar mi sprite al tamaño de la figura
def scaleimage(image, scale):
    w = image.get_width()
    h = image.get_height()
    newimage = pygame.transform.scale(image, (w*scale, h*scale))
    return newimage

def loadimage():
    # Cargar imágenes para cada dirección
    imagen_abajo = pygame.image.load("player/pj_abajo.png")
    imagen_arriba = pygame.image.load("player/pj_arriba.png")
    imagen_izquierda = pygame.image.load("player/pj_izquierda.png")
    imagen_derecha = pygame.image.load("player/pj_derecha.png")

    # Escalar imágenes
    escala = constantes.ESCALA
    imagenes = {
        'abajo': scaleimage(imagen_abajo, escala),
        'arriba': scaleimage(imagen_arriba, escala),
        'izquierda': scaleimage(imagen_izquierda, escala),
        'derecha': scaleimage(imagen_derecha, escala)
    }


    return imagenes

#caargo la imagen de mi jugador
player_image= loadimage()

#asigno la varibale de posicion inicial
start_pos = generador.get_entry_pos()

#coordenadas x, y para el personaje
jugador_x = start_pos[1] * constantes.tileSize  # Columna → X
jugador_y = start_pos[0] * constantes.tileSize  # Fila → Y

# declaro mi personaje con las coordenadas y la imagen
jugador = Personaje(jugador_x, jugador_y, player_image)

COLORES_LABERINTO = {
    'PARED': (0, 0, 0),  # Negro
    'CAMINO': (255, 255, 255),  # Blanco
    'INICIO': (0, 255, 0),  # Verde
    'FIN': (255, 0, 0)  # Rojo
}

mapa_exploracion.marcar_pisada(entrada[0], entrada[1])
# creo la ventana que va a ser del tamaño que asigne en constantes
ventana = pygame.display.set_mode((constantes.screenWidth, constantes.screenHeight))

# titulo de la ventana
pygame.display.set_caption("TREASURE HUNT")


moveUp = False
moveDown = False
moveLeft = False
moveRight = False



reloj=pygame.time.Clock()
run=True


while run:

    reloj.tick(constantes.FPS)

    
    


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

    laberinto_actual = generador.get_maze()

    for trampa in trampas:
        trampa.dibujar(ventana)

        # Verificar colisiones jugador-trampas
    for trampa in trampas:
        if jugador.shape.colliderect(trampa.forma):
            print("¡Has caído en una trampa!")

    for tesoro in tesoros:
        tesoro.dibujar(ventana)

    for tesoro in tesoros:
        if jugador.shape.colliderect(tesoro.forma):
            print("Has encontrado un tesoro!")


    if moveLeft:
        jugador.mover_tile(-1, 0, laberinto_actual,salida)
    elif moveRight:
        jugador.mover_tile(1, 0, laberinto_actual,salida)
    elif moveUp:
        jugador.mover_tile(0, -1, laberinto_actual,salida)
    elif moveDown:
        jugador.mover_tile(0, 1, laberinto_actual,salida)



    jugador_celda_x = jugador.shape.x // constantes.tileSize
    jugador_celda_y = jugador.shape.y // constantes.tileSize

    if verificar_salida(jugador.shape.x, jugador.shape.y, salida, constantes.tileSize):
        print("🎉 ¡Felicidades! Ganaste el juego")

    sistema_iluminacion.actualizar_iluminacion((jugador.shape.x, jugador.shape.y))
    ventana.fill(COLORES_LABERINTO['PARED'])

    sistema_iluminacion.dibujar_laberinto_iluminado(
        ventana,
        laberinto_actual,
        (entrada[1], entrada[0]),  # (columna, fila) ← CORREGIDO
        (salida[1], salida[0])  # (columna, fila) ← CORREGIDO
    )



    sistema_iluminacion.dibujar_entidades_iluminadas(ventana, trampas,tesoros)

    # APLICAR EFECTO DE OSCURIDAD
    sistema_iluminacion.dibujar_overlay_oscuridad(ventana)







        # dibujo al jugador
    jugador.dibujar(ventana)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            laberinto_actual = generador.get_maze()

            if event.key == pygame.K_a:
                jugador.mover_tile(-1, 0, laberinto_actual,salida)
            elif event.key == pygame.K_d:
                jugador.mover_tile(1, 0, laberinto_actual,salida)
            elif event.key == pygame.K_w:
                jugador.mover_tile(0, -1, laberinto_actual,salida)
            elif event.key == pygame.K_s:
                jugador.mover_tile(0, 1, laberinto_actual,salida)

            # Permitir movimiento inmediatamente después
            jugador.permitir_movimiento()

    pygame.display.update()
pygame.quit()


