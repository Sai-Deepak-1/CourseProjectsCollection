// alert("This is the first alert from the scripts.js file");

// $("h1").css("color", "red");

// $("document").ready(function() {
//     $("h1").css("color", "red");
// });

// $("h1").click(function () {
//    $("h1").css("font-family", "Indie Flower"); 
// });

$(document).keypress(function (event) {
    $("h1").text($("h1").text()+event.key);
})