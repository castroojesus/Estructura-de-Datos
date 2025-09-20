function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}
function insertionSort(a) {
    for (let i = 1; i < a.length; i++) {
        let current = a[i];
        let j = i - 1;
        
        while (j >= 0 && a[j] > current) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = current;
    }
    return a;
}
function printarray(a){
    for(let i=0;i<a.length;i++){
    console.log(a[i])
}
}

let arr=new Array(15)

for(let i=0;i<arr.length;i++){
    arr[i]=random(1,100);
}
console.log("\nArreglo Original: ");

printarray(arr)
insertionSort(arr)
console.log("\nArray Ordenado: ")
printarray(arr)

