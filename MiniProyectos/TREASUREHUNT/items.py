import pygame


class Trampas:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.activada=False

    def activar(self, jugador):
        if not self.activada:
            self.activada = True
            if jugador:

             jugador.perder_vida()


class Tesoros:
    def __init__(self, x,y, nombre,imagen, valor):
        self.x = x
        self.y = y
        self.recolectado=False
        self.nombre=nombre
        self.valor=valor
        self.imagen=imagen




    def recolectar(self, jugador):
        if not self.recolectado:
            self.recolectado = True
            if jugador:
                mensaje = f"¡{self.nombre} encontrado! +{self.valor} puntos"
                print(mensaje)
            if hasattr(jugador, 'puntos'):
                jugador.puntos += self.valor

            if hasattr(jugador, 'inventario'):
                jugador.inventario.agregar_tesoro(self.nombre, self.valor)

            return mensaje
        return ""



class Llave:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.encontrada=False


    def encontrar(self, jugador):
        if not self.encontrada:
            if jugador:
             print("Has encontrado la llave")
             self.encontrada = True

class Inventario:
    def __init__(self, capacidad=6):
        self.capacidad = capacidad
        self.items=[]
        self.llaves=0
        self.puntos_totales=0

    def agregar_llave(self):
        if self.llaves<1:
            self.items.append(("Llave",0))
            self.llaves += 1
            print("Haz encontrado la llave")
            return True
        return False

    def agregar_tesoro(self, nombre, valor):
        if len(self.items)<self.capacidad:
            self.items.append((nombre, valor))
            self.puntos_totales += valor
            print(f"🎒 {nombre} (+{valor}) agregado")
            return True
        return False

    def dibujar(self, pantalla, x, y):
        fuente = pygame.font.Font(None, 22)


        pygame.draw.rect(pantalla, (30, 30, 60), (x, y, 240, 200))
        pygame.draw.rect(pantalla, (100, 100, 200), (x, y, 240, 200), 2)


        titulo = fuente.render("INVENTARIO", True, (255, 255, 255))
        pantalla.blit(titulo, (x + 10, y + 5))

        # Puntos totales
        puntos_texto = fuente.render(f"Puntos: {self.puntos_totales}", True, (255, 255, 0))
        pantalla.blit(puntos_texto, (x + 120, y + 5))

        # Capacidad
        capacidad = fuente.render(f"{len(self.items)}/{self.capacidad}", True, (200, 200, 255))
        pantalla.blit(capacidad, (x + 10, y + 25))

        # Items
        for i, (nombre, valor) in enumerate(self.items):
            if i < 8:
                item_y = y + 50 + (i * 18)
                texto = fuente.render(f"{nombre} (+{valor})", True, (255, 255, 255))
                pantalla.blit(texto, (x + 10, item_y))








