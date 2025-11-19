class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    _getValue(promptMsg) {
        let value = prompt(promptMsg);
        while (value === null || isNaN(parseInt(value))) {
            value = prompt("Entrada inválida. " + promptMsg);
        }
        return parseInt(value);
    }

    insertbegin() {
        const value = this._getValue("Ingrese un valor:");
        const newNode = new Node(value);
        newNode.next = this.head;
        newNode.prev = null;

        if (this.head !== null) {
            this.head.prev = newNode;
        } else {
            this.tail = newNode;
        }
        this.head = newNode;
    }

    insertend() {
        const value = this._getValue("Ingrese un valor:");
        const newNode = new Node(value);
        newNode.next = null;
        newNode.prev = this.tail;

        if (this.tail !== null) {
            this.tail.next = newNode;
        } else {
            this.head = newNode;
        }
        this.tail = newNode;
    }

    insertrandom() {
        const value = this._getValue("Ingrese un valor:");
        const pos = this._getValue("Ingrese la posicion donde desea insertar:");

        if (pos <= 0 || this.head === null) {
            this.insertbegin();
            return;
        }

        let current = this.head;
        for (let i = 0; i < pos - 1; i++) {
            if (current.next === null) {
                this.insertend();
                return;
            }
            current = current.next;
        }

        const newNode = new Node(value);
        newNode.next = current.next;
        newNode.prev = current;

        if (current.next !== null) {
            current.next.prev = newNode;
        } else {
            this.tail = newNode;
        }
        current.next = newNode;
        console.log(`Elemento insertado en la posicion ${pos}`);
    }

    deletebegin() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        const temp = this.head;
        this.head = this.head.next;
        if (this.head !== null) {
            this.head.prev = null;
        } else {
            this.tail = null;
        }
        console.log("Elemento eliminado desde el inicio");
    }

    deleteend() {
        if (this.tail === null) {
            console.log("La lista esta vacia");
            return;
        }
        const temp = this.tail;
        this.tail = this.tail.prev;
        if (this.tail !== null) {
            this.tail.next = null;
        } else {
            this.head = null;
        }
        console.log("Elemento eliminado desde el final");
    }

    deleteRandom() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        const pos = this._getValue("Ingresa la posicion:");
        let current = this.head;

        for (let i = 0; i < pos; i++) {
            if (current === null) {
                console.log("La posicion no existe");
                return;
            }
            current = current.next;
        }

        if (current.prev !== null) {
            current.prev.next = current.next;
        } else {
            this.head = current.next;
        }

        if (current.next !== null) {
            current.next.prev = current.prev;
        } else {
            this.tail = current.prev;
        }
        console.log(`Elemento eliminado desde la posicion ${pos}`);
    }

    search() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        const value = this._getValue("Ingrese el valor a buscar:");
        let temp = this.head;
        let pos = 0;
        while (temp !== null) {
            if (temp.data === value) {
                console.log(`Valor ${value} encontrado en la posicion ${pos}`);
                return;
            }
            temp = temp.next;
            pos++;
        }
        console.log(`Valor ${value} no encontrado en la lista`);
    }

    display() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        let temp = this.head;
        let output = "Lista Doble: ";
        while (temp !== null) {
            output += `${temp.data} <-> `;
            temp = temp.next;
        }
        console.log(output + "NULL");
    }
}

function main() {
    const dllJS = new DoublyLinkedList();
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
                dllJS.insertbeg();
                break;
            case 2:
                dllJS.insertend();
                break;
            case 3:
                dllJS.randominsert();
                break;
            case 4:
                dllJS.deletebeg();
                break;
            case 5:
                dllJS.deleteend();
                break;
            case 6:
                dllJS.randomdelete();
                break;
            case 7:
                dllJS.display();
                break;
            case 8:
                dllJS.search();
                break;
            case 9:
                return;
            default:
                console.log("Opcion invalida! Por favor intenta de nuevo.");
        }
    }
}


main();