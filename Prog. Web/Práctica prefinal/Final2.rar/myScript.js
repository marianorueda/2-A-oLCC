document.addEventListener("DOMContentLoaded", function(){

    let boton = document.getElementById("boton");

    boton.addEventListener("mouseover", function(){
        this.style.backgroundColor=("white");
        this.style.color=("black");
    })
    boton.addEventListener("mouseout", function(){
        this.style.backgroundColor=("black");
        this.style.color=("white");
    })

    boton.addEventListener("click", function(){
        let peso = parseFloat(document.getElementById("peso").value);
        let altura = parseFloat(document.getElementById("altura").value);
        console.log("PESO:",peso,"ALTURA:",altura);
        if (isNaN(peso) || isNaN(altura) || peso<=0 || altura<=0){
            document.getElementById("resultado").textContent = "Ingrese valores validos de peso y altura";
        }
        else{
            let imc;
            if(altura==1 || altura==2){
                imc = peso/( altura*altura );
            }
            else if(Number.isInteger(altura)){
                imc = (peso/( altura**2 ))*10000;
                console.log("ENTRE")
            }
            else{
                imc = peso/( altura*altura );
            }
            console.log("puto", imc);
            document.getElementById("resultado").innerText = "Tu IMC es: "+ imc;
        }
        
    })

})