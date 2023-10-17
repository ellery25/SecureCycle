function getAndDisplayAlerts() {
    fetch('alerts/getAlerts')
      .then(response => response.json())
      .then(alerts => {
        const alertCardsContainer = document.getElementById('alert-cards-container');
  
        alerts.forEach(alert => {
          // Crea una tarjeta (card) para cada alerta
          const card = document.createElement('div');
          card.className = 'col-md-4 mb-3'; // Clases de Bootstrap, ajusta según tus estilos
  
          // Contenido de la tarjeta
          card.innerHTML = `
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">${alert.type}</h5>
                <h6 class="card-subtitle mb-2 text-muted">Usuario: ${alert.user_id}</h6>
                <p class="card-text">${alert.description}</p>
                <p class="card-text">Fecha: ${alert.date}</p>
              </div>
            </div>
          `;
  
          // Agrega la tarjeta al contenedor
          alertCardsContainer.appendChild(card);
        });
      })
      .catch(error => {
        console.error('Error al obtener alertas:', error);
      });
  }

  document.addEventListener("DOMContentLoaded", function () {
    getAndDisplayAlerts();
  });
  