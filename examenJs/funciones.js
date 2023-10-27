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


  /////
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

////
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
///
const numbers = [0.5, 12, 2, 99];
const newArr = numbers.map(Ifunction);
function Ifunction(num) {
  return num * 2;
}
console.log (newArr);
