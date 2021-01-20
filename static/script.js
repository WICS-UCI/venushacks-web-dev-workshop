function getResult() {
  $.ajax({
    url: "/view",
    success: function(result) {
      console.log("received result: " + result);
      $.each(JSON.parse(result), function(index, item){
        console.log("added");
        $('#result_table').append('<tr><td>' + item.name + '</td><td>' + item.genre + '</td><td>' + item.time + '</td></tr>');
      });
    }
  });
}
