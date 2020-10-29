(function() { //IIFE

  'use strict';

  // selectInput is the select element w/ id of 'choose'
  var selectInput = document.getElementById('choose'),
      // here we are compiling a list of all the nodes w/ a class of 'options'
      panels = document.querySelectorAll('.options'),
      currentSelect,
      elmClass,
      i;


  // To allow for compatibility with IE < 10,
  // we'll use these custom add/remove class functions
  // instead of classList.add()/.remove()

  function addClass( elm, newClass ) {
    elm.className += ' ' + newClass;
  }


  function removeClass( elm, deleteClass ) {
    elm.className = elm.className.replace(new RegExp("\\b" + deleteClass + "\\b", 'g'), '').trim();
    // the RegExp here makes sure that only the class we want to delete, and not any other
    // potentially matching stings get deleted.
    // e.g. -- if deleteClass = options and we also had a class of options--1 and options
    // on the elm, just the class of options would get deleted
  }


  // Function to go through all nodes with 'options' as a class
  // and remove the class of 'show' from them.
  function clearShow() {
    for ( i = 0; i < panels.length; i++ ) {
      removeClass( panels[i], 'show');
    }
  }


  // Function to add the class of show to the node that has
  // the class that matches the current value of the select drop down (#choose)
  function addShow( showThis ) {
    var el = document.getElementsByClassName( showThis );
    for ( i = 0; i < el.length; i++ ) {
      addClass( el[i], 'show')
    }
  }


  // Run the clear/add functions and set the value for what
  function vUpdate () {
    currentSelect = selectInput.value;

    clearShow();
    addShow(currentSelect);
  }


  // Update the value of currentSelect when selectInput changes option focus
  selectInput.addEventListener('change', vUpdate);


  // If a page is refreshed the select input may not reset to the default
  // option. If that's the case, find the current value of #choose
  // and run addShow() to make that content block visible
  if (selectInput.value !== 'nul') {
    currentSelect = selectInput.value;
    addShow(currentSelect);
  }

})(); // close IIFE