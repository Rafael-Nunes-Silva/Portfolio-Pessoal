window.onload = function () {
    let projetos = document.getElementById("proj-academicos").children;
    for(let i=1; i<projetos.length; i++)
        projetos[i].style.display = "flex";
    projetos = document.getElementById("proj-pessoais").children;
    for(let i=1; i<projetos.length; i++)
        projetos[i].style.display = "flex";
};

document.getElementById("proj-academicos-btn").addEventListener("click", function(event) {
    let projetos = document.getElementById("proj-academicos").children;
    for(let i=1; i<projetos.length; i++){
        if(projetos[i].style.display == "flex")
            projetos[i].style.display = "none";
        else projetos[i].style.display = "flex";
    }
});
document.getElementById("proj-pessoais-btn").addEventListener("click", function(event) {
    let projetos = document.getElementById("proj-pessoais").children;
    for(let i=1; i<projetos.length; i++){
        if(projetos[i].style.display == "flex")
            projetos[i].style.display = "none";
        else projetos[i].style.display = "flex";
    }
});