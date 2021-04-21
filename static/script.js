var inputField = document.getElementById('view-form');
inputField.value = inputField.options[inputField.selectedIndex].value;
inputField.defaultValue = inputField.value;

// Javascript function
function getResult() {
  // Uses AJAX to connect to the backend server
  $.ajax({
    // Python Flask url
    url: "/view",
    success: function(result) {
      console.log("received result: " + result);

      // For each item in the list that is returned in the Python function, we add the equivalent table HTML string
      // For each loop
      // $('#result_table').remove();
      $.each(JSON.parse(result), function(index, elem){
        console.log("added");
        console.log(elem.select);
        $('#view-form').val(elem.select);
        // if (elem.category.localeCompare($('#view-form')))
        // Appending HTML
        $('#result_table').append('<tr><td>' + elem.item + '</td><td>' + elem.amount + '</td><td>' + elem.category + '</td></tr>');
      });
    }
  });
}
