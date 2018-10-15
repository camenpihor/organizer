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
    console.log("adding form");
    console.log(formType);
    var totalFormElement = document.getElementById("id_" + formType + "-TOTAL_FORMS");
    console.log(totalFormElement);
    var formSetElement = document.getElementById(formType + "-formset");
    var emptyFormElement = document.getElementById("empty-" + formType + "-form");
    var initialNumForms = parseInt(totalFormElement.value);

    var removeButton = document.createElement("input");
    removeButton.type = "button";
    removeButton.value = "X";
    removeButton.name = formType + "-" + initialNumForms;
    removeButton.onclick = function() {removeForm(formType, initialNumForms + 1)};

    var formHeader = document.createElement("h2");
    var formHeaderText = document.createTextNode((initialNumForms + 1) + " ");
    formHeader.appendChild(formHeaderText);
    formHeader.appendChild(removeButton);

    formSetElement.insertAdjacentElement('beforeend', formHeader);
    formSetElement.insertAdjacentHTML('beforeend', emptyFormElement.innerHTML.replace(/__prefix__/g, initialNumForms));
    totalFormElement.value = initialNumForms + 1;
}

function removeForm(formType, formIdx) {
    console.log("removing form");
    console.log(formType + " " + formIdx);
    var formSetElement = document.getElementById(formType + "-formset");
    var formSetChildren = formSetElement.children
    var searchString = formType + "-" + (parseInt(formIdx) - 1)
    console.log(searchString)

    for (var i = 0; i < formSetChildren.length; i++) {
        if (formSetChildren[i].hasAttribute("name")) {
            if (formSetChildren[i].name.includes(searchString)) {
                formSetChildren[i].style.display = "none";
            }
        }
    }
    document.getElementById("id_" + formType + "-" + (parseInt(formIdx) - 1) + "-DELETE").value = "on"
}
