from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def RenderIndex():
    certificados = []
    with open("./static/dados/certificados.json", encoding="utf-8") as certificadosFile:
        certificados = json.loads(certificadosFile.read())["Certificados"]
    return render_template("index.html", certificados = certificados)

@app.route("/ExperienciaProfissional")
def RenderExpProfissional():
    experiencias = []
    with open("./static/dados/expProffisional.json", encoding="utf-8") as expFile:
        experiencias = json.loads(expFile.read())["Experiencias"]
    return render_template("ExpProfissional.html", experiencias = experiencias)

@app.route("/ProjetosAcademicos")
def RenderProjetosAcademicos():
    projetos = LoadProjetos("./static/dados/projetosAcademicos.json")
    return render_template("Projetos.html", periodos = projetos)

@app.route("/ProjetosPessoais")
def RenderProjetosPessoais():
    projetos = LoadProjetos("./static/dados/projetosPessoais.json")
    return render_template("Projetos.html", periodos = projetos)

@app.route("/Hobbies")
def RenderHobbies():
    return render_template("Hobbies.html")

@app.route("/Tecnologias")
def RenderTecnologias():
    tecnologias = []
    with open("./static/dados/tecnologias.json", encoding="utf-8") as tecnologiasFile:
        tecnologias = json.loads(tecnologiasFile.read())["Tecnologias"]

    return render_template("Tecnologias.html", tecnologias = tecnologias)

def LoadProjetos(projetos):
    with open(projetos, encoding="utf-8") as projetosFile:
        fileContent = projetosFile.read()
        return json.loads(fileContent)["Periodos"]
