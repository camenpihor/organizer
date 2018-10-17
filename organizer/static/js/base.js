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
    var formElement = document.getElementById("empty-" + formType + "-form").cloneNode(true);
    var initialNumForms = parseInt(totalFormElement.value);

    var removeButton = document.createElement("button");
    removeButton.type = "button";
    removeButton.className = "remove-form-button"
    removeButton.id = formType + "-" + initialNumForms + "-remove-button";
    removeButton.onclick = function() {removeForm(formType, initialNumForms + 1)};
    var buttonText = document.createTextNode("X");
    removeButton.appendChild(buttonText);

    formElement.id = formType + "-" + initialNumForms + "-form"
    formElement.style.display = "grid"

    formSetElement.insertAdjacentElement('beforeend', removeButton);
    formSetElement.insertAdjacentHTML('beforeend', formElement.outerHTML.replace(/__prefix__/g, initialNumForms));
    totalFormElement.value = initialNumForms + 1;
}

function removeForm(formType, formIdx) {
    console.log("removing form");
    var formSetElement = document.getElementById(formType + "-formset");
    var formSetChildren = formSetElement.children
    var searchString = formType + "-" + (parseInt(formIdx) - 1)
    console.log(searchString)

    for (var i = 0; i < formSetChildren.length; i++) {
        if (formSetChildren[i].hasAttribute("id")) {
            if (formSetChildren[i].id.includes(searchString)) {
                formSetChildren[i].style.display = "none";
                formSetChildren[i].value = "";
            }
        }
    }
}
