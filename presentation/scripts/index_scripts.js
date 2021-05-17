function login() {
    
    event.preventDefault();
    
    user = {
        loginId: "100001",
        password: "password"
    }
    var json = JSON.stringify(user)

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
            console.log(user)
            
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

// {
//     "loginId": "100001",
//     "password": "password"
// }