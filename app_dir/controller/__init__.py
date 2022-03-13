from ast import arg
from app_dir import app
from flask import render_template, request


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/resultado")
def contatos():
    search = request.args.get("search")
    return render_template("resultado.html",search=search)
    
@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")