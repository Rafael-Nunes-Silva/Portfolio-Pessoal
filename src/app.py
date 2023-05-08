from flask import Flask, render_template
import json

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route("/")
def renderIndex():
    certificados = []
    with open("./static/dados/certificados.json") as certificadosFile:
        certificados = json.loads(certificadosFile.read().encode("latin_1").decode("utf_8"))["Certificados"]
    return render_template("index.html", certificados = certificados)

@app.route("/Trabalhos")
def renderTrabalhos():
    return render_template("Trabalhos.html")

@app.route("/Projetos")
def renderProjetos():
    projetos = []
    with open("./static/dados/projetos.json") as projetosFile:
        projetos = json.loads(projetosFile.read().encode("latin_1").decode("utf_8"))["Projetos"]

    return render_template("Projetos.html", projetos = projetos)

@app.route("/Hobbies")
def renderHobbies():
    return render_template("Hobbies.html")

@app.route("/Tecnologias")
def renderTecnologias():
    tecnologias = []
    with open("./static/dados/tecnologias.json") as tecnologiasFile:
        tecnologias = json.loads(tecnologiasFile.read().encode("latin_1").decode("utf_8"))["Tecnologias"]

    return render_template("Tecnologias.html", tecnologias = tecnologias)