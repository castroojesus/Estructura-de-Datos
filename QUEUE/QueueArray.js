// COLA CON ARRAYS
const MAXSIZE = 5;
let queue = new Array(MAXSIZE);
let front = -1, rear = -1;

function insertar() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    rl.question("Ingrese el elemento: ", (input) => {
        let elem = parseInt(input);
        
        if (rear == MAXSIZE - 1) {
            console.log("OVERFLOW");
            rl.close();
            return;
        }
        if (front == -1 && rear == -1) {
            front = rear = 0;
        } else {
            rear++;
        }
        queue[rear] = elem;
        console.log("Elemento insertado correctamente");
        rl.close();
    });
}

function eliminar() {
    if (front == -1 || front > rear) {
        console.log("UNDERFLOW");
        return;
    }
    let elemento = queue[front];
    if (front == rear) {
        front = rear = -1;
    } else {
        front++;
    }
    console.log("Elemento eliminado " + elemento);
}

function mostrar() {
    if (rear == -1 || front == -1 || front > rear) {
        console.log("La cola esta vacia");
    } else {
        console.log("Elementos de la cola: ");
        for (let i = front; i <= rear; i++) {
            console.log(queue[i]);
        }
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
        console.log("\n************************MENU QUEUE****************************");
        console.log("==================================================================");
        console.log("1. Insertar elemento en la cola");
        console.log("2. Eliminar elemento de la cola");
        console.log("3. Mostrar la cola");
        console.log("4. Salir");
        rl.question("Ingrese su opcion: ", (input) => {
            opc = parseInt(input);
            
            switch(opc) {
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
                    console.log("\nOpcion invalida. Ingrese de nuevo\n");
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