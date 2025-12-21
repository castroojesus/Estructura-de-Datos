// PILA
const MAX_SIZE = 100;
let stack = new Array(MAX_SIZE);      // arreglo de la pila
let top = -1;                         // elemento del tope de la pila

// funcion para insertar un elemento en la pila
function push(item) {
    if (top == MAX_SIZE - 1) {        // si la pila está llena
        console.log("STACK OVERFLOW");
        return;
    }
    stack[++top] = item;              // incrementa el indice y agrega el elemento a la pila
}

// funcion para eliminar un elemento o sacar
function pop() {
    if (top == -1) {                  // si la pila esta vacia
        console.log("STACK UNDERFLOW");
        return -1;
    }
    return stack[top--];
}

// funcion para ver el elemento superior sin eliminarlo
function peek() {
    if (top == -1) {                  // si esta vacia
        console.log("PILA VACIA");
        return -1;
    }
    return stack[top];                // retorna el valor del tope
}

// funcion para ver si la pila esta vacia
function isEmpty() {
    return top == -1;                 // retorna true si la pila es -1, o sea que esta vacia 
}

// funcion para ver si esta llena
function isFull() {
    return top == MAX_SIZE - 1;       // retorna true si esta llena, si el indice sup es igual al tamaño maximo menos uno
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
        console.log("1. Insertar PUSH\n2. Extraer POP\n3. Ver elemento superior\n4. Verificar si está vacía\n5. Verificar si está llena\n6. Salir");
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
                    console.log(isFull() ? "La pila está llena" : "La pila NO está llena");
                    showMenu();
                    break;
                case 6:
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