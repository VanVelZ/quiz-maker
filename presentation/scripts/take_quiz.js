function logout(event) {

    event.preventDefault()
    console.log("logout")
    window.location.href = "///Users/alexjones/Desktop/RevatureTraining/Project2/presentation/index.html"
    clearCookie([userId])
}

function onLoad(){
    userId = getCookie("userId")
    quizId = getCookie("quizId")
    loadQuiz()
}
function loadQuiz(){

    let xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            quiz = JSON.parse(this.response)
            displayQuiz(quiz)
        } 
    }

    let url = "http://127.0.0.1:5000/quiz/" + quizId

    xhr.open("GET", url, true)

    xhr.send()
}
function displayQuiz(quiz){
    let questionCount = 1
    quiz.questions.forEach(question => {
        document.getElementById("quiz").innerHTML += 
        `
        <tr>
            <td class="dataName">Question ${questionCount}</td>
            <td id="q1">${question.description}</td>
        </tr>
        <tr>
            <td id="a1_1">${question.answers[0].description}</td>
            <td id="option1_1Radio"> A <input type="radio" name="q${question.id}Radio" value="${question.answers[0].id}"></td>
        </tr>
        <tr>
            <td id="a1_2">${question.answers[1].description}</td>
            <td id="option1_2Radio"> B <input type="radio" name="q${question.id}Radio" value="${question.answers[1].id}"></td>
        </tr>
        <tr>
            <td id="a1_3">${question.answers[2].description}</td>
            <td id="option1_3Radio"> C <input type="radio" name="q${question.id}Radio" value="${question.answers[2].id}"></td>
        </tr>
        <tr>
            <td id="a1_4">${question.answers[3].description}</td>
            <td id="option1_4Radio"> D <input type="radio" name="q${question.id}Radio" value="${question.answers[3].id}"></td>
        </tr>
        `
        questionCount += 1
        
    });
}
function submitQuiz(){
    Array.prototype.forEach.call(quiz.questions, question =>{
        question.studentsAnswer = getStudentAnswersFor(question)
    });
    let json = JSON.stringify(quiz)

    let xhttp = new XMLHttpRequest();


    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            review = JSON.parse(this.response)
        reviewQuiz(review)
        }
}



let url  = "http://127.0.0.1:5000/quiz/" + userId

xhttp.open("POST", url, true)
xhttp.setRequestHeader('Content-type','application/json')
xhttp.send(json)

}
function getChecked(radioButtions){
    for (const a of radioButtions) {
        if (a.checked) {
            return a.value;
        }
    }

}
function getStudentAnswersFor(question){
    let answerRadios = document.getElementsByName(`q${question.id}Radio`)
    let studentAnswer = getChecked(answerRadios)
    
    question.answeredCorrectly = Array.prototype.forEach.call(question.answers, answer =>{
        if (answer == studentAnswer) {return answer.isCorrect}
    })
    return studentAnswer
}
function reviewQuiz(quiz){
    document.getElementById("quiz").innerHTML = 
    `
    <h1>You scored ${quiz.grade}%</h1>
    `
}