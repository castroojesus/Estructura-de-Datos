import pygame
import constantes as cons


class SistemaIluminacion:
    def __init__(self, filas, columnas, tile_size):
        self.filas = filas
        self.columnas = columnas
        self.tile_size = tile_size
        self.radio_luz = cons.RADIO_LUZ

        # Superficies para efectos visuales
        self.overlay = pygame.Surface((columnas * tile_size, filas * tile_size), pygame.SRCALPHA)
        self.cell_cache = {}  # Cache para superficies de celdas

        # Estado de iluminación
        self.iluminadas = [[False] * columnas for _ in range(filas)]
        self.celdas_iluminadas_actuales = []

    def obtener_celdas_iluminadas(self, px, py):
        """Calcula las celdas iluminadas alrededor de una posición"""
        ilumin = []

        # Obtener la celda base (parte entera)
        base_x = int(px)
        base_y = int(py)

        # Calcular el offset dentro de la celda (parte decimal)
        offset_x = px - base_x
        offset_y = py - base_y

        # Radio extendido para cubrir el área completa
        radio_extendido = self.radio_luz + 1
        for dy in range(-radio_extendido, radio_extendido + 1):
            for dx in range(-radio_extendido, radio_extendido + 1):
                nx, ny = px + dx, py + dy
                if 0 <= nx < self.columnas and 0 <= ny < self.filas:
                    distancia = max(abs(dx), abs(dy))
                    if distancia <= self.radio_luz:
                        ilumin.append((nx, ny, distancia))
        return ilumin

    def actualizar_iluminacion(self, posicion_jugador):
        """Actualiza el estado de iluminación basado en la posición del jugador"""
        # Resetear iluminación
        self.iluminadas = [[False] * self.columnas for _ in range(self.filas)]

        # Obtener posición del jugador en celdas
        jugador_x = posicion_jugador[0] // self.tile_size
        jugador_y = posicion_jugador[1] // self.tile_size

        # Calcular nuevas celdas iluminadas
        self.celdas_iluminadas_actuales = self.obtener_celdas_iluminadas(jugador_x, jugador_y)

        # Marcar celdas como iluminadas
        for nx, ny, dist in self.celdas_iluminadas_actuales:
            self.iluminadas[ny][nx] = True

    def obtener_color_celda(self, laberinto, fila, columna):
        """Determina el color de una celda basado en iluminación y tipo"""
        if not self.iluminadas[fila][columna]:
            return cons.NEGRO  # No iluminado

        if laberinto[fila][columna] == 1:
            return cons.GRIS  # Pared iluminada
        else:
            return cons.BEIGE  # Camino iluminado

    def dibujar_laberinto_iluminado(self, screen, laberinto, entrada=None, salida=None):
        """Dibuja el laberinto con iluminación"""
        for fila in range(self.filas):
            for columna in range(self.columnas):
                color = self.obtener_color_celda(laberinto, fila, columna)

                rect = pygame.Rect(columna * self.tile_size,
                                   fila * self.tile_size,
                                   self.tile_size, self.tile_size)
                pygame.draw.rect(screen, color, rect)

                # Marcar entrada y salida (solo si están iluminadas)
                if self.iluminadas[fila][columna]:
                    if entrada and (columna, fila) == entrada:
                        pygame.draw.rect(screen, (0, 255, 0), rect, 2)
                    elif salida and (columna, fila) == salida:
                        pygame.draw.rect(screen, (0, 0, 255), rect, 2)

    def crear_superficie_celda(self, alpha):
        """Crea una superficie de celda con transparencia (usando cache)"""
        if alpha not in self.cell_cache:
            cell = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
            cell.fill((0, 0, 0, alpha))
            self.cell_cache[alpha] = cell
        return self.cell_cache[alpha]

    def dibujar_overlay_oscuridad(self, screen):
        """Dibuja el efecto de oscuridad gradual"""
        self.overlay.fill((0, 0, 0, 200))  # Limpiar overlay

        # Procesar todas las celdas
        for fila in range(self.filas):
            for columna in range(self.columnas):
                if not self.iluminadas[fila][columna]:
                    # Celda completamente oscura
                    cell = self.crear_superficie_celda(200)
                    self.overlay.blit(cell, (columna * self.tile_size, fila * self.tile_size))
                else:
                    # Encontrar la distancia para esta celda iluminada
                    for nx, ny, dist in self.celdas_iluminadas_actuales:
                        if nx == columna and ny == fila:
                            # Efecto de desvanecimiento en los bordes
                            alpha = int(200 * (dist / (self.radio_luz + 1)))
                            cell = self.crear_superficie_celda(alpha)
                            self.overlay.blit(cell, (columna * self.tile_size, fila * self.tile_size))
                            break

        # Dibujar overlay en la pantalla
        screen.blit(self.overlay, (0, 0))

    def esta_iluminada(self, x, y):
        """Verifica si una posición está iluminada"""
        if isinstance(x, pygame.Rect):
            # Si es un rectángulo, verificar su posición central
            celda_x = x.x // self.tile_size
            celda_y = x.y // self.tile_size
        else:
            # Si son coordenadas
            celda_x = x // self.tile_size if x >= self.tile_size else x
            celda_y = y // self.tile_size if y >= self.tile_size else y

        return (0 <= celda_x < self.columnas and
                0 <= celda_y < self.filas and
                self.iluminadas[celda_y][celda_x])

    def dibujar_entidades_iluminadas(self, screen, entidades,entidades2):
        """Dibuja entidades solo si están iluminadas"""
        for entidad in entidades:
            if self.esta_iluminada(entidad.forma.x, entidad.forma.y):
                entidad.dibujar(screen)

        for entidad2 in entidades:
            if self.esta_iluminada(entidad2.forma.x, entidad2.forma.y):
                entidad2.dibujar(screen)




