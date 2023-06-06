var i = 0;
var txt = "Unlocking Knowledge's Hidden Gems: Discover, Explore, and Innovate!";
var speed = 50; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.querySelector('#typer').innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}

typeWriter();

window.addEventListener("load", () => {
    document.querySelector('#random-gibberish').classList.add("visible")
})