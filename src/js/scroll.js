(function() {
    const enlacesNavegacion = document.querySelectorAll('.hacerCroll');
    const secciones = Array.from(enlacesNavegacion).map(enlace => {
        const destino = enlace.getAttribute('href');
        return document.querySelector(destino);
    });

    function actualizarEstado() {
        const scrollPosition = window.scrollY;

        secciones.forEach((seccion, index) => {
            const barraEnlace = enlacesNavegacion[index];
            const barraPrincipalHeight = document.getElementById('nav').offsetHeight;

            if (seccion) {
                const seccionPosition = seccion.offsetTop;
                const seccionHeight = seccion.offsetHeight;

                if (scrollPosition >= seccionPosition - barraPrincipalHeight && scrollPosition < seccionPosition + seccionHeight - barraPrincipalHeight) {
                    barraEnlace.classList.add('active');
                } else {
                    barraEnlace.classList.remove('active');
                }
            }
        });

        const seccionVisible = document.querySelector('.hacerCroll.active');
        const nuevoTitulo = seccionVisible ? seccionVisible.textContent : 'Inicio';
        document.title = nuevoTitulo;
    }

    enlacesNavegacion.forEach(enlace => {
        enlace.addEventListener('click', function(e) {
            e.preventDefault();
            const destino = this.getAttribute('href');
            const seccionDestino = document.querySelector(destino);

            if (seccionDestino) {
                window.scrollTo({
                    top: seccionDestino.offsetTop - 20,
                    behavior: 'smooth'
                });
            }
        });
    });

    document.addEventListener('scroll', actualizarEstado);
    window.addEventListener('resize', actualizarEstado);

    actualizarEstado();
})();
