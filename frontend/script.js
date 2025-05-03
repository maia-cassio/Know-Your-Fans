document.getElementById('fan-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = document.getElementById('fan-form');
    const formData = new FormData(form);

    const response = await fetch('http://localhost:8000/api/fan', {
        method: 'POST',
        body: formData
    });

    const statusMsg = document.getElementById('status-msg');
    if (response.ok) {
        statusMsg.textContent = "Dados enviados com sucesso!";
        form.reset();
    } else {
        statusMsg.textContent = "Erro ao enviar os dados.";
    }
});

// Define o volume da música de fundo (30%)
document.getElementById("bg-music").volume = 0.3;
