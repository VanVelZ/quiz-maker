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
            
            document.getElementById("student").innerHTML = student.name
            document.getElementById("student_id").innerHTML = student.studentId

            document.getElementById("teacher").innerHTML = teacher.name
            document.getElementById("teacher_id").innerHTML = teacher.teacherId

            notification.innerText = "Welcome " + user.name

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