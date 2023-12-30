var dropdown;

window.onload = function () {
    let dropdowns = document.getElementsByClassName("proj-dropdown");

    for(let i = 0; i < dropdowns.length; i++){
        dropdowns[i].children[0].children[0].addEventListener("click", function() {
            AbreFecha(dropdowns[i].children[0].children[0], dropdowns[i].children);
        });

        // dropdowns[i].children[0].children[0].children[0].style.display = (i == 0 ? "block" : "none");
        // dropdowns[i].children[0].children[0].children[1].style.display = (i == 0 ? "none" : "block");
        dropdowns[i].children[0].children[0].children[0].style.display = (i == 0 ? "none" : "block");
        dropdowns[i].children[0].children[0].children[1].style.display = (i == 0 ? "block" : "none");

        for(let j = 1; j < dropdowns[i].children.length; j++){
            dropdowns[i].children[j].style.display = (i == 0 ? "flex" : "none");
        }
    }
};

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
