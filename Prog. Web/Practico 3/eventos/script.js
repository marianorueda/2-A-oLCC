// 1. Función para mostrar un saludo en el elemento <p> al hacer clic en "SALUDAR"
function saludar() {
    const saludoElemento = document.getElementById('saludo');
    saludoElemento.textContent = '¡Hola, bienvenido a la práctica de JavaScript!';
}

// 2. Cambiar el color de fondo del header y footer después de 5 segundos
window.addEventListener('load', function() {
    setTimeout(() => {
        const header = document.querySelector('header');
        const footer = document.querySelector('footer');
        
        header.style.backgroundColor = 'lightblue';
        footer.style.backgroundColor = 'lightblue';
    }, 5000);
});

// 3. Función para obtener datos de la API y mostrar los primeros 10 elementos
function obtenerDatos() {
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(response => response.json())
        .then(data => {
            // Verificar si ya existe el elemento UL
            let lista = document.getElementById('dataList');
            if (!lista) {
                lista = document.createElement('ul');
                lista.id = 'dataList';
                document.body.appendChild(lista);  // Insertar la lista en el body
            }

            // Limpiar la lista antes de agregar los datos
            lista.innerHTML = '';

            // Mostrar los primeros 10 elementos de la respuesta
            data.slice(0, 10).forEach(post => {
                const listItem = document.createElement('li');
                listItem.textContent = post.title;
                lista.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error al obtener datos:', error));
}

// Añadir evento al botón GET DATA (como tiene id, usamos getElementById)
document.getElementById('getDataBtn').addEventListener('click', obtenerDatos);
