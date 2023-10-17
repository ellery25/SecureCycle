function getAndDisplayPosts() {
  fetch("posts/getPost")
    .then((response) => response.json())
    .then((posts) => {
      const postContainer = document.getElementById("post-container");

      posts.forEach((post) => {
        // Crear elementos HTML para cada post
        const card = document.createElement("div");
        card.className = "card";

        const cardContent = document.createElement("div");
        cardContent.className = "card-content";

        const cardTitle = document.createElement("h2");
        cardTitle.textContent = post.title;
        cardTitle.className = "card-title";

        const cardUser = document.createElement("h3");
        cardUser.textContent = post.user_id;
        cardUser.className = "card_user";

        const cardDate = document.createElement("p");
        cardDate.textContent = `Publicado el: ${post.date}`;
        cardDate.className = "card-date";

        const cardContentText = document.createElement("p");
        cardContentText.textContent = post.content;
        cardContentText.className = "card-content-text";

        // Agregar elementos al DOM
        cardContent.appendChild(cardTitle);
        cardContent.appendChild(cardUser);
        cardContent.appendChild(cardDate);
        cardContent.appendChild(cardContentText);
        card.appendChild(cardContent);
        postContainer.appendChild(card);
      });

      // ...
    })
    .catch((error) => {
      console.error("Error al obtener los posts:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  getAndDisplayPosts();
});
