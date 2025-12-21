// PILA CON LISTA ENLAZADA
class Node {
    constructor() {
        this.data = 0;     // dato del nodo
        this.next = null;  // direccion al siguiente nodo
    }
}

let top = null;    // puntero a tope de pila

// funcion para insertar en pila
function push(item) {
    let newNode = new Node();    // crea un nodo
    newNode.data = item;         // asigna el dato
    newNode.next = top;          // el nuevo nodo apunta al anterior tope
    top = newNode;               // el nuevo nodo es ahora el tope
    console.log("Elemento insertado: " + item);
}

// funcion para eliminar un elemento o extraer
function pop() {
    if (top == null) {          // si la pila esta vacia
        console.log("STACK UNDERFLOW");
        return -1;
    }
    let temp = top;              // guarda el nodo del tope
    let valor = top.data;        // guarda el dato
    top = top.next;              // mueve el tope al siguiente nodo
    temp = null;                 // ayuda al recolector de basura
    return valor;
}

// funcion para ver el elemento superior 
function peek() {
    if (top == null) {          // si esta vacia
        console.log("PILA VACIA");
        return -1;
    }
    return top.data;            // retorna el valor del tope
}

// funcion para ver si la pila esta vacia
function isEmpty() {
    return top == null;         // retorna true si el tope es null, o sea que esta vacia
}

// Menu principal (simulado)
function main() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    
    let choice = 0;
    
    function showMenu() {
        console.log("\n\n*********Menu Pila*********");
        console.log("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Salir");
        rl.question("Ingrese su opción: ", (answer) => {
            choice = parseInt(answer);
            if (isNaN(choice)) choice = 0;
            
            switch(choice) {
                case 1:
                    rl.question("Ingrese el valor a insertar: ", (valorInput) => {
                        let valor = parseInt(valorInput);
                        if (!isNaN(valor)) {
                            push(valor);
                        }
                        showMenu();
                    });
                    break;
                case 2: {
                    let valor = pop();
                    if (valor != -1) console.log("Elemento extraído: " + valor);
                    showMenu();
                    break;
                }
                case 3: {
                    let valor = peek();
                    if (valor != -1) console.log("Elemento superior: " + valor);
                    showMenu();
                    break;
                }
                case 4:
                    console.log(isEmpty() ? "La pila está vacía" : "La pila NO está vacía");
                    showMenu();
                    break;
                case 5:
                    console.log("Saliendo del programa...");
                    rl.close();
                    break;
                default:
                    console.log("Por favor, introduzca una opción válida");
                    showMenu();
            }
        });
    }
    
    showMenu();
}

// Ejecutar el programa
if (require.main === module) {
    main();
}