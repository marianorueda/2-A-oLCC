// Ejemplo de var
function ejemploVar() {
    if (true) {
        var x = 10; // Declarada dentro del bloque
    }
    console.log(x); // Funciona: x = 10 (var tiene ámbito de función, no de bloque)
}
ejemploVar();


// Ejemplo de let
function ejemploLet() {
    if (true) {
        let y = 20; // Declarada dentro del bloque
    }
    console.log(y); // Error: y is not defined (let tiene ámbito de bloque)
}
ejemploLet();


// Ejemplo de const
function ejemploConst() {
    const z = 30; // z no puede ser reasignada
    z = 40; // Error: Assignment to constant variable
    console.log(z); // 30
}
ejemploConst();


// Ejemplo de hoisting con var
console.log(a); // undefined (por el hoisting)
var a = 10;
console.log(a); // 10 (ya está inicializada)


// Ejemplo de hoisting con funciones
saludar(); // "Hola Mundo!"

function saludar() {
    console.log("Hola Mundo!");
}


//Ejemplo de problemas con var
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i); // Imprime 3 tres veces, en lugar de 0, 1, 2
    }, 100);
}


// Ejemplo de tipos de funciones

// Función declarada, con retorno
function sum(a, b) {
    return a + b;
}

console.log(sum(5, 3)); // 8


// Función anónima
const sum = function(a, b) {
    return a + b;
};

console.log(sum(5, 3)); // 8


// Función flecha
const sum = (a, b) => a + b;

console.log(sum(5, 3)); // 8


// Función como método
let calculadora = {
    sum: function(a, b) {
        return a + b;
    }
};

console.log(calculadora.sum(5, 3)); // 8


// Función de Orden Superior
function calcular(a, b, operacion) {
    return operacion(a, b);
}

console.log(calcular(5, 3, sum)); // 8




// Manejo de arreglos

const arreglo = [1, 2, 3, 4, 5, 6, 11, 23, 1, 989, 0, 1, 111, 645, 50, 45];

// a. Retornar el menor elemento del arreglo
const menorElemento = arreglo.reduce((menor, actual) => (actual < menor ? actual : menor), arreglo[0]);
console.log(menorElemento); // 0

// b. Retornar la suma de todos los elementos del arreglo
const sumaTotal = arreglo.reduce((total, actual) => total + actual, 0);
console.log(sumaTotal); // 1897

// c. Retornar un arreglo donde cada elemento es el doble que en el arreglo original
const arregloDoble = arreglo.map(numero => numero * 2);
console.log(arregloDoble);
// [2, 4, 6, 8, 10, 12, 22, 46, 2, 1978, 0, 2, 222, 1290, 100, 90]

// d. Retornar un arreglo con los elementos que sean mayores o iguales a 10
const elementosMayoresDiez = arreglo.filter(numero => numero >= 10);
console.log(elementosMayoresDiez);
// [11, 23, 989, 111, 645, 50, 45]

// e. Retornar el índice del primer elemento mayor a 10
const indicePrimerMayorDiez = arreglo.findIndex(numero => numero > 10);
console.log(indicePrimerMayorDiez); // 6


// Definir e instanciar la clase Automóvil

// Definir la clase
class Automovil {
    constructor(ruedas, puertas, color, velocidad) {
        this.ruedas = ruedas;
        this.puertas = puertas;
        this.color = color;
        this.velocidad = velocidad;
    }

    // Método para aumentar la velocidad
    aumentarVelocidad(incremento) {
        this.velocidad += incremento;
    }
}

// Instanciar un objeto de la clase Automóvil
const miAutomovil = new Automovil(4, 5, "Negro", 60);