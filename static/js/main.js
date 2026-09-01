const cadastro = document.getElementById("cadastro");

cadastro.addEventListener("submit", function(prevenir) {
    const senha1 = document.querySelector('input[name="senha1"]').value;
    const senha2 = document.querySelector('input[name="senha2"]').value;

    if (senha1 !== senha2) {
        prevenir.preventDefault();
        alert("As senhas devem ser iguais");
    }
});