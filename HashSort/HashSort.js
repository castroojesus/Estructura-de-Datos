function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

function printarray(a){
    for(let i=0;i<a.length;i++){
    console.log(a[i])
}
}

function shellSort(arr) {
    let n = arr.length;
    for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {
        for (let i = gap; i < n; i++) {
            let temp = arr[i];
            let j;
            for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
                arr[j] = arr[j - gap];
            }
            arr[j] = temp;
        }
    }
    return arr;
} 


let arr=new Array(15)
for(let i=0;i<arr.length;i++){
    arr[i]=random(1,100);
}
console.log("\nArreglo Original: ");
printarray(arr);
console.log("\nArreglo Ordenado con Heap Sort: ");
let sortedArray = shellSort(arr);
printarray(sortedArray);