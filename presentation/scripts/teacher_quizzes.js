function logout(event) {

    event.preventDefault()
    console.log("logout")

    clearCookie([userId])

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
}

function getTeacherInfo() {
   
    thisUserId = getCookie('userId')

        let xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
            console.log(user)
                
        document.getElementById("teacherName").innerHTML = user.firstName + " " + user.lastName
        document.getElementById("teacherId").innerHTML = user.usersId
        document.getElementById("class").innerHTML = ""
        }

    }



    url = url = "http://127.0.0.1:5000/user/" + thisUserId

    xhttp.open("GET", url, true)
    xhttp.send()

}
