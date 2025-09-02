const readline = require("readline");


const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let miArray = [1, 2, 3, 4, 5];

rl.question("Escriba el índice del elemento que desea buscar (0 a 4): ", (input) => {
  const busqueda = parseInt(input);

  
  if (busqueda < 0 || busqueda >= miArray.length) {
    console.log("Error: el índice está fuera del rango del array.");
  } else {
    console.log(`El elemento que se encuentra en el índice ${busqueda} es: ${miArray[busqueda]}`);
  }

  rl.close(); 
});
