from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def RenderIndex():
    return render_template("index.html", title = "Quem sou")

# @app.route("/ExperienciasProfissionais")
# def RenderExpProfissional():
#     experiencias = []
#     with open("./src/static/dados/expProffisional.json", encoding="utf-8") as expFile:
#         experiencias = json.loads(expFile.read())["Experiencias"]
#     return render_template("ExpProfissional.html", experiencias = experiencias)

@app.route("/ProjetosAcademicos")
def RenderProjetosAcademicos():
    projetos = LoadProjetos("./src/static/dados/projetosAcademicos.json")
    return render_template("Projetos.html", title = "Projetos Academicos", periodos = projetos)

@app.route("/ProjetosPessoais")
def RenderProjetosPessoais():
    projetos = LoadProjetos("./src/static/dados/projetosPessoais.json")
    return render_template("Projetos.html", title = "Projetos Pessoais", periodos = projetos)

@app.route("/Hobbies")
def RenderHobbies():
    return render_template("Hobbies.html", title = "Hobbies")

@app.route("/Certificados")
def RenderCertificados():
    certificados = []
    with open("./src/static/dados/certificados.json", "r", encoding="utf-8") as certificadosFile:
        certificados = json.loads(certificadosFile.read())["Certificados"]
    return render_template("Certificados.html", title = "Certificados", certificados = certificados)

# @app.route("/Tecnologias")
# def RenderTecnologias():
#     tecnologias = []
#     with open("./src/static/dados/tecnologias.json", encoding="utf-8") as tecnologiasFile:
#         tecnologias = json.loads(tecnologiasFile.read())["Tecnologias"]

#     return render_template("Tecnologias.html", tecnologias = tecnologias)

def LoadProjetos(projetos):
    with open(projetos, "r", encoding="utf-8") as projetosFile:
        fileContent = projetosFile.read()
        return json.loads(fileContent)["Periodos"]

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = "5000", debug = False)
