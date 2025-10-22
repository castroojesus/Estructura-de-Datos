import pygame
from pkg_resources import non_empty_lines

import constantes as const
from items import Inventario


class Personaje:
    def __init__(self, x, y, images_dict):
        self.images = {}


        for direccion, imagen in images_dict.items():
            self.images[direccion] = pygame.transform.scale(imagen, (const.tileSize, const.tileSize))

        self.direccion_actual = 'abajo'
        self.image = self.images[self.direccion_actual]

        self.se_puede_mover = True
        self.velocidad_movimiento = 1

        self.image = pygame.transform.scale(self.image, (const.tileSize, const.tileSize))
        self.flip = False
        self.shape = pygame.Rect(0, 0, const.tileSize, const.tileSize)
        self.shape.x = x
        self.shape.y = y
        self.vidamaxima=3
        self.vidaactual=self.vidamaxima
        self.energia_maxima=4
        self.energia=[True]*self.energia_maxima
        self.pasos_exitosos=0
        self.llaves=0
        self.energia_perdida=0
        self.puntos=0
        self.inventario=Inventario()

    def agregar_llave(self):
        if self.inventario.agregar_llave():
            self.llaves = self.inventario.llaves
            return True
        return False




    def dibujar_vidas(self, interfaz,corazon, corazon_muerto):

        margenx = 10
        margeny = 605
        space=5
        tamano=(32,32)


        for i in range(self.vidamaxima):
            x = margenx + i * (tamano[0] + space)
            y = margeny

            if i < self.vidaactual:
                interfaz.blit(corazon, (x, y))
            else:
                interfaz.blit(corazon_muerto, (x, y))

    def dibujar_energia(self, interfaz,energia, energia_agotada):

        margenx = 120
        margeny = 605
        space=5
        tamano=(32,32)


        for i in range(self.get_energia_maxima()):
            x = margenx + i * (tamano[0] + space)
            y = margeny

            if self.energia[i]:
                interfaz.blit(energia, (x, y))
            else:
                interfaz.blit(energia_agotada, (x, y))

    def perder_vida(self, laberinto=None):
        if self.vidaactual>0:
            self.vidaactual-=1

            if laberinto:
                entrada=laberinto.get_entry_pos()
                self.shape.x=entrada[1]*const.tileSize
                self.shape.y=entrada[0]*const.tileSize
            print(f"¡Has perdido una vida! Te quedan: {self.vidaactual}")
            return True
        return False

    def energia_actual(self):

        return sum(1 for estado in self.energia if estado)

    def get_energia_maxima(self):
        return len(self.energia)

    def ganar_energia(self):

        self.energia.append(True)
        self.energia_perdida = 0

        return True

    def perder_energia(self, laberinto=None):
        if self.energia_actual()>0:
            for i in range(len(self.energia) - 1, -1, -1):
                if self.energia[i]:
                    self.energia[i] = False
                    self.energia_perdida += 1
                    break


            if self.energia_perdida>=4:
                self.reset_energia()
                self.perder_vida(laberinto)

            return True
        return False


    def reset_energia(self):
        self.energia_perdida=0
        self.energia=[True]*self.energia_maxima


    def esta_vivo(self):

        return self.vidaactual > 0

    def resetear_vidas(self):

        self.vidaactual = self.vidamaxima

    def _verificar_colision(self, x, y, ancho, alto, laberinto, salida_pos):

        celda_x1 = x // const.tileSize
        celda_y1 = y // const.tileSize
        celda_x2 = (x + ancho - 1) // const.tileSize
        celda_y2 = (y + alto - 1) // const.tileSize



        for fila in range(celda_y1, celda_y2 + 1):
            for columna in range(celda_x1, celda_x2 + 1):
                # EXCLUIR LA SALIDA de las colisiones
                if (columna, fila) == (salida_pos[1], salida_pos[0]):

                    if hasattr(laberinto, 'salida_visible'):
                        laberinto.salida_visible = True
                    if self.llaves>0:
                      continue
                    else:
                        print("🔒 Necesitas una llave para salir")
                        return True

                if (0 <= fila < len(laberinto.maze) and
                        0 <= columna < len(laberinto.maze[0]) and
                        laberinto.maze[fila][columna] == 1):  # Pared
                    self.perder_energia()
                    return True
        return False

    def mover_tile(self, dx, dy, laberinto, salida_pos,trampas=None, tesoros=None, llave=None):
        """Mueve instantáneamente a un tile adyacente"""
        nueva_x = self.shape.x + (dx * const.tileSize)
        nueva_y = self.shape.y + (dy * const.tileSize)

        if not self._verificar_colision(nueva_x, nueva_y, const.tileSize, const.tileSize, laberinto, salida_pos):
            pos_anterior_x = self.shape.x
            pos_anterior_y = self.shape.y

            self.shape.x = nueva_x
            self.shape.y = nueva_y

            # Actualizar dirección
            if dx < 0:
                self.direccion_actual = 'izquierda'
            elif dx > 0:
                self.direccion_actual = 'derecha'
            elif dy < 0:
                self.direccion_actual = 'arriba'
            elif dy > 0:
                self.direccion_actual = 'abajo'

            self.pasos_exitosos += 1
            if self.pasos_exitosos >= 3:
                self.ganar_energia()
                self.pasos_exitosos = 0



            if trampas is not None:
                self.detectar_trampas(trampas, pos_anterior_x, pos_anterior_y)

            if tesoros is not None:
                self.detectar_tesoro(tesoros, pos_anterior_x, pos_anterior_y)

            if llave is not None:
                self.detectar_llave(llave, pos_anterior_x, pos_anterior_y)

            return True
        self.pasos_exitosos = 0
        return False

    def detectar_trampas(self, trampas, pos_anterior_x, pos_anterior_y, laberinto=None):

        tile_x = self.shape.x // const.tileSize
        tile_y = self.shape.y // const.tileSize

        for trampa in trampas:

            if trampa.x == tile_y and trampa.y == tile_x and not trampa.activada:
                mensaje = trampa.activar(self)
                if mensaje:
                    print(mensaje)

    def detectar_llave(self, llave_lista, pos_anterior_x, pos_anterior_y):
        tile_x = self.shape.x // const.tileSize
        tile_y = self.shape.y // const.tileSize

        for llaves in llave_lista:
            if llaves.x == tile_y and llaves.y == tile_x and not llaves.encontrada:
                if self.inventario.agregar_llave():
                    llaves.encontrada = True
                    self.llaves = self.inventario.llaves
    def detectar_tesoro(self, tesoros, pos_anterior_x, pos_anterior_y):

            tile_x = self.shape.x // const.tileSize
            tile_y = self.shape.y // const.tileSize

            for tesoro in tesoros:
                if tesoro.x == tile_y and tesoro.y == tile_x and not tesoro.recolectado:
                    mensaje = tesoro.recolectar(self)
                    if mensaje:
                        print(mensaje)

    def permitir_movimiento(self):

        self.se_puede_mover = True

    def dibujar(self, interfaz):

        imagen_actual = self.images[self.direccion_actual]


        if self.flip:
            imagen_actual = pygame.transform.flip(imagen_actual, True, False)

        imagen_rect = imagen_actual.get_rect()
        imagen_rect.center = (
            self.shape.x + self.shape.width // 2,
            self.shape.y + self.shape.height // 2
        )

        interfaz.blit(imagen_actual, imagen_rect)


    def movement(self, deltax, delta_y):

        if deltax < 0:
            self.direccion_actual = 'izquierda'
            self.flip = False
        elif deltax > 0:
            self.direccion_actual = 'derecha'
            self.flip = False
        elif delta_y < 0:
            self.direccion_actual = 'arriba'
            self.flip = False
        elif delta_y > 0:
            self.direccion_actual = 'abajo'
            self.flip = False


        if self.direccion_actual == 'izquierda':
            self.flip = True
            self.direccion_actual = 'derecha'

        self.shape.x = self.shape.x + deltax
        self.shape.y = self.shape.y + delta_y

