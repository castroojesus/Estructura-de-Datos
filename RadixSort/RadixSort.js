function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}

function printarray(a){
    for(let i=0;i<a.length;i++){
    console.log(a[i])
}
}

function countingSortForRadix(inputArr, place) {
    let outputArr = new Array(inputArr.length).fill(0);
    let countArr = new Array(10).fill(0);
    for (let i = 0; i < inputArr.length; i++) {
        let digit = Math.floor((inputArr[i] / place) % 10);
        countArr[digit]++;
    }
    for (let i = 1; i < countArr.length; i++) {
        countArr[i] += countArr[i - 1];
    }
    for (let i = inputArr.length - 1; i >= 0; i--) {
        let digit = Math.floor((inputArr[i] / place) % 10);
        outputArr[countArr[digit] - 1] = inputArr[i];
        countArr[digit]--;
    }
    for (let i = 0; i < inputArr.length; i++) {
        inputArr[i] = outputArr[i];
    }
}

function radix_sort(inputArr) {
    let maxVal = Math.max(...inputArr);
    for (let place = 1; Math.floor(maxVal / place) > 0; place *= 10) {
        countingSortForRadix(inputArr, place);
    }
}
let arr=new Array(15)

for(let i=0;i<arr.length;i++){
    arr[i]=random(1,100);
}
console.log("\nArreglo Original: ");

printarray(arr)
radix_sort(arr)
console.log("\nArray Ordenado: ")
printarray(arr)