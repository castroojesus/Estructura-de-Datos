function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

function printarray(a){
    for(let i=0;i<a.length;i++){
    console.log(a[i])
}
}

function heapify(arr, n, i) {
    let largest = i; 
    let left = 2 * i + 1; 
    let right = 2 * i + 2;
    if (left < n && arr[left] > arr[largest])
        largest = left;
    if (right < n && arr[right] > arr[largest])
        largest = right;
    if (largest != i) {
        let swap = arr[i];
        arr[i] = arr[largest];
        arr[largest] = swap;
        heapify(arr, n, largest);
    }
}
function heapSort(arr) {
    let n = arr.length;
    for (let i = Math.floor(n / 2) - 1; i >= 0; i--)
        heapify(arr, n, i);
    for (let i = n - 1; i > 0; i--) {
        let temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
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
let sortedArray = heapSort(arr);
printarray(sortedArray);