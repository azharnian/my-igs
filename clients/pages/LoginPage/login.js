document.addEventListener("DOMContentLoaded", () => {
  var navbar = document.querySelector("#nav");
  var header = document.querySelector("header");
  var sticky = navbar.offsetTop;
  //nav background color
  window.onscroll = function () {
    myFunction();
  };

  function myFunction() {
    if (window.pageYOffset >= sticky) {
      header.classList.add("fixed");
    } else {
      header.classList.remove("fixed");
    }
  }
  //hidenav responsive
  const hamburger_menu = document.querySelector(".hamburger");
  const hamburger_menuSec = document.querySelector(".hamburger_Second")
  const body = document.querySelector("body");
  const HideNav = document.querySelector("#HideNav")

  hamburger_menu.addEventListener("click", function () {
    hamburger_menu.classList.toggle("HideNavMode");
    hamburger_menuSec.classList.remove("HideNavMode");
    function bodyNav(){
      body.classList.toggle("HideNavMode");
      HideNav.classList.toggle("HideNavMode");
    }
    setTimeout(bodyNav, 349)
  });
  
  hamburger_menuSec.addEventListener("click", function () {
    hamburger_menuSec.classList.toggle("HideNavMode");
    hamburger_menu.classList.remove("HideNavMode");
    function bodyNav(){
      body.classList.toggle("HideNavMode");
      HideNav.classList.toggle("HideNavMode");
    }
    setTimeout(bodyNav, 349)
  });
    //language nav
        var languagebtn = document.getElementById("langBtn")
        var languagenav = document.getElementById("langNav")
        var firstInput = document.querySelector(".firstinput")
        var basearrow = document.getElementById("baseArrow");
        languagebtn.addEventListener("click", (e)=>{
          e.stopPropagation();
          basearrow.classList.toggle("show")
          languagenav.classList.toggle("show")
            firstInput.classList.toggle("disabledcursor")
        })
        body.addEventListener('click',()=>{
          languagenav.classList.remove("show")
          basearrow.classList.remove("show")
          firstInput.classList.remove("disabledcursor")
        })
  //languageNav Mobile
        var languagebtnS = document.getElementById("langBtn2")
        var arrow = document.querySelector("#arrow")
        var languagenavS = document.getElementById("langNav2")
        languagebtnS.addEventListener("click", ()=>{
            arrow.classList.toggle("show")
            languagenavS.classList.toggle("show")
        })

  //checkbox base view
      const checkboxF = document.getElementById('checkboxF');
      const checkboxS = document.getElementById('checkboxS');

      checkboxF.checked = true;
      let previousStateF = true;
      let previousStateS = false;
      checkboxF.addEventListener('change', function () {
        if (checkboxF.checked) {
          checkboxS.checked = false;
          checkboxFH.checked = true;
          checkboxSH.checked = false;
          previousStateF = true;
          previousStateS = false;
          previousStateFH = true;
          previousStateSH = false;
        }
        else if (!checkboxF.checked && !checkboxS.checked){
          checkboxFH.checked = previousStateFH;
          checkboxSH.checked = previousStateSH;
          checkboxF.checked = previousStateF;
          checkboxS.checked = previousStateS;
          previousStateFH = previousStateFH;
          previousStateSH = previousStateSH;
          previousStateF = previousStateF;
          previousStateS = previousStateS;
        }
      });

      checkboxS.addEventListener('change', function () {
        if (checkboxS.checked) {
          checkboxF.checked = false;  
          checkboxSH.checked =true;
          checkboxFH.checked = false;
          previousStateS = true;
          previousStateF = false;
          previousStateSH = true;
          previousStateFH = false;
        }
        else if (!checkboxF.checked && !checkboxS.checked){
          checkboxFH.checked = previousStateFH;
          checkboxSH.checked = previousStateSH;
          checkboxF.checked = previousStateF;
          checkboxS.checked = previousStateS;
          previousStateFH = previousStateFH;
          previousStateSH = previousStateSH;
          previousStateF = previousStateF;
          previousStateS = previousStateS;
        }
      });
  //checkbox mobile
  const checkboxFH = document.getElementById('checkboxFH');
      const checkboxSH = document.getElementById('checkboxSH');

      checkboxFH.checked = true;
      let previousStateFH = true;
      let previousStateSH = false;
      checkboxFH.addEventListener('change', function () {
        if (checkboxFH.checked) {
          checkboxSH.checked = false;
          checkboxF.checked = true;
          checkboxS.checked = false;
          previousStateFH = true;
          previousStateSH = false;
          previousStateF = true;
          previousStateS = false;
          
        }
        else if (!checkboxFH.checked && !checkboxSH.checked){
          checkboxFH.checked = previousStateFH;
          checkboxSH.checked = previousStateSH;
          checkboxF.checked = previousStateF;
          checkboxS.checked = previousStateS;
          previousStateFH = previousStateFH;
          previousStateSH = previousStateSH;
          previousStateF = previousStateF;
          previousStateS = previousStateS;
        }
        languagenavS.classList.remove("show");
        arrow.classList.remove("show");
      });

      checkboxSH.addEventListener('change', function () {
        if (checkboxSH.checked) {
          checkboxFH.checked = false;  
          checkboxS.checked = true;
          checkboxF.checked = false
          previousStateSH = true;
          previousStateFH = false;
          previousStateS = true;
          previousStateF = false;
        }
        else if (!checkboxFH.checked && !checkboxSH.checked){
          checkboxFH.checked = previousStateFH;
          checkboxSH.checked = previousStateSH;
          checkboxF.checked = previousStateF;
          checkboxS.checked = previousStateS;
          previousStateFH = previousStateFH;
          previousStateSH = previousStateSH;
          previousStateF = previousStateF;
          previousStateS = previousStateS;
        }
        languagenavS.classList.remove("show");
        arrow.classList.remove("show");
      });

});