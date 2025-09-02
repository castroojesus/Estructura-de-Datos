let miArray=[1,2,3,4,5];
let posicion = 4;
let nuevo=102;

console.log("Los elementos del array antes de la insercion son: ");

for(let i=0;i<5;i++){
    console.log(miArray[i]);
}

for(let i=4;i>posicion;i--){
    miArray[i]=miArray[i-1];
}

miArray[posicion]=nuevo

console.log("Los elementos del array antes de la insercion son: ");

for(let i=0;i<5;i++){
    console.log(miArray[i]);
}
