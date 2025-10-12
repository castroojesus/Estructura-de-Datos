import pygame


import constantes as const

class Personaje:
    def __init__(self,x,y, image):
        self.image=image
        self.flip=False
        self.shape=pygame.Rect(0,0,const.tileSize,const.tileSize)
        self.shape.center=(x,y)

    def dibujar(self, interfaz):
        imagen_flip=pygame.transform.flip(self.image,self.flip,False)
        interfaz.blit(imagen_flip,self.shape)
        #pygame.draw.rect(interfaz,constantes.PlayerColor,self.shape,1)



    def movement(self, deltax, delta_y):
        if deltax<0:
            self.flip=True
        if deltax>0:
            self.flip=False



        self.shape.x=self.shape.x+deltax
        self.shape.y=self.shape.y+delta_y

