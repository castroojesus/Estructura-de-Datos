# PRIMERA REVISION 14/10/25

import pygame
import constantes as const
from personaje import Personaje
from maze import MazeGenerator
from game_manager import GameManager
import json
import time
from rankings import guardar_ranking,mostrar_rankings,pedir_nombre

pygame.init()
inicio=time.time()
manager=GameManager()
partida_guardada=False
def scaleimage(image, scale):
    w = image.get_width()
    h = image.get_height()
    newimage = pygame.transform.scale(image, (w*scale, h*scale))
    return newimage

def loadimage():

    imagen_abajo = pygame.image.load("player/pj _abajo-1.png.png")
    imagen_arriba = pygame.image.load("player/pj_arriba-1.png.png")
    imagen_izquierda = pygame.image.load("player/pj_izquierda-1.png.png")
    imagen_derecha = pygame.image.load("player/pj_derecha-1.png.png")



    escala = const.ESCALA
    imagenes = {
        'abajo': scaleimage(imagen_abajo, escala),
        'arriba': scaleimage(imagen_arriba, escala),
        'izquierda': scaleimage(imagen_izquierda, escala),
        'derecha': scaleimage(imagen_derecha, escala)
    }


    return imagenes

respuesta = input("¿Quieres cargar una partida guardada? (s/n): ").lower()

if respuesta == "s":

    try:
        with open("savegame.json", "r") as f:
            datos = json.load(f)
            print("Partida cargada exitosamente 🎮")

            generador = MazeGenerator(20, 20)
            generador.maze=datos["laberinto"]
            entrada = generador.get_entry_pos()
            salida = generador.get_exit_pos()

            jugador_x = entrada[1] * const.tileSize
            jugador_y = entrada[0] * const.tileSize
            jugador = Personaje(jugador_x, jugador_y, loadimage())

            jugador.puntos = datos["puntos"]
            jugador.vidaactual = datos["vidas"]
            jugador.energia = datos["energia"]
            jugador.inventario.llaves = datos["llaves"]
            jugador.inventario.items = datos["items"]
            contador_salida = datos["nivel"]
            for t, d in zip(generador.trampas, datos.get("trampas", [])):
                t.x, t.y, t.activada = d

            for t, d in zip(generador.tesoros, datos.get("tesoros", [])):
                t.x, t.y, t.recolectado, t.nombre = d

            for l, d in zip(generador.llave, datos.get("llaves_obj", [])):
                l.x, l.y, l.encontrada = d

            partida_guardada = True

    except FileNotFoundError:
        print("No hay partida guardada, iniciando nueva 😅")
        generador = MazeGenerator(20, 20)
else:
    generador = MazeGenerator(20, 20)

if not partida_guardada or contador_salida>=3:
    generador = MazeGenerator(20,20)
    entrada = generador.get_entry_pos()
    salida = generador.get_exit_pos()

    jugador_x = entrada[1] * const.tileSize
    jugador_y = entrada[0] * const.tileSize
    jugador = Personaje(jugador_x, jugador_y, loadimage())

    contador_salida = 0

def verificar_salida(jugador, salida_pos, tileSize):

    celda_x = jugador.shape.x // tileSize
    celda_y = jugador.shape.y // tileSize

    if (celda_x, celda_y) == (salida_pos[1], salida_pos[0]):
        if jugador.llaves > 0:

            return True
        else:
            print("🔒 Necesitas una llave para salir")
            return False
    return False


# creo la ventana que va a ser del tamaño que asigne en constantes
ventana = pygame.display.set_mode((const.screenWidth, const.screenHeight))




# titulo de la ventana
pygame.display.set_caption("TREASURE HUNT")

moveUp = False
moveDown = False
moveLeft = False
moveRight = False



reloj=pygame.time.Clock()
mostrar_inventario=False

run = True
while run:

    fullheart = pygame.image.load("player/fullheart.png")
    voidheart = pygame.image.load("player/voidheart.png")
    fullheart = pygame.transform.scale(fullheart, (const.tileSize, const.tileSize))
    voidheart = pygame.transform.scale(voidheart, (const.tileSize, const.tileSize))

    fullenergy = pygame.image.load("player/fullenergy.png")
    voidenergy = pygame.image.load("player/voidenergy.png")
    fullenergy = pygame.transform.scale(fullenergy, (const.tileSize, const.tileSize))
    voidenergy = pygame.transform.scale(voidenergy, (const.tileSize, const.tileSize))

    generador.dibujar_laberinto(ventana, const.tileSize,const.COLORES_LABERINTO)

    # hago que el movimiento de mi personaje sea en 60fps
    reloj.tick(const.FPS)

    jugador.dibujar(ventana)
    jugador.dibujar_vidas(ventana,fullheart,voidheart)
    jugador.dibujar_energia(ventana, fullenergy, voidenergy)

    if mostrar_inventario:
        jugador.inventario.dibujar(ventana, 400, 50)

    # Mostrar puntos en pantalla
    fuente = pygame.font.Font(None, 24)
    puntos_texto = fuente.render(f"Puntos: {jugador.puntos}", True, (255, 255, 0))
    ventana.blit(puntos_texto, (10, 590))

    if not jugador.esta_vivo():
        print("¡Game Over!")
        # Aquí puedes reiniciar el juego o mostrar pantalla de game over
        jugador.resetear_vidas()
        nombre = pedir_nombre(ventana)
        tiempo_total=time.time()-inicio
        guardar_ranking(nombre, jugador.puntos, tiempo_total, contador_salida)
        mostrar_rankings(ventana)


        break
    trampas = generador.get_trampas()
    tesoros = generador.get_tesoros()
    llave = generador.get_llave()
    salida = generador.get_exit_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:



            if event.key == pygame.K_a:
                if jugador.mover_tile(-1, 0, generador, salida,trampas,tesoros,llave):
                    celda_x = jugador.shape.x // const.tileSize
                    celda_y = jugador.shape.y // const.tileSize
                    generador.marcar_camino(celda_x, celda_y)
            elif event.key == pygame.K_d:
                if jugador.mover_tile(1, 0, generador, salida,trampas,tesoros,llave):
                    celda_x = jugador.shape.x // const.tileSize
                    celda_y = jugador.shape.y // const.tileSize
                    generador.marcar_camino(celda_x, celda_y)
            elif event.key == pygame.K_w:
                if jugador.mover_tile(0, -1, generador, salida,trampas,tesoros, llave):
                    celda_x = jugador.shape.x // const.tileSize
                    celda_y = jugador.shape.y // const.tileSize
                    generador.marcar_camino(celda_x, celda_y)
            elif event.key == pygame.K_s:
                if jugador.mover_tile(0, 1, generador, salida,trampas,tesoros, llave):
                    celda_x = jugador.shape.x // const.tileSize
                    celda_y = jugador.shape.y // const.tileSize
                    generador.marcar_camino(celda_x, celda_y)
            elif event.key == pygame.K_i:
                mostrar_inventario = not mostrar_inventario
            elif event.key == pygame.K_ESCAPE:
                manager.mostrar_menu_pausa(ventana, jugador, contador_salida,generador)

            # Permitir movimiento inmediatamente después
            jugador.permitir_movimiento()

    if verificar_salida(jugador, salida, const.tileSize) and not nivel_transicion:
        print("🎉 ¡Felicidades! Pasaste al siguiente nivel!")
        contador_salida += 1
        print(f"Nivel actual: {contador_salida}")

        nivel_transicion = True

        generador.next_level()

        jugador.inventario.llaves = 0
        jugador.inventario.items = [item for item in jugador.inventario.items if item[0] != "Llave"]

        salida=generador.get_exit_pos()
        llave=generador.get_llave()
        trampas=generador.get_trampas()
        tesoros=generador.get_tesoros()


        entrada = generador.get_entry_pos()
        jugador.shape.x = entrada[1] * const.tileSize
        jugador.shape.y = entrada[0] * const.tileSize
        jugador.inventario.items = [
            item for item in jugador.inventario.items
            if item[0] not in [t.nombre for t in tesoros]
        ]
        # Sincronizar atributo rápido para verificar salida
        jugador.llaves = jugador.inventario.llaves

        if contador_salida>=3:
            print("Haz ganado el juego")
            nombre = pedir_nombre(ventana)
            tiempo_total = time.time() - inicio
            guardar_ranking(nombre, jugador.puntos, tiempo_total, contador_salida)
            mostrar_rankings(ventana)
            break


    keys = pygame.key.get_pressed()
    if any([keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_s], keys[pygame.K_d]]):
        nivel_transicion = False

    pygame.display.update()

pygame.quit()