(function() {
    document.addEventListener('scroll', function() {
        let scrollPosition = window.scrollY;

        let barraPrincipal = document.getElementById('nav');
        let barraPortafolio = document.getElementById('nav-portafolio');
        let barraSobreMi = document.getElementById('nav-sobremi');
        let barraHobby = document.getElementById('nav-hobby');
        let barraContacto = document.getElementById('nav-contacto');
        let barraPrincipalHeight = barraPrincipal.offsetHeight;

        let portafolioSection = document.getElementById('portafolio');
        let sobreMiSection = document.getElementById('sobre-mi');
        let hobbySection = document.getElementById('hobby');
        let contactoSection = document.getElementById('contacto');
        let portafolioSectionPosition = portafolioSection.offsetTop;
        let sobreMiSectionPosition = sobreMiSection.offsetTop;
        let hobbySectionPosition = hobbySection.offsetTop;
        let contactoSectionPosition = contactoSection.offsetTop;

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
