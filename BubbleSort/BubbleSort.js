function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

let arr = new Array(15);

for(let i=0;i<arr.length;i++){
    arr[i]=random(1,100);
}
console.log("\nArreglo Original: ");

for(let i=0;i<arr.length;i++){
    console.log(arr[i])
}

let mayor=0;

for(let i=0;i<arr.length;i++){
    for(let j=0;j<arr.length-i-1;j++){
        if(arr[j]>arr[j+1]){
            mayor=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=mayor
        }
    }
}

console.log("\nArreglo Ordenado: ");

for(let i=0;i<arr.length;i++){
    console.log(arr[i])
}