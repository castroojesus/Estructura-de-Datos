class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class CircularLinkedList {
    constructor() {
        this.last = null;
    }

    
    _getValue(promptMsg) {
        let value = prompt(promptMsg);
        
        while (value === null || isNaN(parseInt(value))) {
            value = prompt("Entrada inválida. " + promptMsg);
        }
        return parseInt(value);
    }

    

    insertBegin() {
        const value = this._getValue("Ingrese un valor para el inicio:");
        const newNode = new Node(value);
        
        if (this.last === null) {
            this.last = newNode;
            this.last.next = this.last;
        } else {
            newNode.next = this.last.next;
            this.last.next = newNode;
        }
    }
    
    insertEnd() {
        const value = this._getValue("Ingrese un valor para el final:");
        const newNode = new Node(value);

        if (this.last === null) {
            this.last = newNode;
            this.last.next = this.last;
        } else {
            newNode.next = this.last.next;
            this.last.next = newNode;
            this.last = newNode; 
        }
    }
    
    insertRandom() {
        const value = this._getValue("Ingrese un valor:");
        const pos = this._getValue("Ingrese la posicion donde desea insertar:");

        const newNode = new Node(value);
        
        if (this.last === null) {
            if (pos <= 0) {
                this.last = newNode;
                this.last.next = this.last;
                console.log("Lista vacía, insertado al inicio/posición 0.");
            }
            return;
        }
        if (pos <= 0) {
            this.insertBegin(); 
            return;
        }

        let current = this.last.next;
        
        for (let i = 0; i < pos - 1; i++) {
            if (current === this.last) {
                
                break; 
            }
            current = current.next;
        }
        
        newNode.next = current.next;
        current.next = newNode;
        
        if (current === this.last) {
            this.last = newNode; 
        }
    }

   

    deleteBegin() {
        if (this.last === null) {
            console.log("La lista esta vacia");
            return;
        }
        const temp = this.last.next; 
        if (this.last.next === this.last) { 
            this.last = null;
        } else {
            this.last.next = temp.next; 
        }
        console.log(`Elemento ${temp.data} eliminado del inicio.`);
        
    }

    deleteEnd() {
        if (this.last === null) {
            console.log("La lista esta vacia");
            return;
        }
        if (this.last.next === this.last) { 
            this.last = null;
            console.log("Elemento único eliminado.");
            return;
        }
        
        let temp = this.last.next; 
        while (temp.next !== this.last) {
            temp = temp.next;
        }
        

        temp.next = this.last.next; 
        this.last = temp; 
        console.log("Elemento eliminado desde el final");
    }
    
    deleteRandom() {
        if (this.last === null) {
            console.log("La lista esta vacia");
            return;
        }
        const pos = this._getValue("Ingresa la posicion a eliminar:");

        let current = this.last.next;
        let previous = this.last; 

        if (pos === 0) {
            this.deleteBegin();
            return;
        }

        for (let i = 0; i < pos; i++) {
             if (current === this.last.next && i > 0) {
                console.log("La posicion no existe");
                return;
            }
            previous = current;
            current = current.next; 
        }
        
        previous.next = current.next; 
        
        if (current === this.last) {
            this.last = previous; 
        }
        console.log(`Elemento eliminado desde la posicion ${pos}`);
    }


    
    search() {
        if (this.last === null) {
            console.log("La lista esta vacia");
            return;
        }
        const value = this._getValue("Ingrese el valor a buscar:");
        let temp = this.last.next;
        let pos = 0;
        
        do {
            if (temp.data === value) {
                console.log(`Valor ${value} encontrado en la posicion ${pos}`);
                return;
            }
            temp = temp.next;
            pos++;
        } while (temp !== this.last.next);
        
        console.log(`Valor ${value} no encontrado en la lista`);
    }

    display() {
        if (this.last === null) {
            console.log("La lista esta vacia");
            return;
        }
        let temp = this.last.next;
        let output = "Lista Circular: ";
        do {
            output += `${temp.data}-> `;
            temp = temp.next;
        } while (temp !== this.last.next);
        console.log(output + "inicio");
    }
}

function main() {
    const cllJS = new CircularLinkedList();
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
                cllJS.insertbeg();
                break;
            case 2:
                cllJS.insertend();
                break;
            case 3:
                cllJS.randominsert();
                break;
            case 4:
                cllJS.deletebeg();
                break;
            case 5:
                cllJS.deleteend();
                break;
            case 6:
                cllJS.randomdelete();
                break;
            case 7:
                cllJS.display();
                break;
            case 8:
                cllJS.search();
                break;
            case 9:
                return;
            default:
                console.log("Opcion invalida! Por favor intenta de nuevo.");
        }
    }
}


main();