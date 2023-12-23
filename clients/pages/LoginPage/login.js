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
        var arrowbase = document.getElementById("arrowbase");
        languagebtn.addEventListener("click", (e)=>{
          e.stopPropagation()
          arrowbase.classList.toggle("show")
          languagenav.classList.toggle("show")
          firstInput.classList.toggle("disabledcursor")
        })
        body.addEventListener('click', function(){
          arrowbase.classList.toggle("show")
          languagenav.classList.toggle("show")
          firstInput.classList.toggle("disabledcursor")
        })
  //languageNav Mobile
        var languagebtnS = document.getElementById("langBtn2")
        var arrow = document.querySelector("#arrow")
        var languagenavS = document.getElementById("langNav2")
        languagebtnS.addEventListener("click", (e)=>{
          e.stopPropagation()
            arrow.classList.toggle("show")
            languagenavS.classList.toggle("show")
        })
        body.addEventListener('click', function(){
          arrow.classList.remove("show")
          languagenavS.classList.remove("show")
        })

  //checkbox
      const checkboxF = document.getElementById('checkboxF');
      const checkboxS = document.getElementById('checkboxS');

      checkboxF.checked = true;
      let previousStateF = true;
      let previousStateS = false;
      checkboxF.addEventListener('change', function () {
        if (checkboxF.checked) {
          checkboxS.checked = false;
          previousStateF = true;
          previousStateS = false;
        }
        else if (!checkboxF.checked && !checkboxS.checked){
          checkboxF.checked = previousStateF;
          checkboxS.checked = previousStateS;
          previousStateF = previousStateF;
          previousStateS = previousStateS;
        }
        languagenav.classList.toggle("show")
      });

      checkboxS.addEventListener('change', function () {
        if (checkboxS.checked) {
          checkboxF.checked = false;  
          previousStateS = true;
          previousStateF = false;
        }
        else if (!checkboxF.checked && !checkboxS.checked){
          checkboxF.checked = previousStateF;
          checkboxS.checked = previousStateS;
          previousStateF = previousStateF;
          previousStateS = previousStateS;
        }
        languagenav.classList.toggle("show")
      });
      
});
