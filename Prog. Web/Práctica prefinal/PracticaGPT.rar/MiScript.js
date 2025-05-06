document.addEventListener("DOMContentLoaded", function () {
    let a = document.getElementById("a");
    let b = document.getElementById("b");
    let operador = document.getElementById("operador");

    let c = document.getElementById("boton");

    c.addEventListener("click", function () {
        let num1 = parseFloat(a.value);
        let num2 = parseFloat(b.value);
        let operadorValue = operador.value;
        let resultado;

        if (operadorValue == "+") {
            resultado = num1 + num2;
            alert("El resultado de la suma es: " + resultado);
        }
        else if (operadorValue == "-") {
            resultado = num1 - num2;
            alert("El resultado de la resta es: " + resultado);
        }
        else if (operadorValue == "*") {
            resultado = num1 * num2;
            alert("El resultado de la multiplicación es: " + resultado);
        }
        else if (operadorValue == "/") {
            if (num2 !== 0) {
                resultado = num1 / num2;
                alert("El resultado de la división es: " + resultado);
            } else {
                alert("Error: División por cero");
            }
        }
        else {
            alert("Operador no válido");
        }
    });
});
