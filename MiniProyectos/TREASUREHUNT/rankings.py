import pygame
import json
import os
import time

RANKINGS_FILE = "rankings.json"

# Guardar ranking
def guardar_ranking(nombre, puntos, tiempo, nivel):
    if not os.path.exists(RANKINGS_FILE):
        with open(RANKINGS_FILE, "w") as f:
            json.dump([], f)

    with open(RANKINGS_FILE, "r") as f:
        rankings = json.load(f)

    rankings.append({
        "nombre": nombre,
        "puntos": puntos,
        "tiempo": tiempo,
        "nivel": nivel
    })

    rankings.sort(key=lambda x: (-x["puntos"], x["tiempo"]))

    with open(RANKINGS_FILE, "w") as f:
        json.dump(rankings, f, indent=4)

# Mostrar ranking en Pygame
def mostrar_rankings(ventana, top=5):
    ventana.fill((0,0,0))
    fuente_titulo = pygame.font.Font(None, 50)
    fuente = pygame.font.Font(None, 36)

    titulo = fuente_titulo.render("Ranking", True, (255, 215, 0))
    ventana.blit(titulo, (ventana.get_width()//2 - titulo.get_width()//2, 50))

    if not os.path.exists(RANKINGS_FILE):
        texto = fuente.render("No hay rankings aún", True, (255,255,255))
        ventana.blit(texto, (ventana.get_width()//2 - texto.get_width()//2, 150))
    else:
        with open(RANKINGS_FILE, "r") as f:
            rankings = json.load(f)

        for i, entry in enumerate(rankings[:top]):
            texto = fuente.render(
                f"{i+1}. {entry['nombre']} - {entry['puntos']} pts - {entry['tiempo']:.1f}s - Nivel {entry['nivel']}",
                True, (255,255,255)
            )
            ventana.blit(texto, (50, 150 + i*50))

    pygame.display.flip()

    # Esperar a que el jugador cierre la ventana o presione cualquier tecla
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                esperando = False


def pedir_nombre(ventana):
    nombre = ""
    fuente = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    escribiendo = True

    while escribiendo:
        ventana.fill((0, 0, 0))
        texto = fuente.render(f"Ingresa tu nombre: {nombre}", True, (255, 255, 255))
        ventana.blit(texto, (50, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    escribiendo = False
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode

        clock.tick(30)
    return nombre