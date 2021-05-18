console.log(getCookie('userId'))

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
// getStudentInfo()

function logout(event) {

    event.preventDefault()
    console.log("logout")

    clearCookie([userId])

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
}