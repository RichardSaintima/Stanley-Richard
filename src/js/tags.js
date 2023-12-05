import Swal from 'sweetalert2'
(function() {
    var items = document.querySelectorAll('#tags li');

    function handleClick(event) {
        var aptitudId = event.target.dataset.aptitudId;
        document.getElementById('nombre').value = event.target.innerText;
        document.getElementById('aptitud_id').value = aptitudId;
    }
    
    for (var i = 0; i < items.length; i++) {
        items[i].addEventListener('click', handleClick);
    }

    function handleDoubleClick(event) {
        Swal.fire({
            title: 'Estás seguro',
            text: '¿Quieres borrar esta aptitud?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, borrar',
            cancelButtonText: 'No, cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                var aptitudId = event.target.dataset.aptitudId;
                eliminarAptitud(aptitudId, event.target);
            }
        });
    }

    for (var i = 0; i < items.length; i++) {
        items[i].addEventListener('dblclick', handleDoubleClick);
    }

    function eliminarAptitud(aptitudId, elemento) {
        fetch('/stanley/eliminar_aptitud/' + aptitudId, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        }).then(response => response.json()).then(data => {
            if (data.success) {
                elemento.remove();
                Swal.fire(
                    '¡Eliminado!',
                    'La aptitud ha sido eliminada.',
                    'success'
                );
            } else {
                Swal.fire(
                    'Error',
                    data.error_message,
                    'error'
                );
            }
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

})();
