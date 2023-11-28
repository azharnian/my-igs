document.addEventListener("DOMContentLoaded", () => {
    var navbar = document.querySelector("#nav");
    var header = document.querySelector("header")
    var sticky = navbar.offsetTop;
    //nav background color
    window.onscroll = function() {
        myFunction();
    };

    function myFunction() {
        if (window.pageYOffset >= sticky) {
            header.classList.add("fixed");
        } else {
            header.classList.remove("fixed");
        }
    }

    var hiddenLanguage = document.querySelector(".hidden-nav-language")
    var language = document.querySelector(".language");
    language.addEventListener('click', function(){
        
    })
    //hidenav responsive
        var smthng
    //language nav
        var languagebtn = document.getElementById("langBtn")
        var languagenav = document.getElementById("langNav")
        var firstInput = document.querySelector(".firstinput")
        languagebtn.addEventListener("click", ()=>{
            languagenav.classList.toggle("show")
            firstInput.classList.toggle("disabledcursor")
        })
        //selecting all exc LanguageNav (kelemahan (select satu satu)))
        var content = document.querySelector("section")
        var footer = document.querySelector("footer")
        var headerLogo = document.querySelector(".logo")
        var callLogo = document.querySelector(".call")
        content.addEventListener("click", ()=>{
            languagenav.classList.remove("show")
            firstInput.classList.remove("disabledcursor")
        })
        footer.addEventListener("click", ()=>{
            languagenav.classList.remove("show")
            firstInput.classList.remove("disabledcursor")
        })
        headerLogo.addEventListener("click", ()=>{
            languagenav.classList.remove("show")
            firstInput.classList.remove("disabledcursor")
        })
        callLogo.addEventListener("click", ()=>{
            languagenav.classList.remove("show")
            firstInput.classList.remove("disabledcursor")
        })
        
});