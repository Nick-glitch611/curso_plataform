from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash

conexao = sqlite3.connect("curso_plataform/database.db")
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

    return render_template("auth/login.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        usuario = request.form["usuario"]
        email = request.form["email"]
        senha1 = generate_password_hash(request.form["senha1"])
        senha2 = generate_password_hash(request.form["senha2"])

        if senha1 == senha2:
            db.execute("""
                INSERT INTO dados (usuario, senha, email)
                VALUES (?, ?, ?)
            """, (usuario, email, senha1))

    return render_template("auth/cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)