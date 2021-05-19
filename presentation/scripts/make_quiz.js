
//Globals
questionCount = 1
class Question {
    constructor(id, description, answers=[]) {
        this.id = id
        this.description = description
        this.answers = answers
    }
}
class Answer {
    constructor(description, isCorrect, id=0) {
        this.description = description
        this.isCorrect = isCorrect
        this.id = id
    }
}
class Quiz {
    constructor(name, courseId, questions, id=0){
        this.name = name
        this.courseId = courseId
        this.questions = questions
        this.id = id
    }
}
function onLoad(){
    teacherId = 6
    getCourses()
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

    let url = "http://127.0.0.1:5000/courses/teacher/" + teacherId

    xhr.open("GET", url, true)

    xhr.send()
}
function submitQuiz(){
    let quizName = document.getElementById("quizName").value
    let courseId = document.getElementById("courseSelect").value
    let quiz = new Quiz(quizName, courseId, getQuestions())
    let json = JSON.stringify(quiz)

    let xhttp = new XMLHttpRequest();


    xhttp.onreadystatechange = function () {
            
        console.log(this.response)

}



let url  = "http://127.0.0.1:5000/quiz/"

xhttp.open("PUT", url, true)
console.log(json)
xhttp.setRequestHeader('Content-type','application/json')
xhttp.send(json)

}
function logout(event) {

    event.preventDefault()
    console.log("logout")

    clearCookie([userId])

    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
}
function getQuestions() {
    let questionDescriptions = document.getElementsByClassName("questionDescription")
    let questions = []
    let count = 1
    Array.prototype.forEach.call(questionDescriptions, function (element) {
        let question = new Question(count, element.value)
        getAnswersFor(question)
        questions.push(question)
        count++
    });
    console.log(questions)
    return questions
}
function getAnswersFor(question){
    let answers = document.getElementsByClassName(`q${question.id}Answer`)
    let answerRadios = document.getElementsByName(`q${question.id}Radio`)
    let selectedValue = getChecked(answerRadios);
    Array.prototype.forEach.call(answers, function (element) {
        question.answers.push(new Answer(element.value, selectedValue == element.name))
    });
}
function getChecked(radioButtions){
    for (const a of radioButtions) {
        if (a.checked) {
            return a.value;
        }
    }

}
function addQuestion(){
    questions = getQuestions()
    questionCount += 1
    document.getElementById("quiz").innerHTML += 
    `
    <tr>
        <td class="dataName">Question ${questionCount}</td>
        <td id="q1"><input class="questionDescription" name="q${questionCount}" type="text" placeholder="Question" id="q${questionCount}Description"></td>
    </tr>
    <tr>
        <td id="a1_1"><input class="q${questionCount}Answer" name="a${questionCount}_1" type="text" placeholder="Answer"></td>
        <td id="option1_1Radio"> A <input type="radio" name="q${questionCount}Radio" value="a${questionCount}_1" checked> Correct Answer </td>
    </tr>
    <tr>
        <td id="a1_2"><input class="q${questionCount}Answer" name="a${questionCount}_2" type="text" placeholder="Answer"></td>
        <td id="option1_2Radio"> B <input type="radio" name="q${questionCount}Radio" value="a${questionCount}_2"> Correct Answer </td>
    </tr>
    <tr>
        <td id="a1_3"><input class="q${questionCount}Answer" name="a${questionCount}_3" type="text" placeholder="Answer"></td>
        <td id="option1_3Radio"> C <input type="radio" name="q${questionCount}Radio" value="a${questionCount}_3"> Correct Answer </td>
    </tr>
    <tr>
        <td id="a1_4"><input class="q${questionCount}Answer" name="a${questionCount}_4" type="text" placeholder="Answer"></td>
        <td id="option1_4Radio"> D <input type="radio" name="q${questionCount}Radio" value="a${questionCount}_4"> Correct Answer </td>
    </tr>
    `
    refillValues(questions)
}

function refillValues(questions){
    let count = 0
    questionDescriptions = document.getElementsByClassName("questionDescription")
        Array.prototype.forEach.call(questionDescriptions, function (element) {
            if(count < questions.length){ 
                let answers = document.getElementsByClassName(`q${questions[count].id}Answer`)
                let answerRadios = document.getElementsByName(`q${questions[count].id}Radio`)
                let selectedValue = getChecked(answerRadios);
                let aCount = 0
                Array.prototype.forEach.call(answers, function (answer) {
                    answer.value = questions[count].answers[aCount].description
                    if(questions[count].answers[aCount].isCorrect) answerRadios[aCount].checked = true
                    aCount+=1
                });
                element.value = questions[count].description
            }
            count+=1
    });
}