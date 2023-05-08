from flask import Flask, render_template
import json
import html

app = Flask(__name__, static_folder="./static", template_folder="./templates")

@app.route("/")
def renderIndex():
    return render_template("index.html")

@app.route("/Trabalhos")
def renderTrabalhos():
    return render_template("Trabalhos.html")

@app.route("/Projetos")
def renderProjetos():
    # projetos = ""
    # with open("./projetos.json") as projetosFile:
    #     projetos = json.loads(projetosFile.read())["Projetos"]

    # projetos[-1]["texto"] = projetos[-1]["texto"].encode("utf_8").decode("utf_8")
    projetos = 0
    with open("./projetos.json") as projetosFile:
        projetos = json.loads(projetosFile.read().encode("latin_1").decode("utf_8"))["Projetos"]

    return render_template("Projetos.html", projetos = projetos)

@app.route("/Hobbies")
def renderHobbies():
    return render_template("Hobbies.html")

@app.route("/Tecnologias")
def renderTecnologias():
    return render_template("Tecnologias.html")