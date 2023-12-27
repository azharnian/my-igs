document.addEventListener("DOMContentLoaded", function () {
  const menu_btn = document.querySelector("button.hamburger");
  const mobile_menu = document.querySelector(".mobile-nav");
  const cross_menu = document.querySelector(".x");
  const logo = document.getElementById("header--logo");
  const languange = document.getElementById("header--language");
  const body = document.querySelector("body");
  menu_btn.addEventListener("click", function () {
    body.classList.toggle("is-active");
    menu_btn.classList.toggle("is-active");
    mobile_menu.classList.toggle("is-active");
    arrow.classList.toggle("show");
  });

  cross_menu.addEventListener("click", function () {
    body.classList.toggle("is-active");
    menu_btn.classList.remove("is-active");
    mobile_menu.classList.remove("is-active");
  });


  //profile

  const ProfileBtn = document.getElementById("headerProf");
  const arrow = document.getElementById("arrow");
  const Profilenav = document.getElementById("profNav");
  ProfileBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    arrow.classList.toggle("show");
    Profilenav.classList.toggle("show");
  });
  Profilenav.addEventListener("click", function (e) {
    e.stopPropagation();
  });
  body.addEventListener("click", function () {
    arrow.classList.remove("show");
    Profilenav.classList.remove("show");
  });

  //darkmode
  const buttonDark = document.getElementById("switch");

  buttonDark.addEventListener("click", () => {
    body.classList.toggle("dark");
  });
  //language
  const languageNav = document.getElementById("languageNavWrapper");
  const languageNavBtn = document.getElementById("languageNavBtn");
  const chevronLanguage = document.getElementById("arrowlang");

  languageNavBtn.addEventListener("click", () => {
    languageNav.classList.toggle("show");
    chevronLanguage.classList.toggle("show");
    languageNavBtn.classList.toggle("show");
  });

  //checkbox base view
  const checkboxF = document.getElementById("Indonesia");
  const checkboxS = document.getElementById("English");

  checkboxF.checked = true;
  let previousStateF = true;
  let previousStateS = false;
  checkboxF.addEventListener("change", function () {
    if (checkboxF.checked) {
      checkboxS.checked = false;
      previousStateF = true;
      previousStateS = false;
    } else if (!checkboxF.checked && !checkboxS.checked) {
      checkboxF.checked = previousStateF;
      checkboxS.checked = previousStateS;
      previousStateF = previousStateF;
      previousStateS = previousStateS;
    }
  });

  checkboxS.addEventListener("change", function () {
    if (checkboxS.checked) {
      checkboxF.checked = false;
      previousStateS = true;
      previousStateF = false;
    } else if (!checkboxF.checked && !checkboxS.checked) {
      checkboxF.checked = previousStateF;
      checkboxS.checked = previousStateS;
      previousStateF = previousStateF;
      previousStateS = previousStateS;
    }
  });

  //checkbox responsive
  

  //notification base view
  const notifBtn = document.getElementById("notifBtn");
  const notifBox = document.getElementById("notifBox");
  const notifClose = document.getElementById("notifCloseBtn");

  notifBtn.addEventListener("click", (e)=>{
    e.stopPropagation();
    notifBox.classList.toggle("show");
  })
  notifClose.addEventListener("click", (e)=>{
    e.stopPropagation();
    notifBox.classList.remove("show");
  })
  notifBox.addEventListener("click", (e)=>{
    e.stopPropagation();
  })

  body.addEventListener("click", function () {
    notifBox.classList.remove("show");
  });

  //languageNav mobile

  const languageMobileNavBtn = document.getElementById("languageMobileNavBtn");
  const languageMobileNav = document.getElementById("languageMobileNavWrapper");
  const languageMobileWrap = document.getElementById("languageMobileWrap");
  const arrow2 = document.getElementById("arrow2");

  languageMobileNavBtn.addEventListener("click", function () {
    languageMobileNav.classList.toggle("show");
    arrow2.classList.toggle("show");
  });

});
