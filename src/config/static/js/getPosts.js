function getAndDisplayPosts() {
  fetch("posts/getPost")
    .then((response) => response.json())
    .then((posts) => {
      const postContainer = document.getElementById("post-container");

      posts.forEach((post) => {
        // Crear elementos HTML para cada post
        const card = document.createElement("div");
        card.className = "card mb-3"; // Agrega la clase 'card' y ajusta según tus necesidades

        // Contenido de la tarjeta
        card.innerHTML = `
          <div class="card-body">
            <h5 class="card-title">${post.title}</h5>
            <p class="card-text">${post.content}</p>
          </div>
          <div class="card-footer text-muted">
            Usuario: ${post.user_id} | Publicado el: ${new Date(post.date).toDateString()}
          </div>
        `;

        // Agregar elementos al DOM
        postContainer.appendChild(card);
      });
    })
    .catch((error) => {
      console.error("Error al obtener los posts:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  getAndDisplayPosts();
});
