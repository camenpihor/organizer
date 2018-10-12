function questionHandler(question_id) {
    console.log(question_id)
    console.log("deciding what to do")
    var questionElement = document.getElementById(question_id);
    if (!questionElement.classList.contains("opened")) {
        expandQuestion(questionElement);
    }

    else {
        closeQuestion(questionElement);
    }

}

function expandQuestion(questionElement) {
    console.log("opening");
    questionElement.querySelector(".question-bottom").style.display = "block";
    questionElement.classList.add("opened");
}

function closeQuestion(questionElement) {
    console.log("closing");
    questionElement.querySelector(".question-bottom").style.display = "none";
    questionElement.classList.remove("opened");
}
