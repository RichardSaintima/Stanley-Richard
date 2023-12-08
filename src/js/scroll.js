(function(){
    document.addEventListener("DOMContentLoaded", function () {
        const enlacesNavegacion = document.querySelectorAll('.header__navegacion--enlace');

        enlacesNavegacion.forEach(function (enlace) {
            enlace.addEventListener('click', function (e) {
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
    });
})();