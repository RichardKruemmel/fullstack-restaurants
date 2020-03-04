document.addEventListener("DOMContentLoaded", function() {

  var paragraphEl = document.querySelector('p');

  function updateName () {
    var name = prompt('Enter a new name');
    paragraphEl.textContent = 'Player 1: ' + name;
  }

  paragraphEl.addEventListener('click', updateName);

});
