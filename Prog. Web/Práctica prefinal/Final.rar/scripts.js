document.addEventListener("DOMContentLoaded", function(){
    let peso = document.getElementById("peso");
    let altura = document.getElementById("altura");
    let c = document.getElementById("calculo");

    c.addEventListener("mouseover", function(){
        this.style.color= "black";
        this.style.backgroundColor = "white";
    })

    c.addEventListener("mouseout", function(){
        this.style.color= "white";
        this.style.backgroundColor = "black";
    })

    c.addEventListener("click", function(){
        let imc
        let xpeso = parseFloat(peso.value);
        let xaltura = parseFloat(altura.value);
        if(xpeso > 0 && xaltura>0){
            if(Number.isInteger(xaltura)){
                imc = (xpeso/(xaltura**2))*10000;
            }
            else{
                imc = xpeso/(xaltura**2);
            }
            if(imc>30){
                document.getElementById("resultado").innerText = "Tu IMC es: " + imc + " Obeso";
                resultado.style.backgroundColor = "red"
            }
            else if(imc>25){
                resultado.textContent = "Tu IMC es: " + imc + " Sobrepeso";
                resultado.style.backgroundColor = "brown"
            }
            else if(imc>18.5){
                resultado.textContent = "Tu IMC es: " + imc + " Normal";
                resultado.style.backgroundColor = "green"
            }
            else{
                resultado.textContent = "Tu IMC es: " + imc + " Bajo de peso"
                resultado.style.backgroundColor = "yellow"
            }
        }
        else{
            resultado.textContent = 'Error: Ingrese Valores Validos';
        }
    })
})