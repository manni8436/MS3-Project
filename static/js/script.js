$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.modal').modal();
  $('.carousel.carousel-slider').carousel({
      numVisible: 1
  }, {
      duration: 100
  }, {
      fullWidth: true
  });
});

let autoplay = true;

setInterval(function () {
    if (autoplay) $('.carousel.carousel-slider').carousel('next');
}, 5000);

$('.quotes-panel').hover(function () {
    autoplay = false;
}, function () {
    autoplay = true;
});