// Clase abstracta (simulada en JavaScript)
class Persona {
    constructor(nombre, apellidoPat, apellidoMat, cal, matri) {
        if (new.target === Persona) {
            throw new Error("No se puede instanciar una clase abstracta Persona");
        }
        this.nombre = nombre;
        this.apellidoPat = apellidoPat;
        this.apellidoMat = apellidoMat;
        this.cal = cal;
        this.matri = matri;
    }

    // Método abstracto (debe ser implementado por las clases hijas)
    mostrarInfo() {
        throw new Error("Método abstracto mostrarInfo() debe ser implementado");
    }
}

// Clase concreta Estudiante
class Estudiante extends Persona {
    constructor(nombre, apellidoPat, apellidoMat, cal, matri) {
        super(nombre, apellidoPat, apellidoMat, cal, matri);
    }

    mostrarInfo() {
        return `${this.nombre} ${this.apellidoPat} ${this.apellidoMat} ${this.cal} ${this.matri}`;
    }
}

// Crear array de estudiantes
const students = [];

// Agregar estudiantes
students.push(new Estudiante("Jesus Alfonso", "Castro", "Sepulveda", 9.9, "24133450"));
students.push(new Estudiante("Naomi", "Fong", "Burgueño", 9.9, "24125140"));

// Imprimir información
students.forEach(estudiante => {
    console.log(estudiante.mostrarInfo());
});
