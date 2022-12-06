

function viewDiv1(){
    document.getElementById("div1").style.display = "block";
    document.getElementById("div2").style.display = "none";
    document.getElementById("div3").style.display = "none";
    document.getElementById("main__id_1").style.borderBottom = "3px solid #8359de";
    document.getElementById("main__id_2").style.borderBottom = "0px solid #8359de";
    document.getElementById("main__id_3").style.borderBottom = "0px solid #8359de";
    document.getElementById("header__btn").style.background = "grey";
};

function viewDiv2(){
    document.getElementById("div1").style.display = "none";
    document.getElementById("div2").style.display = "block";
    document.getElementById("div3").style.display = "none";
};

function viewDiv3(){
    document.getElementById("div1").style.display = "none";
    document.getElementById("div2").style.display = "none";
    document.getElementById("div3").style.display = "block";
};