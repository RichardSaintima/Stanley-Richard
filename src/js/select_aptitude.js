(function() {
    document.addEventListener('DOMContentLoaded', function () {
        const checkboxes = document.querySelectorAll('input[name="aptitudes"]');
        const aptitudesSeleccionadasList = document.getElementById('aptitudes-seleccionadas-list');

        checkboxes.forEach(function (checkbox) {
            checkbox.addEventListener('change', function () {
                actualizarAptitudesSeleccionadas();
            });
        });

        function actualizarAptitudesSeleccionadas() {
            aptitudesSeleccionadasList.innerHTML = '';

            checkboxes.forEach(function (checkbox) {
                if (checkbox.checked) {
                    const aptitudNombre = checkbox.nextSibling.textContent;
                    const listItem = document.createElement('li');
                    listItem.textContent = aptitudNombre;
                    aptitudesSeleccionadasList.appendChild(listItem);
                }
            });
        }
    });

})();
