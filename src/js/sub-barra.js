(function(){
    document.addEventListener('scroll', function() {
        // Obtén la posición actual del usuario en la página
        var scrollPosition = window.scrollY;
    
        // Obtén la altura de las barras de navegación
        var barraPrincipal = document.getElementById('nav');
        var barraPortafolio = document.getElementById('nav-portafolio');
        var barraPrincipalHeight = barraPrincipal.offsetHeight;
        var barraPortafolioHeight = barraPortafolio.offsetHeight;
    
        // Obtén la posición del elemento "Portafolio" en la página
        var portafolioSection = document.getElementById('portafolio');
        var portafolioSectionPosition = portafolioSection.offsetTop;
    
        // Compara la posición del usuario y la posición del elemento "Portafolio"
        if (scrollPosition >= portafolioSectionPosition - barraPrincipalHeight) {
            // Si el usuario ha alcanzado la sección "Portafolio", muestra ambas barras de navegación
            barraPrincipal.style.display = 'none';
            barraPortafolio.style.display = 'block';
        } else {
            // Si el usuario está en otras secciones, muestra solo la barra principal
            barraPrincipal.style.display = 'block';
            barraPortafolio.style.display = 'none';
        }
    });
    
})();