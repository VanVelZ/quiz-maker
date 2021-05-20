
getStudentClasses()

function getStudentInfo() {
   
    thisUserId = getCookie('userId')

        let xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
                
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
            let classes = []
            classesRes.forEach(sc => {
                classes.push(getCourse(sc.courseId))
            });

        }

    }



    url = "http://127.0.0.1:5000/loadstudentcourses/" + thisUserId

    xhttp.open("GET", url, true)
    xhttp.send()

}

function getCourse(id){

    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let course = JSON.parse(this.response)
                 document.getElementById("classes").innerHTML += 
                 `
                     <option value=${id}>${course.name}</option>
                 `

            return course
        } 
    }

    let url = "http://127.0.0.1:5000//courses/" + id

    xhr.open("GET", url, true)

    xhr.send()
}

function findQuizzes(){

    let xhr = new XMLHttpRequest();

    studid = getCookie('userId')
    
    courid = document.getElementById("classes").value
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let quizzes = JSON.parse(this.response)
                 
            
        } 
    }

    let url = "http://127.0.0.1:5000//quizzes/" + courid + "/" + studid

    xhr.open("GET", url, true)

    xhr.send()
}

function logout(event) {

    event.preventDefault()

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
    clearCookie([userId])
}