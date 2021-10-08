$(document).ready(function(){
  $('.sidenav').sidenav();
});

var addFavourites = 'add to favourites<i class="material-icons right">favorite_border</i>';
var removeFavourites = 'remove from favourites<i class="material-icons right">favorite</i>';
let buttons = document.getElementsByClassName("favourites-button");

for (let button of buttons) {
  button.addEventListener("click", function() {
    if (button.innerHTML == addFavourites) {
      button.innerHTML = removeFavourites;
    } else {
      button.innerHTML = addFavourites;
    }
  }, false);
}
