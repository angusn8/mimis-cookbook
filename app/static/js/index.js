window.onresize = resize;
window.onload = pageLoad;

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

function bulletedInput(event) {
  let previousLength = 0;

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

var fileInput = document.getElementById('recipe_image');

fileInput.addEventListener('change', function(event) {
  var input = event.target;
  for (var i = 0; i < input.files.length; i++) {
    document.getElementById('file_output').innerHTML = input.files[i].name;
  }
});

function pageLoad() {
  var ingredients = document.getElementById('recipe-ingredients').innerHTML;
  var ingredientArr = ingredients.split("\u2022");
  document.getElementById('recipe-ingredients').innerHTML = "";
  var printIngredients = document.getElementById('recipe-ingredients');

  for (var i = 0; i < ingredientArr.length; i++) {
    printIngredients.innerHTML += ingredientArr[i] + "<br><br>";
  }

  var directions = document.getElementById('recipe-directions').innerHTML;
  var directionArr = directions.split("\u2022");
  document.getElementById('recipe-directions').innerHTML = "";
  var printDirections = document.getElementById('recipe-directions');

  for (var i = 1; i < directionArr.length; i++) {
    printDirections.innerHTML += i + ". " + directionArr[i] + "<br><br>";
  }
}



