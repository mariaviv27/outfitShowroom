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

// Función para oscurecer la imagen y mostrar un overlay al pasar el ratón
document.addEventListener("DOMContentLoaded", function () {
    const photo = document.getElementById("photo");
    const overlay = document.getElementById("overlay");

    if (photo && overlay) {
        photo.addEventListener("mouseover", function () {
            // Oscurece la imagen al pasar el ratón
            photo.style.filter = "brightness(50%)";
            // Muestra el overlay
            overlay.style.display = "block";
        });

        photo.addEventListener("mouseout", function () {
            // Restaura el brillo de la imagen
            photo.style.filter = "brightness(100%)";
            // Oculta el overlay
            overlay.style.display = "none";
        });
    }
});
