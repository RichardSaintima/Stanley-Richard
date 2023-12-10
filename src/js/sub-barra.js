(function() {
    document.addEventListener('scroll', function() {
        var scrollPosition = window.scrollY;

        var barraPrincipal = document.getElementById('nav');
        var barraPortafolio = document.getElementById('nav-portafolio');
        var barraSobreMi = document.getElementById('nav-sobremi');
        var barraHobby = document.getElementById('nav-hobby');
        var barraContacto = document.getElementById('nav-contacto');
        var barraPrincipalHeight = barraPrincipal.offsetHeight;

        var portafolioSection = document.getElementById('portafolio');
        var sobreMiSection = document.getElementById('sobre-mi');
        var hobbySection = document.getElementById('hobby');
        var contactoSection = document.getElementById('contacto');
        var portafolioSectionPosition = portafolioSection.offsetTop;
        var sobreMiSectionPosition = sobreMiSection.offsetTop;
        var hobbySectionPosition = hobbySection.offsetTop;
        var contactoSectionPosition = contactoSection.offsetTop;

        if (
            scrollPosition >= portafolioSectionPosition - barraPrincipalHeight &&
            scrollPosition < sobreMiSectionPosition - barraPrincipalHeight
        ) {
            barraPortafolio.style.display = 'block';
            barraSobreMi.style.display = 'none';
            barraHobby.style.display = 'none';
            barraContacto.style.display = 'none';
        } else if (
            scrollPosition >= sobreMiSectionPosition - barraPrincipalHeight &&
            scrollPosition < hobbySectionPosition - barraPrincipalHeight
        ) {
            barraPortafolio.style.display = 'none';
            barraSobreMi.style.display = 'block';
            barraHobby.style.display = 'none';
            barraContacto.style.display = 'none';
        } else if (
            scrollPosition >= hobbySectionPosition - barraPrincipalHeight &&
            scrollPosition < contactoSectionPosition - barraPrincipalHeight
        ) {
            barraPortafolio.style.display = 'none';
            barraSobreMi.style.display = 'none';
            barraHobby.style.display = 'block';
            barraContacto.style.display = 'none';
        } else if (scrollPosition >= contactoSectionPosition - barraPrincipalHeight) {
            barraPortafolio.style.display = 'none';
            barraSobreMi.style.display = 'none';
            barraHobby.style.display = 'none';
            barraContacto.style.display = 'block';
        } else {
            barraPortafolio.style.display = 'none';
            barraSobreMi.style.display = 'none';
            barraHobby.style.display = 'none';
            barraContacto.style.display = 'none';
        }
    });
})();
