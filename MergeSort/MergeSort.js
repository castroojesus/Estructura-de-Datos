function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

function printarray(a){
    for(let i=0;i<a.length;i++){
    console.log(a[i])
}
}

function merge(left, right) {
    let result = [];
    let i = 0;
    let j = 0;
    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            result.push(left[i]);
            i++;
        } else {
            result.push(right[j]);
            j++;
        }       
    }
    return result.concat(left.slice(i)).concat(right.slice(j));
}   

function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }       
    let mid = Math.floor(arr.length / 2);
    let left = arr.slice(0, mid);
    let right = arr.slice(mid);
    return merge(mergeSort(left), mergeSort(right));
}

let arr=new Array(15)

for(let i=0;i<arr.length;i++){
    arr[i]=random(1,100);
}
console.log("\nArreglo Original: ");
printarray(arr);
console.log("\nArreglo Ordenado con Merge Sort: ");
let sortedArray = mergeSort(arr);
printarray(sortedArray);