function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return undefined;
}
function setCookie(cname, value){
    document.cookie = `${cname}=` + value
}
function clearCookie(cname) {
    document.cookie = `${cname}=` + undefined
    window.location.href = "login.html"
}

function checkCookie() {
    employee = getCookie("employee")
    console.log(employee)
    if (employee == "undefined") {
        location.href = "login.html"
    }
}