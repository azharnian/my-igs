const menu_btn = document.querySelector("button.hamburger");
const mobile_menu = document.querySelector(".mobile-nav");
const cross_menu = document.querySelector(".x");
const logo = document.getElementById("header--logo");
const languange = document.getElementById("header--language");
const body = document.querySelector("body")
menu_btn.addEventListener("click", function () {
  body.classList.toggle("is-active")
  menu_btn.classList.toggle("is-active");
  mobile_menu.classList.toggle("is-active");
});

cross_menu.addEventListener("click", function () {
  body.classList.toggle("is-active")
  menu_btn.classList.remove("is-active");
  mobile_menu.classList.remove("is-active");
});

// function openAndClose() {
//   if (this.booleanValue === true) {
//     this.booleanValue = false;
//     open();
//   } else {
//     this.booleanValue = true;
//     close();
//   }
// }
// function open() {
//   menu_btn.classList.add("is-active");
//   mobile_menu.classList.add("is-active");
//   logo.style.display = "none";
// }
// function close() {
//   menu_btn.classList.remove("is-active");
//   mobile_menu.classList.remove("is-active");
//   logo.style.display = "block";
// }



//profile

var ProfileBtn = document.getElementById("headerProf")
var arrow = document.getElementById("arrow")
var Profilenav = document.getElementById("profNav")
ProfileBtn.addEventListener("click", ()=>{
    arrow.classList.toggle("show")
    Profilenav.classList.toggle("show")
})