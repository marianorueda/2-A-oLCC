document.addEventListener("DOMContentLoaded", function(){

    let c = document.getElementById("boton");
    let info = document.getElementById("info");

    c.addEventListener("click", function(){
        if (info.lastElementChild){
            let borrar = info.lastElementChild;
            info.removeChild(borrar);
        }
        let destino = document.getElementById("destino").value;
        let dias = parseInt(document.getElementById("dias").value);
        let presupuesto = parseFloat(document.getElementById("presupuesto").value);
        let tipo = document.getElementById("tipo").value;
        if(destino && dias>0 && presupuesto>0 && tipo){
            let costo;
            if(tipo=="economico"){
                costo = 30*dias;
            }
            else if(tipo=="estandar"){
                costo = 50*dias;
            }
            else{
                costo = 100*dias;
            }
            if(costo <= presupuesto){
                let parrafo = document.createElement("p");
                parrafo.textContent = "El presupuesto cubre el costo del viaje";
                info.appendChild(parrafo);
            }
            else{
                let falta = costo-presupuesto;
                let parrafo = document.createElement("p");
                parrafo.textContent = "El presupuesto NO cubre el costo del viaje, faltan "+falta+" pesos";
                info.appendChild(parrafo);
            }
        }
        else{
            let parrafo = document.createElement("p");
                parrafo.textContent = "Ingrese datos validos";
                info.appendChild(parrafo);
        }
    })

})