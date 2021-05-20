
getStudentClasses()
function getStudentInfo() {
   
    thisUserId = getCookie('userId')

        let xhttp = new XMLHttpRequest();
         xhttp.onreadystatechange = function () {

        if (this.readyState == 4 && this.status == 200) {
            let user = JSON.parse(this.responseText)
                
        document.getElementById("studentName").innerHTML = user.firstName + " " + user.lastName
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
            classesRes.forEach(sc => {
                getCourse(sc.courseId)
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

function loadQuiz(quizId){
    setCookie([new Cookie("userId", thisUserId), new Cookie("quizId", quizId)])
    location.href = "take_quiz.html"
}
function findQuizzes(){
    refresh()
    todoQuizzes()
    finishedQuizzes()
}
function todoQuizzes(){
    let xhr = new XMLHttpRequest();

    studid = getCookie('userId')
    
    let courid = document.getElementById("classes").value  
    refresh()
    console.log(courid)
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let quizzes = JSON.parse(this.response)
            console.log(quizzes)
            Array.prototype.forEach.call(quizzes, function (quiz) {
                document.getElementById("quizzes").innerHTML += 
                `
                <tr>
                    <td onclick="loadQuiz(${quiz.id})">${quiz.name}</td>
                    <td>-</td>
                </tr>
                `
            });
            
        } 
    }

    let url = "http://127.0.0.1:5000//quizzes/" + courid + "/" + studid
    console.log(url)
    xhr.open("GET", url, true)

    xhr.send()
}
function finishedQuizzes(){
    let xhr = new XMLHttpRequest();

    studid = getCookie('userId')
    
    let courid = document.getElementById("classes").value  
    console.log(courid)
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let quizzes = JSON.parse(this.response)
            console.log(quizzes)
            Array.prototype.forEach.call(quizzes, function (quiz) {
                document.getElementById("quizzes").innerHTML += 
                `
                <tr>
                    <td>${quiz.name}</td>
                    <td>${quiz.grade}</td>
                </tr>
                `
            });
        } 
    }

    let url = "http://127.0.0.1:5000//reviews/" + courid + "/" + studid
    xhr.open("GET", url, true)

    xhr.send()
}
function refresh(){
    document.getElementById("quizzes").innerHTML =  
    `            
    <tr>
        <th class="dataName">Quiz Name</th>
        <th >Grade</th>
    </tr>
    `

}
function logout(event) {

    event.preventDefault()
    console.log("logout")

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
    clearCookie([userId])
}

function sortOptions() {
    var options = document.getElementById('classes').options;
    var sorted = Array.prototype.sort.call(options, (a, b) => a.value < b.value)
    console.log(sorted)
    }