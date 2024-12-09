document.addEventListener("DOMContentLoaded", function () {
    // Selecciona todos los comentarios
    const comentarios = document.querySelectorAll(".comment-box");

    comentarios.forEach((comentario) => {
        // Encuentra la puntuación dentro del texto del comentario
        const puntuacionText = comentario.querySelector("p").textContent;
        const puntuacionMatch = puntuacionText.match(/(\d)\/5/);

        if (puntuacionMatch) {
            const puntuacion = parseInt(puntuacionMatch[1]);

            // Cambia el color de fondo según la puntuación
            if (puntuacion >= 4) {
                comentario.style.backgroundColor = "lightgreen"; // Verde
            } else if (puntuacion === 3) {
                comentario.style.backgroundColor = "orange"; // Naranja
            } else if (puntuacion <= 2) {
                comentario.style.backgroundColor = "lightcoral"; // Rojo
            }
        }
    });
});
