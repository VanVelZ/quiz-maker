questionCount = 1
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

function addQuestion(){
    questionCount += 1
    document.getElementById("quiz").innerHTML += 
    `
    <tr>
        <td class="dataName">Question ${questionCount}</td>
        <td id="q1"><input class="q${questionCount}Description" name="q${questionCount}" type="text" placeholder="Question"></td>
    </tr>
    <tr>
        <td id="a1_1"><input class="q${questionCount}Answer" name="a${questionCount}_1" type="text" placeholder="Answer"></td>
        <td id="option1_1Radio"> A <input type="radio" name="q${questionCount}Radio" value="a${questionCount}_1"> Correct Answer </td>
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

}