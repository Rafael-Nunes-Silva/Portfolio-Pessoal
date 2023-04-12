from flask import Flask, render_template

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route("/")
def renderIndex():
    return render_template("index.html")

@app.route("/Trabalhos")
def renderTrabalhos():
    return render_template("Trabalhos.html")

@app.route("/Projetos")
def renderProjetos():
    return render_template("Projetos.html")

@app.route("/Hobbies")
def renderHobbies():
    return render_template("Hobbies.html")

@app.route("/Tecnologias")
def renderTecnologias():
    return render_template("Tecnologias.html")