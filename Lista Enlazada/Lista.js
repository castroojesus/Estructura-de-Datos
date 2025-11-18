class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

let head = null;

function insertbeg() {
    const item = parseInt(prompt("Ingresa un elemento: "));
    const newNode = new Node(item);
    newNode.next = head;
    head = newNode;
    console.log("Elemento insertado");
}

function insertend() {
    const item = parseInt(prompt("Ingresa un elemento: "));
    const newNode = new Node(item);
    
    if (head === null) {
        head = newNode;
        console.log("Elemento insertado");
    } else {
        let temp = head;
        while (temp.next !== null) {
            temp = temp.next;
        }
        temp.next = newNode;
        console.log("Elemento insertado");
    }
}

function randominsert() {
    const item = parseInt(prompt("Ingresa un elemento: "));
    const pos = parseInt(prompt("Ingresa la posicion: "));
    
    const newNode = new Node(item);
    let temp = head;
    
    for (let i = 0; i < pos - 1; i++) {
        if (temp === null) {
            console.log("La posicion no existe");
            return;
        }
        temp = temp.next;
    }
    
    if (temp !== null) {
        newNode.next = temp.next;
        temp.next = newNode;
        console.log("Elemento insertado");
    } else {
        console.log("La posicion no existe");
    }
}

function deletebeg() {
    if (head === null) {
        console.log("La lista esta vacia");
    } else {
        head = head.next;
        console.log("Elemento eliminado desde el principio");
    }
}

function deleteend() {
    if (head === null) {
        console.log("La lista esta vacia");
    } else if (head.next === null) {
        head = null;
        console.log("Solo se elimino un nodo de la lista");
    } else {
        let temp = head;
        let prev = null;
        while (temp.next !== null) {
            prev = temp;
            temp = temp.next;
        }
        prev.next = null;
        console.log("Elemento eliminado desde el final");
    }
}

function randomdelete() {
    if (head === null) {
        console.log("La lista esta vacia");
        return;
    }
    
    const pos = parseInt(prompt("Ingresa la posicion: "));
    
    if (pos === 0) {
        deletebeg();
        return;
    }
    
    let temp = head;
    let prev = null;
    
    for (let i = 0; i < pos; i++) {
        if (temp === null) {
            console.log("La posicion no existe");
            return;
        }
        prev = temp;
        temp = temp.next;
    }
    
    if (temp !== null) {
        prev.next = temp.next;
        console.log("Elemento eliminado desde la posicion " + (pos + 1));
    } else {
        console.log("La posicion no existe");
    }
}

function display() {
    if (head === null) {
        console.log("La lista esta vacia");
    } else {
        let temp = head;
        let result = "Elementos en la lista: ";
        while (temp !== null) {
            result += temp.data + " ";
            temp = temp.next;
        }
        console.log(result);
    }
}

function search() {
    if (head === null) {
        console.log("La lista esta vacia");
        return;
    }
    
    const item = parseInt(prompt("Ingresa el elemento a buscar: "));
    let temp = head;
    let pos = 0;
    let found = false;
    
    while (temp !== null) {
        if (temp.data === item) {
            console.log("Elemento " + item + " encontrado en la posicion " + pos);
            found = true;
        }
        temp = temp.next;
        pos++;
    }
    
    if (!found) {
        console.log("Elemento no encontrado en la lista");
    }
}

// Menú principal
function main() {
    let choice = 0;
    while (choice !== 9) {
        console.log("\n*********Main Menu*********");
        console.log("1. Agregar al inicio");
        console.log("2. Agregar al final");
        console.log("3. Agregar en una posicion aleatoria");
        console.log("4. Eliminar desde el inicio");
        console.log("5. Eliminar desde el final");
        console.log("6. Eliminar desde una posicion aleatoria");
        console.log("7. Mostrar");
        console.log("8. Buscar");
        console.log("9. Salir");
        choice = parseInt(prompt("Ingresa tu opcion: "));
        
        switch (choice) {
            case 1:
                insertbeg();
                break;
            case 2:
                insertend();
                break;
            case 3:
                randominsert();
                break;
            case 4:
                deletebeg();
                break;
            case 5:
                deleteend();
                break;
            case 6:
                randomdelete();
                break;
            case 7:
                display();
                break;
            case 8:
                search();
                break;
            case 9:
                return;
            default:
                console.log("Opcion invalida! Por favor intenta de nuevo.");
        }
    }
}


main();