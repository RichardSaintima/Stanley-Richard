(function() {
    document.addEventListener('scroll', function() {
        var scrollPosition = window.scrollY;

        var barraPrincipal = document.getElementById('nav');
        var barraPortafolio = document.getElementById('nav-portafolio');
        var barraSobreMi = document.getElementById('nav-sobremi');
        var barraPrincipalHeight = barraPrincipal.offsetHeight;
        
        var portafolioSection = document.getElementById('portafolio');
        var sobreMiSection = document.getElementById('sobre-mi');
        var portafolioSectionPosition = portafolioSection.offsetTop;
        var sobreMiSectionPosition = sobreMiSection.offsetTop;

        if (scrollPosition >= portafolioSectionPosition - barraPrincipalHeight &&
            scrollPosition < sobreMiSectionPosition - barraPrincipalHeight) {
                
            barraPortafolio.style.display = 'block';
            barraSobreMi.style.display = 'none';
        } else if (scrollPosition >= sobreMiSectionPosition - barraPrincipalHeight) {
            
            barraPortafolio.style.display = 'none';
            barraSobreMi.style.display = 'block';
        } else {

            barraPortafolio.style.display = 'none';
            barraSobreMi.style.display = 'none';
        }
    });
})();
