// Variables iniciales
let turnoActual = 'X';
let tablero = ["", "", "", "", "", "", "", "", ""];
let juegoActivo = true;
const combinacionesGanadoras = [
    [0, 1, 2], // Fila 1
    [3, 4, 5], // Fila 2
    [6, 7, 8], // Fila 3
    [0, 3, 6], // Columna 1
    [1, 4, 7], // Columna 2
    [2, 5, 8], // Columna 3
    [0, 4, 8], // Diagonal
    [2, 4, 6]  // Diagonal
];

// Elementos HTML
const casillas = document.querySelectorAll('.casilla');
const mensajeTurno = document.getElementById('turnoActual');
const reiniciarBtn = document.getElementById('reiniciarBtn');

// Manejar clic en las casillas
casillas.forEach(casilla => {
    casilla.addEventListener('click', (e) => {
        const index = e.target.getAttribute('data-index');
        
        // Si la casilla ya está ocupada o el juego terminó, no hacer nada
        if (tablero[index] !== "" || !juegoActivo) return;

        // Actualizar el tablero
        tablero[index] = turnoActual;
        e.target.textContent = turnoActual;

        // Verificar si hay un ganador o empate
        verificarResultado();

        // Alternar turno
        turnoActual = turnoActual === 'X' ? 'O' : 'X';
        mensajeTurno.textContent = `Turno del jugador: ${turnoActual}`;
    });
});

// Función para verificar si hay un ganador o empate
function verificarResultado() {
    let rondaGanada = false;

    // Comprobar todas las combinaciones ganadoras
    for (let combinacion of combinacionesGanadoras) {
        const [a, b, c] = combinacion;
        if (tablero[a] && tablero[a] === tablero[b] && tablero[a] === tablero[c]) {
            rondaGanada = true;
            break;
        }
    }

    if (rondaGanada) {
        mensajeTurno.textContent = `¡El jugador ${turnoActual} ha ganado!`;
        juegoActivo = false;
        return;
    }

    // Comprobar si hay un empate (tablero completo sin ganador)
    if (!tablero.includes("")) {
        mensajeTurno.textContent = '¡Empate!';
        juegoActivo = false;
        return;
    }
}

// Reiniciar el juego
reiniciarBtn.addEventListener('click', () => {
    tablero = ["", "", "", "", "", "", "", "", ""];
    juegoActivo = true;
    turnoActual = 'X';
    mensajeTurno.textContent = `Turno del jugador: ${turnoActual}`;
    casillas.forEach(casilla => casilla.textContent = "");
});
