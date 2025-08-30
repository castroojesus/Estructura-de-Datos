from abc import ABC, abstractmethod
#importo la libreria de metodo abstracto

class Persona(ABC):
    def __init__(self, nombre: str, apellidoPat: str, apellidoMat: str, cal: float, matri: str):
        self.nombre = nombre
        self.apellidoPat = apellidoPat
        self.apellidoMat = apellidoMat
        self.cal = cal
        self.matri = matri
#declaro la clase persona que va a ser mi arreglo de tipo abstracto con los elementos de nombres apellidos y de mas

    @abstractmethod
    def mostrar_info(self) -> str:
        pass

class Estudiante(Persona):
    def mostrar_info(self) -> str:
        return f"{self.nombre} {self.apellidoPat} {self.apellidoMat} {self.cal} {self.matri}"
#aqui asigno una clase hija que hereda los atributos de la clase persona y defino una funcion que sea mostrar la informacion que yo escriba para cada elemento

# Crear lista de 2 estudiantes
students = [None] * 2

#aqui le asigno los datos a cada estudiante usando la clase estudiante
students[0] = Estudiante("Jesus Alfonso", "Castro", "Sepulveda", 9.9, "24133450")
students[1] = Estudiante("Naomi", "Fong", "Burgueño", 9.9, "24125140")

#y aqui imprimo cada estudiante en un ciclo para no escribir linea por linea print
for i in range(len(students)):
    print(students[i].mostrar_info())
