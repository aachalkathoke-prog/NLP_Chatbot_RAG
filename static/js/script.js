// Show loading message when uploading PDF
const uploadForm = document.querySelector('form[action="/upload"]');

if (uploadForm) {
    uploadForm.addEventListener("submit", function () {
        alert("Uploading PDF... Please wait.");
    });
}

// Show loading message when asking a question
const chatForm = document.querySelector('form[action="/ask"]');

if (chatForm) {
    chatForm.addEventListener("submit", function () {

        const button = chatForm.querySelector("button");

        button.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Thinking...';

        button.disabled = true;

    });
}