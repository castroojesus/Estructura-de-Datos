import json
import os
import pygame

SAVE_FILE = "savegame.json"

class GameManager:
    def __init__(self):
        self.save_file = SAVE_FILE

    def guardar_partida(self, jugador, contador_salida,generador):
        data = {
            "nivel": contador_salida,
            "puntos": jugador.puntos,
            "vidas": jugador.vidaactual,
            "energia": jugador.energia,
            "llaves": jugador.inventario.llaves,
            "items": jugador.inventario.items,
            "laberinto":generador.maze,
            "trampas": [[t.x, t.y, t.activada] for t in generador.trampas],
            "tesoros": [[t.x, t.y, t.recolectado, t.nombre] for t in generador.tesoros],
            "llaves_obj": [[l.x, l.y, l.encontrada] for l in generador.llave]
        }
        with open(self.save_file, "w") as f:
            json.dump(data, f)
        print("Partida guardada correctamente.")

    def cargar_partida(self, jugador):
        if not os.path.exists(self.save_file):
            print("No hay partida guardada.")
            return 0

        with open(self.save_file, "r") as f:
            data = json.load(f)

        jugador.puntos = data["puntos"]
        jugador.vidaactual = data["vidas"]
        jugador.energia = data["energia"]
        jugador.inventario.llaves = data["llaves"]
        jugador.inventario.items = data["items"]
        jugador.llaves = jugador.inventario.llaves

        print(f"🔄 Partida cargada — Nivel {data['nivel']}, {jugador.puntos} puntos")
        return data["nivel"]

    def mostrar_menu_pausa(self, ventana, jugador, contador_salida, generador):
        pausado = True
        fuente = pygame.font.Font(None, 36)

        while pausado:
            ventana.fill((0, 0, 0))

            opciones = [
                fuente.render("PAUSA", True, (255, 255, 255)),
                fuente.render("1. Guardar partida", True, (200, 200, 0)),
                fuente.render("2. Salir del juego", True, (255, 0, 0)),
                fuente.render("3. Continuar", True, (0, 255, 0))
            ]

            ventana.blit(opciones[0], (250, 200))
            ventana.blit(opciones[1], (200, 250))
            ventana.blit(opciones[2], (200, 300))
            ventana.blit(opciones[3], (200, 350))

            pygame.display.flip()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_1:
                        self.guardar_partida(jugador, contador_salida,generador)
                    elif e.key == pygame.K_2:
                        print("Saliendo del juego...")
                        pygame.quit()
                        exit()
                    elif e.key == pygame.K_3:
                        pausado = False