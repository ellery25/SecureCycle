function getUserData() {
    fetch('/usuarios/getUser', { method: 'GET' })
        .then(response => response.json())
        .then(user => {
            const userCard = document.getElementById('user-card');

            // Crear la tarjeta del usuario
            const card = document.createElement('div');
            card.className = 'card';

            // Agregar un encabezado a la tarjeta
            const cardHeader = document.createElement('div');
            cardHeader.className = 'card-header';
            cardHeader.textContent = 'Datos del Usuario';
            card.appendChild(cardHeader);

            // Crear el contenido de la tarjeta
            const cardBody = document.createElement('div');
            cardBody.className = 'card-body';

            // Mostrar los datos del usuario
            cardBody.innerHTML = `
                <h5 class="card-title">${user.name}</h5>
                <p class="card-text">Usuario: ${user.user}</p>
                <p class="card-text">Correo Electrónico: ${user.email}</p>
            `;

            card.appendChild(cardBody);

            // Agregar la tarjeta al contenedor
            userCard.appendChild(card);
        })
        .catch(error => {
            console.error('Error al obtener datos del usuario:', error);
        });
}

document.addEventListener('DOMContentLoaded', function() {
    getUserData();
});
