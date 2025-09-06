const r=3;
const c=3;
let arr=new Array[r*c].fill(0);
let TwoDArray=[[1,2,3],[4,5,6],[7,8,9]];
let k=0;

for(let y=0;y<c;y++){
    for(let x=0;x<r;x++){
        k=y*r+x;
        arr[k]=TwoDArray[x][y];
        k=k+1;
    }
}
console.log("Los elementos del array bidimensional son: ");
for(let x=0;x<r;x++){
    let fila =" ";
    for(let y=0;y<c;y++){
        fila+=TwoDArray[x][y]+ " ";
    }
    console.log(fila);
}
console.log("\nLos elementos del array bidimensional son: ");
for(let y=0;y<c;y++){
    let resultado =" ";
    for(let x=0;x<r;x++){
        resultado+=arr[y*r+x]+ " ";
    }
    console.log(resultado);
}
