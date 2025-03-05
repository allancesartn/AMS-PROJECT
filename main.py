from flask import Flask, url_for, render_template

# inicialização
app = Flask(__name__)

# rotas


@app.route('/')
def home_page():
    titulo = "Agro Market Service"
    usuarios = [
        {"nome": "Allan", "membro_ativo": True},
        {"nome": "João Paulo", "membro_ativo": False},
        {"nome": "Wesley", "membro_ativo": True},
        {"nome": "Marcuzim", "membro_ativo": False},
    ]

    return render_template("index.html", titulo=titulo, usuarios=usuarios)


@app.route('/cadastro')
def cadastro_cliente():
    return """
        <b>Ams - Agro Market Service</b>
        <a href="https://www.deere.com.br/pt/>John Deere</a>
    """


# execução
app.run(debug=True)
