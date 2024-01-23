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
  //darkmode baseview
  const buttonDark2 = document.getElementById("switch2");

  buttonDark2.addEventListener("click", () => {
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
      checkboxFH.checked = true;
      checkboxSH.checked = false;
      previousStateF = true;
      previousStateS = false;
      previousStateFH = true;
      previousStateSH = false;
    } else if (!checkboxF.checked && !checkboxS.checked) {
      checkboxFH.checked = previousStateFH;
      checkboxSH.checked = previousStateSH;
      checkboxF.checked = previousStateF;
      checkboxS.checked = previousStateS;
      previousStateFH = previousStateFH;
      previousStateSH = previousStateSH;
      previousStateF = previousStateF;
      previousStateS = previousStateS;
    }
    languageNav.classList.remove("show");
    chevronLanguage.classList.remove("show");
    languageNavBtn.classList.remove("show");
  });

  checkboxS.addEventListener("change", function () {
    if (checkboxS.checked) {
      checkboxF.checked = false;
      checkboxSH.checked = true;
      checkboxFH.checked = false;
      previousStateS = true;
      previousStateF = false;
      previousStateSH = true;
      previousStateFH = false;
    } else if (!checkboxF.checked && !checkboxS.checked) {
      checkboxFH.checked = previousStateFH;
      checkboxSH.checked = previousStateSH;
      checkboxF.checked = previousStateF;
      checkboxS.checked = previousStateS;
      previousStateFH = previousStateFH;
      previousStateSH = previousStateSH;
      previousStateF = previousStateF;
      previousStateS = previousStateS;
    }
    languageNav.classList.remove("show");
    chevronLanguage.classList.remove("show");
    languageNavBtn.classList.remove("show");
  });
  //checkbox mobile
  const checkboxFH = document.getElementById("Indonesia2");
  const checkboxSH = document.getElementById("English2");

  checkboxFH.checked = true;
  let previousStateFH = true;
  let previousStateSH = false;
  checkboxFH.addEventListener("change", function () {
    if (checkboxFH.checked) {
      checkboxSH.checked = false;
      checkboxF.checked = true;
      checkboxS.checked = false;
      previousStateFH = true;
      previousStateSH = false;
      previousStateF = true;
      previousStateS = false;
    } else if (!checkboxFH.checked && !checkboxSH.checked) {
      checkboxFH.checked = previousStateFH;
      checkboxSH.checked = previousStateSH;
      checkboxF.checked = previousStateF;
      checkboxS.checked = previousStateS;
      previousStateFH = previousStateFH;
      previousStateSH = previousStateSH;
      previousStateF = previousStateF;
      previousStateS = previousStateS;
    }
    languageMobileNavBtn.classList.remove("show");
    languageMobileNav.classList.remove("show");
    arrow2.classList.remove("show");
  });

  checkboxSH.addEventListener("change", function () {
    if (checkboxSH.checked) {
      checkboxFH.checked = false;
      checkboxS.checked = true;
      checkboxF.checked = false;
      previousStateSH = true;
      previousStateFH = false;
      previousStateS = true;
      previousStateF = false;
    } else if (!checkboxFH.checked && !checkboxSH.checked) {
      checkboxFH.checked = previousStateFH;
      checkboxSH.checked = previousStateSH;
      checkboxF.checked = previousStateF;
      checkboxS.checked = previousStateS;
      previousStateFH = previousStateFH;
      previousStateSH = previousStateSH;
      previousStateF = previousStateF;
      previousStateS = previousStateS;
    }
    languageMobileNavBtn.classList.remove("show");
    languageMobileNav.classList.remove("show");
    arrow2.classList.remove("show");
  });

  //notification base view
  const notifBtn = document.getElementById("notifBtn");
  const notifBox = document.getElementById("notifBox");
  const notifClose = document.getElementById("notifCloseBtn");

  notifBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    notifBox.classList.toggle("show");
  });
  notifClose.addEventListener("click", (e) => {
    e.stopPropagation();
    notifBox.classList.remove("show");
  });
  notifBox.addEventListener("click", (e) => {
    e.stopPropagation();
  });

  body.addEventListener("click", function () {
    notifBox.classList.remove("show");
  });

  //languageNav mobile

  const languageMobileNavBtn = document.getElementById("languageMobileNavBtn");
  const languageMobileNav = document.getElementById("languageMobileNavWrapper");
  const languageMobileWrap = document.getElementById("languageMobileWrap");
  const arrow2 = document.getElementById("arrow2");

  languageMobileNavBtn.addEventListener("click", function () {
    languageMobileNavBtn.classList.toggle("show");
    languageMobileNav.classList.toggle("show");
    arrow2.classList.toggle("show");
  });

  //dokumentasi
  const opendokbtn1 = document.getElementById("opendokbtn1")
  const openpigbtn1 = document.getElementById("openpigbtn1")
  const dokumentasi1 = document.getElementById("dokumentasi1")
  const closebtn1 = document.getElementById("closebtn1")
  opendokbtn1.addEventListener("click", function(){
    dokumentasi1.classList.toggle("show");
  })
  openpigbtn1.addEventListener("click", function(){
    dokumentasi1.classList.toggle("show");
  })
  closebtn1.addEventListener("click", function(){
    dokumentasi1.classList.toggle("show");
  })
});
