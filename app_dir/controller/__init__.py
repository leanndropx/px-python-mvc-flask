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
    