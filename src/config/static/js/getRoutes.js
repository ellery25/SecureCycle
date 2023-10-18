// Función para obtener y mostrar las rutas
function getAndDisplayRoutes() {
    fetch('/routes/getRoute')  // Reemplaza la URL con la ruta correcta de tu API
        .then(response => response.json())
        .then(routes => {
            const routeListContainer = document.getElementById('route-list-container');

            routes.forEach(route => {
                // Crea un elemento de lista (list item) para cada ruta
                const listItem = document.createElement('a');
                listItem.className = 'list-group-item list-group-item-action';

                // Aplica el estilo CSS para el salto de línea
                listItem.style.wordWrap = 'break-word';

                // Contenido del elemento de lista
                listItem.innerHTML = `
                    <div class="d-flex w-100 justify-content-between">
                        <h5 class="mb-1">${route.title}</h5>
                        <small>${new Date(route.creationDate).toDateString()}</small>
                    </div>
                    <p class="mb-1">Descripción: ${route.description}</p>
                    <p class="mb-1">Ubicación Inicial: ${route.initialLocation}</p>
                    <p class="mb-1">Ubicación Final: ${route.finalLocation}</p>
                    <small class="text-body-secondary">Usuario: ${route.user_id}</small>
                `;

                // Agrega el elemento de lista al contenedor de lista
                routeListContainer.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error al obtener rutas:', error);
        });
}

// Llama a la función para cargar las rutas cuando la página esté lista
document.addEventListener('DOMContentLoaded', function () {
    getAndDisplayRoutes();
});