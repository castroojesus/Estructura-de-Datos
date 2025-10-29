function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

function printarray(a){
    for(let i=0;i<a.length;i++){
    console.log(a[i])
}
}

function insertionSort(bucket) {
    for (let j = 1; j < bucket.length; j++) {
        let key = bucket[j];
        let i = j - 1;
        while (i >= 0 && bucket[i] > key) {
            bucket[i + 1] = bucket[i];
            i = i - 1;
        }
        bucket[i + 1] = key;
    }
}
function bucketSort(inputArr) {
    let s = inputArr.length;
    let bucketArr = new Array(s);
    for (let i = 0; i < s; i++) {
        bucketArr[i] = [];
    }
    let maxVal = Math.max(...inputArr);
    // Distribuir los elementos en los buckets
    for (let j = 0; j < inputArr.length; j++) {
        let normalized = inputArr[j] / (maxVal + 1);
        let bi = Math.floor(s * normalized);
        bucketArr[bi].push(inputArr[j]);
    }
    // Ordenar cada bucket con insertion sort
    for (let i = 0; i < bucketArr.length; i++) {
        insertionSort(bucketArr[i]);
    }
    // Concatenar los buckets ordenados en el array de entrada
    let idx = 0;
    for (let i = 0; i < bucketArr.length; i++) {
        for (let j = 0; j < bucketArr[i].length; j++) {
            inputArr[idx] = bucketArr[i][j];
            idx++;
        }
    }
}

let arr=new Array(15)

for(let i=0;i<arr.length;i++){
    arr[i]=random(1,100);
}
console.log("\nArreglo Original: ");

printarray(arr)
bucketSort(arr)
console.log("\nArray Ordenado: ")
printarray(arr)
