function login() {
    
    event.preventDefault();
    
    thisUserId = document.getElementById("nameField").value
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

    url = url = "http://127.0.0.1:5000/users/" + thisUserId

    xhttp.open("GET", url, true)
    xhttp.send()
    

}

function logout() {
    event.preventDefault();

        let xhttp = new XMLHttpRequest();


            xhttp.onreadystatechange = function () {
                
        document.getElementById("name").innerHTML = ""
        document.getElementById("employee_id").innerHTML = ""
        document.getElementById("supervisor_id").innerHTML = ""

    }



    url = url = "http://127.0.0.1:5000/users/" + thisUserId

    xhttp.open("DELETE", url, true)
    xhttp.send()


}