console.log(getCookie('userId'))
getStudentClasses()

function getStudentInfo() {
   
    thisUserId = getCookie('userId')

        let xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
            console.log(user)
                
        document.getElementById("studentName").innerHTML = user.firstName + " " + user.lastName
        document.getElementById("studentId").innerHTML = user.usersId
        document.getElementById("classes").innerHTML = ""
        
        }

    }



    url = url = "http://127.0.0.1:5000/user/" + thisUserId

    xhttp.open("GET", url, true)
    xhttp.send()

}

function getStudentClasses() {
   
    thisUserId = getCookie('userId')

        let xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            let classesRes = JSON.parse(this.responseText)
            let classes
            console.log(classesRes)
            for (i = 0; i < classesRes.length; i++) {
                if (classesRes[i].studentId == thisUserId) {
                    clases += " " + classesRes[i]
                }
            }
            console.log(classes)
            document.getElementById("classes").innerHTML = ""
        }

    }



    url = url = "http://127.0.0.1:5000/studentcourses"

    xhttp.open("GET", url, true)
    xhttp.send()

}

function logout(event) {

    event.preventDefault()
    console.log("logout")

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
    clearCookie([userId])
}