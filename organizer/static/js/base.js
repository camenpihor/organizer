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

function addForm(formType) {
    console.log("adding form")
    console.log(formType)
    var totalFormElement = document.getElementById("id_" + formType + "-TOTAL_FORMS")
    console.log(totalFormElement)
    var formSetElement = document.getElementById(formType + "-formset")
    var emptyFormElement = document.getElementById("empty-" + formType + "-form")
    var initialNumForms = parseInt(totalFormElement.value)

    formSetElement.insertAdjacentHTML('beforeend', "<h2> " + (initialNumForms + 1) + "</h2>")
    formSetElement.insertAdjacentHTML('beforeend', emptyFormElement.innerHTML.replace(/__prefix__/g, initialNumForms))
    totalFormElement.value = initialNumForms + 1
}
