(function(){
    
    const barra = document.querySelector('.header__mobile');
    const barraIcon = document.querySelector('.header__mobile i');
    const barraMenu = document.querySelector('.menu--mobile');

    barra.onclick = function() {
        barraMenu.classList.toggle('abrirMenu');

        const isopen = barraMenu.classList.contains('abrirMenu');
        barraIcon.classList = isopen 
            ? 'fas fa-xmark' 
            : 'fas fa-bars';
    }
})();