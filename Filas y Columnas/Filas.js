let TwoDArray=[[1,2,3],[4,5,6],[7,8,9]];



console.log("Los elementos del array bidimensional son: ");
for(let x=0;x<TwoDArray.length;x++){
    let fila =" ";
    for(let y=0;y<TwoDArray.length;y++){
        fila+=TwoDArray[x][y]+ " ";
    }
    console.log(fila);
}
console.log("\nLos elementos del array unidimensional son: ");
for(let x=0;x<TwoDArray.length;x++){
    let resultado =" ";
    for(let y=0;y<TwoDArray.length;y++){
        resultado+=TwoDArray[x][y]+ " ";
    }
console.log(resultado);
}
