(function () {
    const barra = document.querySelector('.header');
    const fijaHeader = document.querySelector('.fijaHeader');
    const body = document.querySelector('body');

    window.addEventListener('scroll', function () {
        if (fijaHeader && fijaHeader.getBoundingClientRect().bottom < 0) {
            barra.classList.add('fijo');
            body.classList.add('body-scroll');
        } else {
            barra.classList.remove('fijo');
            body.classList.remove('body-scroll');
        }
    });

    const currentYearElement = document.getElementById('current-year');
    if (currentYearElement) {
        const currentYear = new Date().getFullYear();
        currentYearElement.textContent = currentYear;
    }
})();
