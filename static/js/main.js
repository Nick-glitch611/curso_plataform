const cadastro = document.getElementById("cadastro");

if (cadastro != null) {
    cadastro.addEventListener("submit", function(prevenir) {
        const senha1 = document.querySelector('input[name="senha1"]').value;
        const senha2 = document.querySelector('input[name="senha2"]').value;

        if (senha1 !== senha2) {
            prevenir.preventDefault();
            alert("As senhas devem ser iguais");
        }
    });
}

const login = document.getElementById("login");

if (login != null) {

    login.addEventListener("submit", async function(event) {

        event.preventDefault();

        const usuario = document.querySelector('input[name="usuario"]').value;
        const senha = document.querySelector('input[name="senha"]').value;

        const resposta = await fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                usuario: usuario,
                senha: senha
            })
        });

        const resultado = await resposta.json();

        if (resultado.sucesso) {
            window.location.href = "/aluno";
        } else {
            alert("Usuário ou senha incorretos");
        }
    });
}