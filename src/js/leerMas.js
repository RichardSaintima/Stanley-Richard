(function() {
  var parrafos = document.querySelectorAll('.miParrafo');

  parrafos.forEach(function(parrafo) {
      var boton = parrafo.nextElementSibling;

      boton.addEventListener('click', function() {
          parrafo.classList.toggle('completo');

          if (parrafo.classList.contains('completo')) {
              this.textContent = 'Ocultar Descripcion';
          } else {
              this.textContent = 'Leer Descripcion';
          }
      });

      boton.addEventListener('touchstart', function() {
          parrafo.classList.toggle('completo');

          if (parrafo.classList.contains('completo')) {
              this.textContent = 'Ocultar Descripcion';
          } else {
              this.textContent = 'Leer Descripcion';
          }
      });
  });
})();
