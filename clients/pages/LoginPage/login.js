document.addEventListener("DOMContentLoaded", () => {
    var navbar = document.querySelector("#nav");
    var header = document.querySelector("header")
    var sticky = navbar.offsetTop;

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
});