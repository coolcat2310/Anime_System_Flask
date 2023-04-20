$(document).ready(function() {

    $('#submit').click(function(){
        $.ajax({
            url: '/anime-list',
            type: 'get',
            contentType: 'application/json',
            data: {
                username: $('#username').val()
            },
            success: function(response) {
                $('#anime-list').text(response)
            }
        })
    })

})

$(document).ready(function() {
    $('#username').on('keyup', function(event) {
      if (event.key !== 'Enter') return;
      $('#submit').click();
      event.preventDefault();
    });
});