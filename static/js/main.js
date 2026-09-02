const cadastro = document.getElementById("cadastro");

cadastro.addEventListener("submit", function(prevenir) {
    const senha1 = document.querySelector('input[name="senha1"]').value;
    const senha2 = document.querySelector('input[name="senha2"]').value;

    if (senha1 !== senha2) {
        prevenir.preventDefault();
        alert("As senhas devem ser iguais");
    }
});

const login = document.getElementById("login")

login.addEventListener("submit", async function(existente) {
    existente.preventDefault();

    const usuario = document.querySelector('input[name="usuario"]')

    const resultado = await resposta.json();

    if (resultado.existe) {
        alert("Usuário existe!");
    } else {
        alert("Usuário não existe!");
    }

    if (usuario)
});