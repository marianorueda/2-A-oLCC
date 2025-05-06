document.addEventListener("DOMContentLoaded", function(){
    let c = this.getElementById("calcular");

    c.addEventListener("mouseover", function(){
        this.style.color = "black";
        this.style.backgroundColor = "white";
    });

    c.addEventListener("mouseout" ,function(){
        this.style.color = "white";
        this.style.backgroundColor = "black";
    });

    c.addEventListener("click", function(){
        let xedad = parseInt(document.getElementById("edad").value);
        let xfrec = parseInt(document.getElementById("frec").value);
        if(xedad > 0 && xfrec > 0){
            let fcm = parseFloat(220 - xedad);
            let zona = (xfrec * 100)/ fcm;
            document.getElementById("resultado1").innerText = "Tu Frecuencia Cardiaca Maxima es: " + fcm;
            if (zona>90){
                document.getElementById("resultado2").innerText = "Te encuentras en la Zona 5: Esfuerzo Maximo";
                resultado2.style.backgroundColor = "red"
            }
            else if (zona>80){
                document.getElementById("resultado2").innerText = "Te encuentras en la Zona 4: Umbral Anaeróbico";
                resultado2.style.backgroundColor = "oranje"
            }
            else if (zona>70){
                document.getElementById("resultado2").innerText = "Te encuentras en la Zona 3: Resistencia Aeróbica";
                resultado2.style.backgroundColor = "yellow"
            }
            else if (zona>60){
                document.getElementById("resultado2").innerText = "Te encuentras en la Zona 2: Quema de Grasa";
                resultado2.style.backgroundColor = "green"
            }
            else if(zona > 50){
                document.getElementById("resultado2").innerText = "Te encuentras en la Zona 1: Calentamiento";
                resultado2.style.backgroundColor = "blue"
            }
            else if(zona < 50){
                document.getElementById("resultado2").innerText = "Levantate vagote/a";
            }
            else{
                document.getElementById("resultado2").innerText = "Para un poco mostro";
            }
            }   
        else{
            document.getElementById("resultado1").innerText = "Ingrese Valores Validos"
        } 
    })
})