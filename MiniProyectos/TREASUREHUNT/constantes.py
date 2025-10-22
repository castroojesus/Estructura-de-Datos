# el juego esta en una escala de 16 pixeles por 2
OriginalTileSize=16
scale=2
tileSize=OriginalTileSize*scale

#constantes del personaje
characterWidth=OriginalTileSize/scale
characterHeight=OriginalTileSize/scale
FPS=60
ESCALA=1.2


COLORES_LABERINTO = {
    'PARED': (0, 0, 0),  # Negro
    'CAMINO': (255, 255, 255),  # Blanco
    'INICIO': (0, 255, 0),  # Verde
    'FIN': (255, 0, 0),  # Rojo
    'TRAMPA':(255,127,80),


    'LLAVE':(0,255,255)
}

#constantes de pantalla
maxScreenCol=20
maxScreenRow=20
screenWidth=tileSize*maxScreenCol
screenHeight=tileSize*maxScreenRow