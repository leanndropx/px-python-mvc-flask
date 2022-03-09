from app_dir import app
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")