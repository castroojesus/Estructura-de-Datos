import random
import pygame
from items import Trampas
from items import Tesoros
from items import Llave
import constantes as const


class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = []
        self.trampas=[]
        self.tesoros=[]
        self.llave=[]
        self.generate_maze()
        self.entrada=(1,0)
        self.salida=None
        self.salida_visible=False
        self.place_random_exit()
        self.colocar_trampa()
        self.colocar_tesoros()
        self.colocar_llave()



    def colocar_trampa(self):
        callejones = self.detectar_callejones()


        if callejones:
            num_trampas = min(5, len(callejones))
            callejones_seleccionados = random.sample(callejones, num_trampas)

            for x, y in callejones_seleccionados:
                self.trampas.append(Trampas(x, y))

    def colocar_tesoros(self, cantidad_tesoros=5, distancia_minima=6):

        posiciones_validas = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self.maze[i][j] == 0:

                    if (i, j) != self.get_entry_pos() and (i, j) != tuple(self.exit_pos):
                        if all((i, j) != (trampa.x, trampa.y) for trampa in self.trampas):
                            posiciones_validas.append((i, j))


        cantidad_tesoros = min(cantidad_tesoros, len(posiciones_validas))

        if cantidad_tesoros == 0:
            return

        tesoros_colocados = []


        intentos_maximos = 100
        intentos = 0

        while len(tesoros_colocados) < cantidad_tesoros and intentos < intentos_maximos:
            intentos += 1


            posicion = random.choice(posiciones_validas)
            x, y = posicion


            distancia_ok = True
            for tesoro in tesoros_colocados:
                tx, ty = tesoro
                distancia = abs(x - tx) + abs(y - ty)
                if distancia < distancia_minima:
                    distancia_ok = False
                    break


            entrada_pos = self.get_entry_pos()
            salida_pos = self.exit_pos
            distancia_entrada = abs(x - entrada_pos[0]) + abs(y - entrada_pos[1])
            distancia_salida = abs(x - salida_pos[0]) + abs(y - salida_pos[1])

            if distancia_ok and distancia_entrada >= 2 and distancia_salida >= 2:
                tesoros_colocados.append((x, y))

                posiciones_validas.remove((x, y))

        wishbone=pygame.image.load('player/wishbone.png')
        wishbone=pygame.transform.scale(wishbone, (const.tileSize, const.tileSize))
        vodka_cranberry=pygame.image.load('player/vodka_cranberry.png')
        vodka_cranberry=pygame.transform.scale(vodka_cranberry, (const.tileSize, const.tileSize))
        sweater = pygame.image.load('player/sweater.png')
        sweater = pygame.transform.scale(sweater, (const.tileSize, const.tileSize))
        dozen_roses = pygame.image.load('player/dozen_roses.png')
        dozen_roses = pygame.transform.scale(dozen_roses, (const.tileSize, const.tileSize))
        footnote = pygame.image.load('player/footnote.png')
        footnote = pygame.transform.scale(footnote, (const.tileSize, const.tileSize))

        mis_tesoros = [
            {"nombre": "Wishbone", "imagen":wishbone, "valor": 100},
            {"nombre": "Vodka Cranberry","imagen":vodka_cranberry, "valor": 150},
            {"nombre": "Sweater", "imagen":sweater,"valor": 80},
            {"nombre": "Fifteen Dozen Roses","imagen":dozen_roses, "valor": 120},
            {"nombre": "Footnote","imagen":footnote, "valor": 60}
        ]


        cantidad_a_colocar = min(cantidad_tesoros, len(mis_tesoros), len(tesoros_colocados))

        for i in range(cantidad_a_colocar):
            x, y = tesoros_colocados[i]
            info = mis_tesoros[i]
            tesoro = Tesoros(x, y, info["nombre"],info["imagen"], info["valor"])
            self.tesoros.append(tesoro)


    def colocar_llave(self, cantidad=1, distancia_minima=5):

        posiciones_validas = []

        for i in range(self.rows):
            for j in range(self.cols):

                if self.maze[i][j] == 0:

                    if (i, j) != self.get_entry_pos() and (i, j) != tuple(self.exit_pos):
                        posiciones_validas.append((i, j))

        if not posiciones_validas:
            return


        posiciones_evitar = []


        posiciones_evitar.append(self.get_entry_pos())
        posiciones_evitar.append(tuple(self.exit_pos))


        for trampa in self.trampas:
            posiciones_evitar.append((trampa.x, trampa.y))


        for tesoro in self.tesoros:
            posiciones_evitar.append((tesoro.x, tesoro.y))

        llaves_colocadas = []
        intentos_maximos = 50
        intentos = 0

        while len(llaves_colocadas) < cantidad and intentos < intentos_maximos and posiciones_validas:
            intentos += 1


            posicion = random.choice(posiciones_validas)
            x, y = posicion


            distancia_ok = True
            for pos_evitar in posiciones_evitar:
                distancia_manhattan = abs(x - pos_evitar[0]) + abs(y - pos_evitar[1])
                if distancia_manhattan < distancia_minima:
                    distancia_ok = False
                    break


            for llave in llaves_colocadas:
                distancia_manhattan = abs(x - llave[0]) + abs(y - llave[1])
                if distancia_manhattan < distancia_minima:
                    distancia_ok = False
                    break

            if distancia_ok:
                llaves_colocadas.append((x, y))

                posiciones_validas.remove((x, y))


        for x, y in llaves_colocadas:
            self.llave.append(Llave(x, y))



    def detectar_callejones(self):
            callejones = []

            for i in range(1, self.rows - 1):
                for j in range(1, self.cols - 1):
                    if self.maze[i][j] == 0:
                        caminos_adyacentes = self.contar_caminos_adyacentes(i, j)

                        if caminos_adyacentes == 1 and self.es_callejon_puro(i, j):
                            callejones.append((i, j))

            return callejones

    def contar_caminos_adyacentes(self, x, y):
            count = 0
            direcciones = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    if self.maze[nx][ny] == 0:
                        count += 1
            return count

    def es_callejon_puro(self, x, y):

        if not hasattr(self, 'salida') or self.salida is None:

            distancia_salida = 100
        else:
            distancia_salida = abs(x - self.salida[0]) + abs(y - self.salida[1])

        distancia_entrada = abs(x - self.entrada[0]) + abs(y - self.entrada[1])

        return distancia_entrada > 3 and distancia_salida > 3



    def get_trampas(self):
        return self.trampas

    def get_tesoros(self):
        return self.tesoros

    def get_llave(self):
        return self.llave

    def generate_maze(self):

        self.maze = [[1 for _ in range(self.cols)] for _ in range(self.rows)]

        stack = []
        stack.append([1, 1])
        self.maze[1][1] = 0

        directions = [[0, 2], [0, -2], [2, 0], [-2, 0]]

        while stack:
            current = stack.pop()
            x, y = current[0], current[1]

            random.shuffle(directions)

            for dir in directions:
                nx = x + dir[0]
                ny = y + dir[1]

                if (0 < nx < self.rows - 1 and
                        0 < ny < self.cols - 1 and
                        self.maze[nx][ny] == 1):
                    self.maze[nx][ny] = 0
                    self.maze[x + dir[0] // 2][y + dir[1] // 2] = 0
                    stack.append([nx, ny])


        self.maze[1][0] = 0

    def place_random_exit(self):

        min_distance = 10
        start_row = 1
        start_col = 0


        borders = ["top", "bottom", "left", "right"]
        random.shuffle(borders)

        for border in borders:
            candidates = []

            if border == "top":
                for col in range(1, self.cols - 1):
                    if (self.maze[1][col] == 0 and
                            self.maze[0][col] == 1):
                        distance = abs(start_row - 0) + abs(start_col - col)
                        if distance >= min_distance:
                            candidates.append([0, col])

            elif border == "bottom":
                for col in range(1, self.cols - 1):
                    if (self.maze[self.rows - 2][col] == 0 and
                            self.maze[self.rows - 1][col] == 1):
                        distance = abs(start_row - (self.rows - 1)) + abs(start_col - col)
                        if distance >= min_distance:
                            candidates.append([self.rows - 1, col])

            elif border == "left":
                for row in range(1, self.rows - 1):
                    if (self.maze[row][1] == 0 and
                            self.maze[row][0] == 1):
                        distance = abs(start_row - row) + abs(start_col - 0)
                        if distance >= min_distance:
                            candidates.append([row, 0])

            elif border == "right":
                for row in range(1, self.rows - 1):
                    if (self.maze[row][self.cols - 2] == 0 and
                            self.maze[row][self.cols - 1] == 1):
                        distance = abs(start_row - row) + abs(start_col - (self.cols - 1))
                        if distance >= min_distance:
                            candidates.append([row, self.cols - 1])


            if candidates:
                exit_pos = random.choice(candidates)
                self.maze[exit_pos[0]][exit_pos[1]] = 0
                self.exit_pos = exit_pos
                return

    def get_maze(self):
        return self

    def get_entry_pos(self):
        return (1, 0)

    def get_exit_pos(self):
        return self.exit_pos

    def dibujar_laberinto(self, screen, cell_size, colors):

        tesoros_dibujados = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.maze[row][col] == 1:
                    color = colors['PARED']
                elif self.maze[row][col] == 0:
                    color = colors['CAMINO']
                elif self.maze[row][col] == 2:
                    color = colors['CAMINO']


                for trampa in self.trampas:
                    if trampa.x == row and trampa.y == col:


                        color = colors['TRAMPA']

                        break


                for llave in self.llave:
                    if llave.x == row and llave.y == col:
                        color = colors['LLAVE']
                        break

                if self.salida_visible and hasattr(self, 'exit_pos') and (row, col) == tuple(self.exit_pos):
                    color = colors['FIN']


                if (row, col) == self.get_entry_pos():
                    color = colors['INICIO']


                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, color, rect)

                for tesoro in self.tesoros:
                    if tesoro.x == row and tesoro.y == col:
                        if hasattr(tesoro, 'imagen'):

                            screen.blit(tesoro.imagen, (col * cell_size, row * cell_size))

                        break

    def next_level(self):

        self.maze = []
        self.trampas = []
        self.tesoros = []
        self.llave = []
        self.salida_visible = False


        self.generate_maze()
        self.place_random_exit()
        self.colocar_trampa()
        self.colocar_tesoros()
        self.colocar_llave()

        print("Nuevo nivel generado")

    def marcar_camino(self, x, y):

        if (x < self.rows and x>=0) and (y < self.cols and y >= 0):
            if self.maze[y][x]==0 or self.maze[y+1][x+1] == 0:
                self.maze[y][x] = 2

