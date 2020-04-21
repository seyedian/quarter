$(document).ready(function () {
    $('#live-qa-form').submit(function (e) {
        e.preventDefault();
        var url = $('#live-qa-url').val();
        var scopes = [
            '.*google-analytics1.com/r/collect.*',
            '.*google-analytics2.com/r/collect.*',
            '.*google-analytics3.com/r/collect.*',
            '.*google-analytics4.com/r/collect.*'
        ];
        $(this).fadeOut('slow', function () {
            $('#live-qa-snipper').fadeIn('slow');
        });
        $.ajax({
            type: 'post',
            url: '',
            data: {
                csrfmiddlewaretoken: getCookieValue('csrftoken'),
                'command': 'start',
                "url": url,
                'scopes': scopes
            },
            dataType: 'json',
            success: function (response) {
                if (response.status == 'success') {
                    $('#live-qa-snipper').fadeOut('slow', function () {
                        $('#live-qa-table').fadeIn('slow');

                    });
                }
            },
            error: function (response) {
                console.log('error');
            }
        });
    });



    function updateTable() {
        setInterval(() => {
            $.ajax({
                type: 'post',
                url: '',
                data: {
                    csrfmiddlewaretoken: getCookieValue('csrftoken'),
                    'command': 'update'
                },
                dataType: 'json',
                success: function (response) {
                    console.log('i am here');
                }
            });
        }, 1000);
    }
});


function getCookieValue(strCookieName) {
    try {
        var cookieValue = null;
        var cookies = document.cookie.split(';');
        if (cookies.length > 0) {
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, strCookieName.length + 1) === strCookieName + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(strCookieName.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    } catch (err) {
        console.log(err);
    }
}


