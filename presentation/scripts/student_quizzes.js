console.log(getCookie('userId'))

function getStudentInfo() {

    thisUserId = getCookie('userId')

        let xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
            console.log(user)
                
        document.getElementById("studentName").innerHTML = ""
        document.getElementById("studentId").innerHTML = ""
        document.getElementById("classes").innerHTML = ""
        }

    }



    url = url = "http://127.0.0.1:5000/user/" + thisUserId

    xhttp.open("GET", url, true)
    xhttp.send()
}
getStudentInfo()

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