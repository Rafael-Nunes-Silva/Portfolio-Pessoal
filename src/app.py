from flask import Flask, render_template
import json

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route("/")
def renderIndex():
    certificados = []
    with open("./static/dados/certificados.json", encoding="utf-8") as certificadosFile:
        certificados = json.loads(certificadosFile.read())["Certificados"]
    return render_template("index.html", certificados = certificados)

@app.route("/Trabalhos")
def renderTrabalhos():
    trabalhos = []
    with open("./static/dados/trabalhos.json", encoding="utf-8") as trabalhosFile:
        trabalhos = json.loads(trabalhosFile.read())["Trabalhos"]
    return render_template("Trabalhos.html", trabalhos = trabalhos)

@app.route("/Projetos")
def renderProjetos():
    projetosAcademicos, projetosPessoais = [], []
    with open("./static/dados/projetos.json", encoding="utf-8") as projetosFile:
        fileContent = projetosFile.read()
        projetosAcademicos = json.loads(fileContent)["ProjetosAcademicos"]
        projetosPessoais = json.loads(fileContent)["ProjetosPessoais"]

    return render_template("Projetos.html", projetosAcademicos = projetosAcademicos, projetosPessoais = projetosPessoais)

@app.route("/Hobbies")
def renderHobbies():
    return render_template("Hobbies.html")

@app.route("/Tecnologias")
def renderTecnologias():
    tecnologias = []
    with open("./static/dados/tecnologias.json", encoding="utf-8") as tecnologiasFile:
        tecnologias = json.loads(tecnologiasFile.read())["Tecnologias"]

    return render_template("Tecnologias.html", tecnologias = tecnologias)