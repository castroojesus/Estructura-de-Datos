class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
        this.prev = null;
    }
}

class DoublyCircularLinkedList {
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
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            newNode.next = this.head;
            newNode.prev = this.tail;
            this.head.prev = newNode;
            this.tail.next = newNode;
            this.head = newNode;
        }
    }

    insertend() {
        const value = this._getValue("Ingrese un valor:");
        const newNode = new Node(value);
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            newNode.next = this.head;
            newNode.prev = this.tail;
            this.tail.next = newNode;
            this.head.prev = newNode;
            this.tail = newNode;
        }
    }

    insertrandom() {
        const value = this._getValue("Ingrese un valor:");
        const pos = this._getValue("Ingrese la posicion donde desea insertar:");
        const newNode = new Node(value);
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
            newNode.next = newNode;
            newNode.prev = newNode;
        } else {
            let current = this.head;
            for (let i = 0; i < pos; i++) {
                current = current.next;
                if (current === this.head) break;
            }
            newNode.next = current;
            newNode.prev = current.prev;
            current.prev.next = newNode;
            current.prev = newNode;
            if (current === this.head && pos === 0) this.head = newNode;
            if (current === this.head) this.tail = newNode;
        }
    }

    deletebegin() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        if (this.head === this.tail) {
            this.head = null;
            this.tail = null;
        } else {
            const temp = this.head;
            this.head = this.head.next;
            this.head.prev = this.tail;
            this.tail.next = this.head;
        }
        console.log("Elemento eliminado desde el inicio");
    }

    deleteend() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        if (this.head === this.tail) {
            this.head = null;
            this.tail = null;
        } else {
            const temp = this.tail;
            this.tail = this.tail.prev;
            this.tail.next = this.head;
            this.head.prev = this.tail;
        }
        console.log("Elemento eliminado desde el final");
    }

    deleteRandom() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        let current = this.head;
        const pos = this._getValue("Ingresa la posicion:");
        for (let i = 0; i < pos; i++) {
            current = current.next;
            if (current === this.head) {
                console.log("La posicion no existe");
                return;
            }
        }
        current.prev.next = current.next;
        current.next.prev = current.prev;
        if (current === this.head) this.head = current.next;
        if (current === this.tail) this.tail = current.prev;
        if (this.head === null) this.tail = null;
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
        do {
            if (temp.data === value) {
                console.log(`Valor ${value} encontrado en la posicion ${pos}`);
                return;
            }
            temp = temp.next;
            pos++;
        } while (temp !== this.head);
        console.log(`Valor ${value} no encontrado en la lista`);
    }

    display() {
        if (this.head === null) {
            console.log("La lista esta vacia");
            return;
        }
        let temp = this.head;
        let output = "Lista Doble Circular: ";
        do {
            output += `${temp.data} <-> `;
            temp = temp.next;
        } while (temp !== this.head);
        console.log(output + "inicio");
    }
}

function main() {
    const dcllJS = new DoublyCircularLinkedList();
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
                dcllJS.insertbeg();
                break;
            case 2:
                dcllJS.insertend();
                break;
            case 3:
                dcllJS.randominsert();
                break;
            case 4:
                dcllJS.deletebeg();
                break;
            case 5:
                dcllJS.deleteend();
                break;
            case 6:
                dcllJS.randomdelete();
                break;
            case 7:
                dcllJS.display();
                break;
            case 8:
                dcllJS.search();
                break;
            case 9:
                return;
            default:
                console.log("Opcion invalida! Por favor intenta de nuevo.");
        }
    }
}


main();