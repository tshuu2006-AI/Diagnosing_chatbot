const rasaURL = "http://localhost:5005/webhooks/rest/webhook"; // URL REST API của Rasa

function sendMessage() {
  const userInput = document.getElementById("user-input").value;
  if (!userInput) return;

  // Hiển thị tin nhắn người dùng
  appendMessage("Bạn", userInput);

  // Gửi tin nhắn đến Rasa
  fetch(rasaURL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sender: "user", message: userInput }),
  })
    .then(response => response.json())
    .then(data => {
      data.forEach(reply => appendMessage("Bot", reply.text));
    })
    .catch(err => console.error("Error:", err));

  // Xóa nội dung input
  document.getElementById("user-input").value = "";
}

function appendMessage(sender, message) {
  const chatBody = document.getElementById("chat-body");
  const messageElement = document.createElement("div");
  messageElement.textContent = `${sender}: ${message}`;
  chatBody.appendChild(messageElement);
  chatBody.scrollTop = chatBody.scrollHeight; // Tự động cuộn xuống
}
