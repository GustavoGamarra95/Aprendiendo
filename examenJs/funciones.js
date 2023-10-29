///1
function numerosPares(array) {
    const pares = [];
    for (const numero of array) {
      if (numero % 2 === 0) {
        pares.push(numero);
      }
    }
    return pares;
  }

  const array = [1,2,3,4,5,6,60,78,55];
  const pares = numerosPares(array);
  console.log(pares);

/////2
let numerosImpares = function() {
    const impares = [];
    for (const numero of [1, 2, 3, 4, 5]) {
        if (numero % 2 === 1) {
            impares.push(numero);
        }
    }
    return impares;
}
console.log(numerosImpares());

////3
//Uma função recursiva é uma função que chama a si mesma até encontrar uma instrução de parar. Essa técnica é chamada de recursão.
//Resultado Factorial multiplicação desse número pelos seus antecessores maiores que zero.
function recursiva(n){
    if (n===0){
        return 1;
    } else {
        return n*recursiva(n-1);
    }
}
console.log(recursiva(5));
///4
const numbers = [0.5, 12, 2, 99];
const newArr = numbers.map(Ifunction);
function Ifunction(num) {
  return num * 2;
}
console.log (newArr);

///5 

const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const numerosPares1 = numeros.filter(numero => numero % 2 === 0);
console.log(numerosPares1); 

///6 
const mayor5 = [5, 0, 15, 25, 1, 2 , 3];
const Mayor5 = mayor5.find( elemento => elemento > 5);
console.log(Mayor5);

///7
const array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const elemento4 = array4.indexOf(4);
console.log(elemento4);

///8
const arrayNuevo = Array(5).fill(0);
console.log(arrayNuevo);
///9
const Somearray = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const numPar= Somearray.some( numero => Math.floor(numero / 2) == 0);
console.log(numPar);

///10
const numero = [5, 0, 15, 25, 1, 2 , 3];
const num10 = numero.every( numero => numero <10);
console.log(num10);

const numero1 = [1, 2, 3, 4, 5];
const num11 = numero1.every( numero => numero <10);
console.log(num11);
