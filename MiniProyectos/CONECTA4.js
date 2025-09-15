let Conecta4 = [];
for (let i = 0; i < 6; i++) {
    Conecta4[i] = [];
    for (let j = 0; j < 7; j++) {
        Conecta4[i][j] = 0;
    }
}

let name1 = prompt("Jugador 1 ingrese su nombre: ");
let name2 = prompt("Jugador 2 ingrese su nombre: ");
let turno = 0;
let ganador = false;

function verificarGanador(fila, columna, jugador) {
    
    let count = 0;
    for (let j = 0; j < 7; j++) {
        count = (Conecta4[fila][j] === jugador) ? count + 1 : 0;
        if (count >= 4) return true;
    }
    
    
    count = 0;
    for (let i = 0; i < 6; i++) {
        count = (Conecta4[i][columna] === jugador) ? count + 1 : 0;
        if (count >= 4) return true;
    }
    
    
    count = 0;
    let i = fila - Math.min(fila, columna);
    let j = columna - Math.min(fila, columna);
    while (i < 6 && j < 7) {
        count = (Conecta4[i][j] === jugador) ? count + 1 : 0;
        if (count >= 4) return true;
        i++;
        j++;
    }
    
    
    count = 0;
    i = fila - Math.min(fila, 6 - columna);
    j = columna + Math.min(fila, 6 - columna);
    while (i < 6 && j >= 0) {
        count = (Conecta4[i][j] === jugador) ? count + 1 : 0;
        if (count >= 4) return true;
        i++;
        j--;
    }
    
    return false;
}

while (turno < 42 && !ganador) {
    console.log("\nTablero actual:");
    console.log("  1     2     3     4     5     6     7");
    console.log("=============================================");

    for (let i = 0; i < 6; i++) {
        let fila = "";
        for (let j = 0; j < 7; j++) {
            let simbolo = " ";
            if (Conecta4[i][j] === 1) simbolo = "X";
            if (Conecta4[i][j] === 2) simbolo = "O";
            
            fila += `  ${simbolo}  `;
            if (j < 6) fila += "|";
        }
        console.log(fila);
        
        if (i < 5) {
            console.log("---------------------------------------------");
        }
    }

    let jugadorActual = (turno % 2 === 0) ? 1 : 2;
    let nombreJugador = (jugadorActual === 1) ? name1 : name2;
    
    let columnaValida = false;
    let columna;
    
    while (!columnaValida) {
        columna = parseInt(prompt(`${nombreJugador}, elige una columna (1-7): `)) - 1;
        
        if (columna >= 0 && columna < 7) {
            if (Conecta4[0][columna] === 0) {
                columnaValida = true;
            } else {
                alert("¡Columna llena! Elige otra.");
            }
        } else {
            alert("Columna inválida. Debe ser entre 1 y 7.");
        }
    }
    
    let fila;
    for (fila = 5; fila >= 0; fila--) {
        if (Conecta4[fila][columna] === 0) {
            Conecta4[fila][columna] = jugadorActual;
            break;
        }
    }
    
    
    ganador = verificarGanador(fila, columna, jugadorActual);
    
    
    if (!ganador) {
        turno++;
    }
}


console.log("\nTablero final:");
console.log("  1     2     3     4     5     6     7");
console.log("=============================================");

for (let i = 0; i < 6; i++) {
    let fila = "";
    for (let j = 0; j < 7; j++) {
        let simbolo = " ";
        if (Conecta4[i][j] === 1) simbolo = "X";
        if (Conecta4[i][j] === 2) simbolo = "O";
        
        fila += `  ${simbolo}  `;
        if (j < 6) fila += "|";
    }
    console.log(fila);
    
    if (i < 5) {
        console.log("---------------------------------------------");
    }
}


if (ganador) {
    let ganadorNombre = (turno % 2 === 0) ? name1 : name2;
    console.log(`\n¡Felicidades ${ganadorNombre}, has ganado!`);
} else {
    console.log("\n¡Empate! El tablero está lleno.");
}
