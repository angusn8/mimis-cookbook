window.onresize = resize;
function resize()
{
    var resize = document.getElementById("nav-links");

    if (window.innerWidth > 925) {
        resize.style.visibility = "visible";
    } else {
        resize.style.visibility = "hidden";
    }
}

function show_hide() {
   var click = document.getElementById("nav-links");

   if (click.style.visibility === "hidden" || click.style.visibility == "") {
      click.style.visibility = "visible";
   } else {
      click.style.visibility = "hidden";
   }
}

let previousLength = 0;

function bulletedInput(event) {
  const bullet = "\u2022";
  const newLength = event.target.value.length;
  const characterCode = event.target.value.substr(-1).charCodeAt(0);

  if (newLength > previousLength) {
    if (characterCode === 10) {
      event.target.value = `${event.target.value}${bullet} `;
    } else if (newLength === 1) {
      event.target.value = `${bullet} ${event.target.value}`;
    }
  }
  
  previousLength = newLength;
}