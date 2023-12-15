import Swal from 'sweetalert2';

function handleClick(event) {
    const aptitudId = event.target.dataset.aptitudId;
    document.getElementById('nombre').value = event.target.innerText;
    document.getElementById('aptitud_id').value = aptitudId;
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
            const aptitudId = event.target.dataset.aptitudId;
            eliminarAptitud(aptitudId, event.target);
        }
    });
}

function eliminarAptitud(aptitudId, elemento) {
    fetch('/dashboard/eliminar_aptitud/' + aptitudId, {
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
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (const element of cookies) {
            const cookie = element.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

(function() {
    const items = document.querySelectorAll('#tags li');

    for (const element of items) {
        element.addEventListener('click', handleClick);
        element.addEventListener('dblclick', handleDoubleClick);
    }
})();
