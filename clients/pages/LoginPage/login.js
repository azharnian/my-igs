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
    var smthng

});