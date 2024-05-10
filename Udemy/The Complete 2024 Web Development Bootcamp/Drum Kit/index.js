// alert("Hello, Welcome to the Drum Kit Page!!!");

var n = document.querySelectorAll(".drum").length;

for (var i = 0; i < n; i++) {
  document.querySelectorAll(".drum")[i].addEventListener("click", function () {
    alert("Click "+i);
  });
}
