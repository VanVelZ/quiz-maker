function login() {
    
    event.preventDefault();

    logn = document.getElementById("loginField").value
    passf = document.getElementById("passField").value
    
    user = {
        loginId: logn,
        password: passf
    }
    var json = JSON.stringify(user)

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
            let cookie = {
                name: 'userId',
                value: user.userId
                }
            clearCookie()
            setCookie([cookie])

            // if student
            if (user.roleId == 1){
                window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/student_quizzes.html"
            } else {
                window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/teacher_quizzes.html"
            }

        }

    }

    url = url = "http://127.0.0.1:7001/login"

    xhttp.open("POST", url, true)
    xhttp.setRequestHeader('Content-type','application/json')
    xhttp.send(json)
    

}
clearCookie(userId)

// {
//     "loginId": "100001",
//     "password": "password"
// }