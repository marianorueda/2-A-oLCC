// Obtener el formulario y el área para mostrar mensajes
const form = document.getElementById('registroForm');
const mensaje = document.getElementById('mensaje');

// Lista de nombres de usuario prohibidos
const nombresProhibidos = ['Ana', 'Pepe', 'Pancho'];

// Función de validación
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    // Obtener los valores de los campos
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const confirmPassword = document.getElementById('confirmPassword').value.trim();

    // Validación del nombre de usuario
    if (username.length < 3) {
        mensaje.textContent = 'El nombre de usuario debe tener al menos 3 caracteres.';
        return;
    }
    if (nombresProhibidos.includes(username)) {
        mensaje.textContent = 'El nombre de usuario no está disponible.';
        return;
    }

    // Validación del correo electrónico
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        mensaje.textContent = 'Ingrese una dirección de correo válida.';
        return;
    }

    // Validación de la contraseña
    if (password.length < 8) {
        mensaje.textContent = 'La contraseña debe tener al menos 8 caracteres.';
        return;
    }

    // Validación de confirmación de la contraseña
    if (password !== confirmPassword) {
        mensaje.textContent = 'Las contraseñas no coinciden.';
        return;
    }

    // Si las validaciones son correctas, se envían los datos
    enviarDatos({ username, email, password });
});

// Función para enviar los datos a la API
function enviarDatos(data) {
    fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST', // Método HTTP para enviar datos
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // Convertir los datos en formato JSON
    })
    .then(response => response.json())
    .then(data => {
        mensaje.textContent = 'Registro exitoso.';
        mensaje.classList.add('success');
    })
    .catch(error => {
        mensaje.textContent = 'Ocurrió un error durante el envío de datos.';
        console.error('Error:', error);
    });
}
