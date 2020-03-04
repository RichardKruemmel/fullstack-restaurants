document.addEventListener("DOMContentLoaded", function() {

  function createParagraph() {
      var paragraphEl = document.createElement('p');
      paragraphEl.textContent = 'You clicked the button!';
      document.body.appendChild(paragraphEl);
  }

    var buttonEl = document.querySelector('button');
    buttonEl.addEventListener('click', createParagraph);

});


/* DOMContentLoaded --> wrap JS around this block, so it will wait until
all content (e.g. images, css, html) has been loaded. Other than that,
JS will try to access something that potentitally
doesn't exist yet, your app will break */
