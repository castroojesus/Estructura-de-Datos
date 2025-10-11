import pygame
import constantes as const

class Personaje():
    def __init__(self,x,y):
        self.shape=pygame.Rect(0,0,const.tileSize,const.tileSize)
        self.shape.center=(x,y)

    def dibujar(self, interfaz):
            pygame.draw.rect(interfaz, const.PlayerColor,self.shape)

    def movement(self, deltax, delta_y):
        self.shape.x=self.shape.x+deltax
        self.shape.y=self.shape.y+delta_y