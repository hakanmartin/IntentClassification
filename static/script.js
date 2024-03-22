function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    var chatOutput = document.getElementById("chat-output");

    // Kullanıcının mesajını gönder
    chatOutput.innerHTML += "<p><strong>You:</strong> " + userInput + "</p>";

    // Burada kullanıcı mesajına göre cevap üretmek için Python kodunuzu çağırabilirsiniz.
    // Örneğin, bir Ajax isteği kullanarak sunucu tarafında çalışan bir Python kodunu çağırabilirsiniz.

    // Cevabı ekrana yazdır (örneğin, sunucudan alınan veri)
    // chatOutput.innerHTML += "<p><strong>Chatbot:</strong> " + response + "</p>";

    // Kullanıcı mesajı gönderildikten sonra giriş alanını temizle
    document.getElementById("user-input").value = "";

    // Chat penceresini en altta tut
    chatOutput.scrollTop = chatOutput.scrollHeight;
}