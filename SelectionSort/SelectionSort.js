function random(min, max){
    return Math.floor(Math.random()*(max-min+1))+min;
}
function SelectionSort(a) {
    for (let i = 0; i < a.length; i++) {
        let small=1
        for (let j=i+1;j<a.length;j++){
            if (a[j]<a[small]){
                small=j
            }
            let temp=a[small]
            a[small]=a[i]
            a[i]=temp
        }
        
        
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
SelectionSort(arr)
console.log("\nArray Ordenado: ")
printarray(arr)