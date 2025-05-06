document.addEventListener("DOMContentLoaded", function(){

    let c = document.getElementById(("boton"));

    c.addEventListener("mouseover", function(){
        this.style.color = "blue";
    })

    c.addEventListener("mouseout", function(){
        this.style.color = "black";
    })

    c.addEventListener("click", function(){
        this.style.color = "green";
        let peso = document.getElementById("peso").value;
        let act = document.getElementById("act").value;
        let agua = 0;
        if(act === "" || isNaN(peso) || peso<=0){
            document.getElementById("resultado").innerText = "Ingrese Valores Validos";
            alert("Error");
        }
        else{
            if(act=="sedentario"){
                agua = 35*peso;
                document.getElementById("resultado").innerText = "Debes beber " + agua + " ml de agua diarios";
            }
            else if(act=="moderado"){
                agua = 40*peso;
                document.getElementById("resultado").innerText = "Debes beber " + agua + " ml de agua diarios";
            }
            else if(act=="activo"){
                agua = 45*peso;
                document.getElementById("resultado").innerText = "Debes beber " + agua + " ml de agua diarios";
            }
            if(agua<2000){
                document.getElementById("resultado").style.backgroundColor = "red";
            }
            else if(agua<3000){
                document.getElementById("resultado").style.backgroundColor = "yellow";
            }
            else{
                document.getElementById("resultado").style.backgroundColor = "green";
            }
        }
    })
})