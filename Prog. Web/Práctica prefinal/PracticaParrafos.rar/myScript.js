document.addEventListener("DOMContentLoaded", function(){

    let a = document.getElementById("agregar");
    let b = document.getElementById("eliminar");
    let here = document.getElementById("aca");

    a.addEventListener("click", function(){
        let parrafo = document.createElement("h1")
        parrafo.textContent = "FACU GAY MONO MANCO EN EL BS";
        here.appendChild(parrafo);
    })

    b.addEventListener("click", function(){
        let borrar = here.lastElementChild;
        here.removeChild(borrar);
    })

})