window.onload = function () {
    let projetos = document.getElementById("proj-academicos").children;
    projetos[0].children[0].style.display = "block";
    projetos[0].children[1].style.display = "none";
    for(let i = 1; i < projetos.length; i++)
        projetos[i].style.display = "none";
    
    projetos = document.getElementById("proj-pessoais").children;
    projetos[0].children[0].style.display = "none";
    projetos[0].children[1].style.display = "block";
    for(let i=1; i < projetos.length; i++)
        projetos[i].style.display = "flex";
};

document.getElementById("proj-academicos-btn").addEventListener("click", function() { AbreFecha(this, document.getElementById("proj-academicos").children); });
document.getElementById("proj-pessoais-btn").addEventListener("click", function() { AbreFecha(this, document.getElementById("proj-pessoais").children); });

function AbreFecha(btn, projetos){
    for(let i = 0; i < 2; i++){
        if(btn.children[i].style.display == "block")
            btn.children[i].style.display = "none";
        else btn.children[i].style.display = "block";
    }
    
    for(let i = 1; i < projetos.length; i++){
        if(projetos[i].style.display == "flex")
            projetos[i].style.display = "none";
        else projetos[i].style.display = "flex";
    }
}