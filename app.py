from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash
import os

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho = os.path.join(diretorio, "database.db")
conexao = sqlite3.connect(caminho)
db = conexao.cursor()

db.execute("""
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
""")

conexao.commit()
conexao.close()

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = generate_password_hash(request.form["senha"])

    usuario_existe = db.execute(" SELECT * FROM dados WHERE usuario = ? ", (usuario,)).fetchone()

    if not usuario_existe:
        render_template("auth/login.html", erro=True)

    else:
        senha_correta = db.execute(" SELECT senha FROM DADOS WHERE usuario = ?", (usuario,)).fetchone()

        if senha_correta:
            aluno()
        
        else:
            render_template("auth/login.html", erro=True)


    return render_template("auth/login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        usuario = request.form["usuario"]
        email = request.form["email"]
        senha1 = request.form["senha1"]
        senha2 = request.form["senha2"]

        if senha1 != senha2:
            return render_template("auth/cadastro.html", erro=True)

        senha1 = generate_password_hash(request.form["senha1"])

        conexao = sqlite3.connect(caminho)
        db = conexao.cursor()

        db.execute("""
            INSERT INTO dados (usuario, senha, email)
            VALUES (?, ?, ?)
        """, (usuario, email, senha1))

        conexao.commit()
        conexao.close()
        

    return render_template("auth/cadastro.html")

@app.route("/aluno")
def aluno():
    render_template("auth/perfil.html")

if __name__ == "__main__":
    app.run(debug=True)