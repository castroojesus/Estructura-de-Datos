import random
import pygame


class MazeGenerator:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.maze = []
        self.generate_maze()
        self.place_random_exit()

    def generate_maze(self):
        # Inicializar todo como paredes (1)
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

        # Entrada fija
        self.maze[1][0] = 0

    def place_random_exit(self):
        """Coloca una salida aleatoria que esté a una distancia mínima de la entrada"""
        min_distance = 10
        start_row = 1
        start_col = 0

        # Lista de bordes posibles
        borders = ["top", "bottom", "left", "right"]
        random.shuffle(borders)  # mezcla aleatoria

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

            # Si hay candidatos válidos en este borde, elige uno
            if candidates:
                exit_pos = random.choice(candidates)
                self.maze[exit_pos[0]][exit_pos[1]] = 0
                self.exit_pos = exit_pos
                return  # ya colocamos la salida, salimos del método

    def get_maze(self):
        return self.maze

    def get_entry_pos(self):
        return (1, 0)  # Posición de entrada fija

    def get_exit_pos(self):
        return self.exit_pos

    def dibujar_laberinto(self, screen, cell_size, colors):
        """
            screen: Superficie de Pygame
            cell_size: Tamaño de cada celda en píxeles
            colors: Diccionario con colores {'PARED', 'CAMINO', 'INICIO', 'FIN'}
        """
        for row in range(self.rows):
            for col in range(self.cols):
                color = colors['PARED'] if self.maze[row][col] == 1 else colors['CAMINO']

                # Colores especiales para entrada y salida
                if (row, col) == self.get_entry_pos():
                    color = colors['INICIO']
                elif hasattr(self, 'exit_pos') and (row, col) == tuple(self.exit_pos):
                    color = colors['FIN']

                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, color, rect)