// Estructura del nodo
class Nodo {
    constructor() {
        this.dato = 0;
        this.siguiente = null;
    }
}

let front = null;
let rear = null;

function insertar() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question("Ingrese el elemento: ", (input) => {
        let elem = parseInt(input);
        
        let nuevo = new Nodo();
        nuevo.dato = elem;
        nuevo.siguiente = null;
        
        if (front == null && rear == null) {
            front = rear = nuevo;
        } else {
            rear.siguiente = nuevo;
            rear = nuevo;
        }
        
        console.log("Elemento insertado correctamente");
        rl.close();
    });
}

function eliminar() {
    if (front == null) {
        console.log("UNDERFLOW");
        return;
    }
    
    let temp = front;
    let elemento = temp.dato;
    
    front = front.siguiente;
    if (front == null) {
        rear = null;
    }
    
    temp = null; // Ayuda al recolector de basura
    console.log("Elemento eliminado: " + elemento);
}

function mostrar() {
    if (front == null) {
        console.log("La cola está vacía");
        return;
    }
    
    console.log("Elementos de la cola:");
    let actual = front;
    while (actual != null) {
        console.log(actual.dato);
        actual = actual.siguiente;
    }
}

function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let opc = 0;
    
    function mostrarMenu() {
        console.log("\n*************** MENU QUEUE ***************");
        console.log("1. Insertar elemento en la cola");
        console.log("2. Eliminar elemento de la cola");
        console.log("3. Mostrar la cola");
        console.log("4. Salir");
        rl.question("Ingrese su opción: ", (input) => {
            opc = parseInt(input);
            
            switch (opc) {
                case 1:
                    rl.close();
                    insertar();
                    setTimeout(() => {
                        mostrarMenu();
                    }, 100);
                    break;
                case 2:
                    eliminar();
                    mostrarMenu();
                    break;
                case 3:
                    mostrar();
                    mostrarMenu();
                    break;
                case 4: 
                    console.log("Saliendo del programa...");
                    rl.close();
                    break;
                default:
                    console.log("Opción inválida. Ingrese de nuevo");
                    mostrarMenu();
            }
        });
    }
    
    mostrarMenu();
}

// Ejecutar el programa
if (require.main === module) {
    main();
}