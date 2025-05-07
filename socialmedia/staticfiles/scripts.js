const items = document.querySelector(".menu-items");
const profile = document.getElementById('profile');
const dropdown = document.getElementById('dropdown-menu');

items.addEventListener('click', () => {
  dropdown.classList.toggle('hidden');
});
profile.addEventListener('click', () => {
    dropdown.classList.toggle('hidden');
});     



const likeButtons = document.querySelectorAll(".like-button");
const likes = document.querySelectorAll(".likes");

likeButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        let postId = button.getAttribute("data-value");

        fetch(`/post/${postId}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                let currentText = event.target.textContent.trim();
            if (currentText === "Like") {
                event.target.textContent = "Liked";
            } else {
            event.target.textContent = "Like";
            }
            let likeCountElement = event.target.closest('.post').querySelector('.likes');
            
            let currentLikeCount = parseInt(likeCountElement.textContent.trim());

            if (currentText === "Like") {
                likeCountElement.textContent = currentLikeCount + 1;
            } else {
                likeCountElement.textContent = currentLikeCount - 1;
            }
            } else {
                console.error("Failed to like the post.");
            }
        })
        .catch((error) => console.error("Error:", error));
    });
});


const likeButtonOne = document.querySelectorAll(".like-buttonOne");

likeButtonOne.forEach((button) => {
    button.addEventListener("click", (event) => {
        let title = button.getAttribute("data-value");
        fetch(`/like_post/${title}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
        })
        .then((response) => response.json())
        .then((data) => {
            if (data.success) {
                let currentText = button.textContent.trim();
                if (currentText === "Like") {
                    button.textContent = "Liked";
                } else {
                    button.textContent = "Like";
                }

                let likeCountElement = button.closest(".posts").querySelector(".liked");
                let currentLikeCount = parseInt(likeCountElement.textContent.trim());

                if (currentText === "Like") {
                    likeCountElement.textContent = currentLikeCount + 1;
                } else {
                    likeCountElement.textContent = currentLikeCount - 1;
                }
            } else {
                console.error("Failed to like the post.");
            }
        })
        .catch((error) => console.error("Error:", error));
    });
});



document.addEventListener("DOMContentLoaded", function () {
    const imageInput = document.querySelector("#id_image");
    const preview = document.getElementById("imagePreview");

    if (imageInput) {
      imageInput.addEventListener("change", function (event) {
        const file = event.target.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = function (e) {
            preview.src = e.target.result;
            preview.style.display = "block";
          };
          reader.readAsDataURL(file);
        } else {
          preview.src = "#";
          preview.style.display = "none";
        }
      });
    }
  });



  const chatSocket = new WebSocket("ws://" + window.location.host + "/");
  chatSocket.onopen = function (e) {
    console.log("The connection was setup successfully !");
  };
  chatSocket.onclose = function (e) {
    console.log("Something unexpected happened !");
  };
  document.querySelector("#id_message_send_input").focus();
  document.querySelector("#id_message_send_input").onkeyup = function (e) {
    if (e.keyCode == 13) {
      document.querySelector("#id_message_send_button").click();
    }
  };
  document.querySelector("#id_message_send_button").onclick = function (e) {
    var messageInput = document.querySelector(
      "#id_message_send_input"
    ).value;
    chatSocket.send(JSON.stringify({ message: messageInput, username : "{{request.user.username}}"}));
  };
  chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    var div = document.createElement("div");
    div.innerHTML = data.username + " : " + data.message;
    document.querySelector("#id_message_send_input").value = "";
    document.querySelector("#id_chat_item_container").appendChild(div);
  };