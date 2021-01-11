// intention is to update the search bar

$(document).ready( function () {
  $('input[name="locationsearch"]').keyup(getSearchData);
});

var getSearchData = function (e) {
  var jsondata = {
    value: $(this).val(),
  };
  console.log(jsondata);
  $.ajax({
    url: '/search/',
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify(jsondata),
    method: 'POST',
    success: function(response) {
      console.log(response);
    },
    error: function(error) {
      console.log(error);
    }
  });
};

