function getAndDisplayAlerts() {
  fetch('alerts/getAlerts')
    .then(response => response.json())
    .then(alerts => {
      const alertListContainer = document.getElementById('alert-list-container');

      alerts.forEach(alert => {
        // Crea un elemento de lista (list item) para cada alerta
        const listItem = document.createElement('a');
        listItem.className = 'list-group-item list-group-item-action';

        // Aplica el estilo CSS para el salto de línea
        listItem.style.wordWrap = 'break-word';

        // Contenido del elemento de lista
        listItem.innerHTML = `
          <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1">${alert.type}</h5>
            <small>${new Date(alert.date).toDateString()}</small>
          </div>
          <p class="mb-1">${alert.description}</p>
          <small class="text-body-secondary">Usuario: ${alert.user_id}</small>
          <small class="text-body-secondary">|| Dirección: ${alert.direction}</small>
        `;

        // Agrega el elemento de lista al contenedor de lista
        alertListContainer.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('Error al obtener alertas:', error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  getAndDisplayAlerts();
});
