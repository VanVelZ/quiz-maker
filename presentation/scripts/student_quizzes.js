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
            let classes = ''
            console.log(classesRes[2].studentId)
            for (i = 0; i < classesRes.length; i++) {
                if (classesRes[i].studentId == thisUserId) {
                    if (classesRes[i].courseId == 1){
                        classes += "Physical Science, "
                    } else if (classesRes[i].courseId == 2) {
                        classes += "Biology, "
                    }
                    
                }
            }
            console.log(classes)
            document.getElementById("classes").innerHTML = classes
            // console.log(courses)
            // Array.prototype.forEach.call(courses, function (course) {
            //     document.getElementById("classes").innerHTML = `
            //         ${course.coursesId}${course.name}
            //     `
            // });

        }

    }



    url = url = "http://127.0.0.1:5000/studentcourses"

    xhttp.open("GET", url, true)
    xhttp.send()

}

function getCourses(){

    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let courses = JSON.parse(this.response)
            console.log(courses)
            Array.prototype.forEach.call(courses, function (course) {
                document.getElementById("courseSelect").innerHTML = `
                    <option value=${course.coursesId}>${course.name}</option>
                `
            });
        } 
    }

    let url = "http://127.0.0.1:5000/courses/studentcourses"

    xhr.open("GET", url, true)

    xhr.send()
}

function logout(event) {

    event.preventDefault()
    console.log("logout")

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
    clearCookie([userId])
}