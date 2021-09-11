/*##################   border des images   #################*/
var div = document.getElementById("placeimg");
var img = document.createElement("img");
var lim = 5
var i = 1

/*#########################  pour animation de border images  ##################*/

setInterval(function() {
    img.src = "/static/images/mvt/bord" + i + ".png";
    img.setAttribute("style", "width:101.4%; height:15%; display:block;position:relative;left:-10px;")
    div.appendChild(img)
    i++
    if (i === lim) {
        i = 1
    }
}, 2500)


/* produit */
function bla(x) {
    x.style.opacity = "1"
}

function bla2(x) {
    x.style.opacity = "0"
}
/*#######################  achat   ################################*/
const btnmoin = document.querySelector("#moin")
const btnplus = document.querySelector("#plus")
const nbr = document.querySelector("#nbr")
const nom = document.getElementById("name")
const adre = document.getElementById("adr")
const ville = document.getElementById("city")
const tele = document.getElementById("numerotele")
var total = 1

btnmoin.onclick = () => {
    if (total > 1) {
        total = total - 1
        nbr.value = total
    }
}

btnplus.onclick = () => {
    if (total < 9) {
        total = total + 1
        nbr.value = total
    }
}

/*####################   check type of variable   ########################3*/

nom.addEventListener("input", () => {
    if (nom.value === "" || isNaN(nom.value) !== true) {
        nom.style.border = "solid red"
    } else {
        nom.style.border = "solid green"
    }
})

adre.addEventListener("input", () => {
    if (adre.value === "") {
        adre.style.border = "solid red"
    }
})

ville.addEventListener("input", () => {
    if (ville.value === "" || isNaN(ville.value) !== true) {
        ville.style.border = "solid red"
    } else {
        ville.style.border = "solid green"
    }
})


tele.addEventListener('input', () => {
    if (tele.value === "" || isNaN(tele.value) === true || tele.value.length !== 10) {
        tele.style.border = "solid red"
    } else {
        tele.style.border = "solid green"
    }
})

/*################## button of search  #########################*/
//const prouct = [{ name: "business" }, { name: "dax" }, { name: "arctic" }];
/*
const search = document.querySelector("#search");
search.addEventListener('input', () => {
    console.log('idk if it work')
}
*/
document.getElementById("search").onchange = () => {
    console.log('idk if it work')
}

function openPage() {

    var search = document.querySelector("#search").value;
    var inputsearch = search.toLowerCase();
    console.log(inputsearch);

    if (inputsearch === "business") {
        window.open("/nosproduit/recherche/business");
    }

    if (inputsearch === "dax") {
        window.open("/nosproduit/recherche/dax");
    }

    if (inputsearch === "business sac" || inputsearch === "business sac a dos de voyage") {
        window.open("/nosproduit/BUSINESS-SAC-À-DOS-DE-VOYAGE");
    }

    if (inputsearch === "dax 3d" || inputsearch === "dax 3d the hunter sac a dos") {
        window.open("/nosproduit/DAX-3D-THE-HUNTER-SAC-À-DOS");
    }

    if (inputsearch === "arctic" || inputsearch === "arctic hunter sac a dos multifunction") {
        window.open("/nosproduit/ARCTIC-HUNTER-SAC-A-DOS-MULTI-FONCTION");
    }

    if (inputsearch === "foldable" || inputsearch === "foldable smart" || inputsearch === "foldable smart sac a dos voyage et business ") {
        window.open("/nosproduit/FOLDABLE-SMART-SAC-À-DOS-VOYAGE-&-BUSINESS")
    }

    if (inputsearch === "last" || inputsearch === "last hunter" || inputsearch === "last hunter sac a dos") {
        window.open("/nosproduit/last-hunter-sac-a-dos")
    }

    if (inputsearch === "chest" || inputsearch === "chest & back sac pour sortie" || inputsearch === "chest & back") {
        window.open("/nosproduit/CHEST-&-BACK-SAC-POUR-SORTIE")
    }

    if (inputsearch === "business sac a dos" || inputsearch === "business sac a dos smart laptop convertible") {
        window.open("/nosproduit/BUSINESS-SAC-À-DOS-SMART-LAPTOP-CONVERTIBLE")
    }

    if (inputsearch === "fashion" || inputsearch === "fashion style backpackfashion style backpack") {
        window.open("/nosproduit/FASHION-STYLE-BACKPACKFASHION-STYLE-BACKPACK")
    }

    if (inputsearch === "heweltt" || inputsearch === "hewlett backpack") {
        window.open("/nosproduit/HEWLETT-BACKPACK")
    }

    if (inputsearch === "matt" || inputsearch === "matt flat sac a dos") {
        window.open("/nosproduit/MATT-FLAT-SAC-À-DOS")
    }

    if (search === "dax teenagers" || search === "dax teenagers ecole backpack") {
        window.open("/nosproduit/DAX-TEENAGERS-ECOLE-BACKPACK")
    } else {
        document.getElementById("no_found").innerHTML = "Not found";

    }
}