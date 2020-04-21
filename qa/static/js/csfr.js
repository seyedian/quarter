function getCookieValue(strCookieName) {
    try {
        var cookieValue = null;
        var cookies = document.cookie.split(';');
        if (cookies.length > 0) {
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, strCookieName.length + 1) === strCookieName + '=') {
                    cookieValue = decodeURIComponent(cookies.substring(strCookieName.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    } catch (err) {
        console.log(err);
    }
}