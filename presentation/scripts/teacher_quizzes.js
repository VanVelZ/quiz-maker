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