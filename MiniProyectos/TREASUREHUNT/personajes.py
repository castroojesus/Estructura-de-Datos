import pygame
import constantes as const

class Personaje:
    def __init__(self,x,y, images_dict):
        self.images = {}

        # Escalar TODAS las imágenes al tamaño del tile
        for direccion, imagen in images_dict.items():
            self.images[direccion] = pygame.transform.scale(imagen, (const.tileSize, const.tileSize))


        self.direccion_actual = 'abajo'  # Dirección por defecto
        self.image = self.images[self.direccion_actual]
        # Variables para movimiento por tiles
        self.se_puede_mover = True
        self.velocidad_movimiento = 1  # Velocidad de transición entre tiles

        self.image = pygame.transform.scale(self.image, (const.tileSize, const.tileSize))
        self.flip=False
        self.shape=pygame.Rect(0,0,const.tileSize,const.tileSize)
        self.shape.x = x
        self.shape.y = y

    def _verificar_colision(self, x, y, ancho, alto, laberinto, salida_pos):
        """Verifica colisiones excluyendo la salida"""
        celda_x1 = x // const.tileSize
        celda_y1 = y // const.tileSize
        celda_x2 = (x + ancho - 1) // const.tileSize
        celda_y2 = (y + alto - 1) // const.tileSize

        for fila in range(celda_y1, celda_y2 + 1):
            for columna in range(celda_x1, celda_x2 + 1):
                # EXCLUIR LA SALIDA de las colisiones
                if (columna, fila) == (salida_pos[1], salida_pos[0]):  # Salida en formato (columna, fila)
                    continue  # Saltar la salida, no es una colisión

                if (0 <= fila < len(laberinto) and
                        0 <= columna < len(laberinto[0]) and
                        laberinto[fila][columna] == 1):  # Pared
                    return True
        return False

    def mover_tile(self, dx, dy, laberinto, salida_pos):
        """Mueve instantáneamente a un tile adyacente"""
        nueva_x = self.shape.x + (dx * const.tileSize)
        nueva_y = self.shape.y + (dy * const.tileSize)

        if not self._verificar_colision(nueva_x, nueva_y, const.tileSize, const.tileSize, laberinto, salida_pos):
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

            return True
        return False

    def permitir_movimiento(self):
        """Permite que el personaje se mueva nuevamente"""
        self.se_puede_mover = True

    def dibujar(self, interfaz):
        # Obtener la imagen actual según la dirección
        imagen_actual = self.images[self.direccion_actual]

        # Aplicar flip si es necesario (para izquierda/derecha)
        if self.flip:
            imagen_actual = pygame.transform.flip(imagen_actual, True, False)

        imagen_rect = imagen_actual.get_rect()
        imagen_rect.center = (
            self.shape.x + self.shape.width // 2,
            self.shape.y + self.shape.height // 2
        )


        interfaz.blit(imagen_actual, imagen_rect)
        #pygame.draw.rect(interfaz,(255,255,0),self.shape,1)



    def movement(self, deltax, delta_y):
        # Determinar dirección basada en el movimiento
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

        # Para izquierda/derecha, usar flip en lugar de imágenes separadas
        if self.direccion_actual == 'izquierda':
            self.flip = True
            self.direccion_actual = 'derecha'  # Usar imagen derecha con flip



        self.shape.x=self.shape.x+deltax
        self.shape.y=self.shape.y+delta_y

