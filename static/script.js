// Javascript function getResult(): Grabs the log of entries from database to view
function getResult() {
  // Uses AJAX to connect to the backend server
  $.ajax({
    // Python Flask url
    url: "/view",
    success: function(result) {
      console.log("received result: " + result);

      // For each item in the list that is returned in the Python function, we add the equivalent table HTML string
      // For each loop that applies the given function to each item in the list
      /*
        Example item:
        {
          name: "Avatar: The Last Airbender", 
          genre: "Adventure",
          time: 180
        }
      */
      $.each(JSON.parse(result), function(index, item){
        // Appending HTML
        $('#result_table').append('<tr><td>' + item.name + '</td><td>' + item.genre + '</td><td>' + item.time + '</td></tr>');
      });
    }
  });
}
