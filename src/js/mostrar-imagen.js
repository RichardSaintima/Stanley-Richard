(function() {
    window.mostrarImagen = function(input) {
        let imagenSeleccionada = document.querySelector('.imagenSeleccionada');
        imagenSeleccionada.innerHTML = '';
    
        if (input.files && input.files[0]) {
            let reader = new FileReader();
    
            reader.onload = function(e) {
                let imagen = document.createElement('img');
                imagen.src = e.target.result;
                imagen.style.maxWidth = '100%';
                imagenSeleccionada.appendChild(imagen);
            };
    
            reader.readAsDataURL(input.files[0]);
        }
    }
})();
