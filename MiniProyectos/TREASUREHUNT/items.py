import pygame
import random
import constantes as cons
from maze import MazeGenerator

class Trampas:
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, cons.tileSize, cons.tileSize)
        self.forma.x = x * cons.tileSize
        self.forma.y = y * cons.tileSize

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, (255, 0, 0), self.forma, 1)  # Debug

class GeneradorTrampas:
    @staticmethod
    def crear_trampas(laberinto, cantidad,  entrada,posicion_salida):
        """Crea trampas solo en callejones sin salida, excluyendo la salida"""
        trampas = []


        # Encontrar callejones sin salida
        callejones = GeneradorTrampas.encontrar_callejones_sin_salida(laberinto,entrada, posicion_salida)

        print(f"✓ Se encontraron {len(callejones)} callejones sin salida")

        # Seleccionar callejones aleatorios para trampas
        if len(callejones) >= cantidad:
            posiciones = random.sample(callejones, cantidad)
        else:
            posiciones = callejones  # Usar todos los disponibles

        # Crear trampas en callejones
        for fila, columna in posiciones:
            trampa = Trampas(columna, fila)
            trampas.append(trampa)

        print(f"✓ Se crearon {len(trampas)} trampas en callejones sin salida")
        return trampas

    @staticmethod
    def encontrar_callejones_sin_salida(laberinto, entrada,posicion_salida):
        """Encuentra todas las celdas que son callejones sin salida, excluyendo la salida"""
        callejones = []
        filas = len(laberinto)
        columnas = len(laberinto[0])

        for fila in range(filas):
            for columna in range(columnas):
                if GeneradorTrampas.es_callejon_sin_salida(laberinto, fila, columna,entrada, posicion_salida):
                    callejones.append((fila, columna))

        return callejones

    @staticmethod
    def es_callejon_sin_salida(laberinto, fila, columna, entrada, posicion_salida):
        """Verifica si una celda es un callejón sin salida, excluyendo la salida"""
        # Solo considerar celdas que son caminos
        if laberinto[fila][columna] != 0:
            return False

        # NO puede ser la salida
        if posicion_salida and (fila, columna) == posicion_salida:
            return False

        if entrada and (fila,columna)==entrada:
            return False


        # Contar vecinos que son caminos (no paredes)
        vecinos_camino = 0
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba

        for df, dc in direcciones:
            nf, nc = fila + df, columna + dc
            if (0 <= nf < len(laberinto) and
                    0 <= nc < len(laberinto[0]) and
                    laberinto[nf][nc] == 0):
                vecinos_camino += 1

        # Un callejón sin salida tiene exactamente 1 vecino camino (solo una entrada/salida)
        return vecinos_camino == 1

class Tesoros:
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, cons.tileSize, cons.tileSize)
        self.forma.x = x * cons.tileSize
        self.forma.y = y * cons.tileSize

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, (255, 0, 0), self.forma, 1)  # Debug


class GeneradorTesoros:
    @staticmethod
    def crear_tesoros(laberinto, cantidad, entrada, posicion_salida):
        """Crea trampas solo en callejones sin salida, excluyendo la salida"""
        tesoros = []

        # Encontrar callejones sin salida
        caminos = GeneradorTesoros.encontrar_canminos(laberinto, entrada, posicion_salida)



        # Seleccionar callejones aleatorios para trampas
        if len(caminos) >= cantidad:
            posiciones = random.sample(caminos, cantidad)
        else:
            posiciones = caminos  # Usar todos los disponibles

        # Crear trampas en callejones
        for fila, columna in posiciones:
            tesoro = Tesoros(columna, fila)
            tesoros.append(tesoro)

        print(f"✓ Se crearon {len(tesoros)} trampas en callejones sin salida")
        return tesoros

    @staticmethod
    def encontrar_canminos(laberinto, entrada, posicion_salida):
        """Encuentra todas las celdas que son callejones sin salida, excluyendo la salida"""
        caminos = []
        filas = len(laberinto)
        columnas = len(laberinto[0])

        for fila in range(filas):
            for columna in range(columnas):
                if GeneradorTesoros.es_camino(laberinto, fila, columna, entrada, posicion_salida):
                    caminos.append((fila, columna))

        return caminos

    @staticmethod
    def es_camino(laberinto, fila, columna, entrada, posicion_salida):
        """Verifica si una celda es un callejón sin salida, excluyendo la salida"""
        # Solo considerar celdas que son caminos
        if laberinto[fila][columna] != 0:
            return False

        # NO puede ser la salida
        if posicion_salida and (fila, columna) == posicion_salida:
            return False

        if entrada and (fila, columna) == entrada:
            return False

        # Contar vecinos que son caminos (no paredes)
        vecinos_camino = 0
        direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # derecha, abajo, izquierda, arriba

        for df, dc in direcciones:
            nf, nc = fila + df, columna + dc
            if (0 <= nf < len(laberinto) and
                    0 <= nc < len(laberinto[0]) and
                    laberinto[nf][nc] == 0):
                vecinos_camino += 1

        # Un callejón sin salida tiene exactamente 1 vecino camino (solo una entrada/salida)
        return vecinos_camino == 0