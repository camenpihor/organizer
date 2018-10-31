function outlineQuestionObject(form_type) {
  console.log("filling form outline")
  if (form_type == "resource") {
    simplemde.value("# Summary \n\n\n\n# Resource \n\n\n\n# Notes\n\n")
  }

  if (form_type == "thought") {
    simplemde.value("# Summary \n\n\n\n# Thought\n\n")
  }

  if (form_type == "answer") {
    simplemde.value("# Summary \n\n\n\n# Answer\n\n")
  }

  if (form_type == "none") {
    simplemde.value("")
  }
  simplemde.codemirror.focus();
  simplemde.codemirror.setCursor(2);
}

function expandHistoryItem(thisButton, historyElementID) {
  console.log("expanding/collapsing history item");
  var element = document.getElementById(historyElementID);
  element.classList.toggle("open");
  if (element.classList.contains("open")) {
    thisButton.innerText = "collapse";
  }
  else {
    thisButton.innerText = "expand";
  }
}

function expandAllHistory() {
  var target = event.target;
  var historyListChildren = document.getElementById("history-list").getElementsByTagName('*');

  if (target.innerText == "Expand All") {
    console.log("expaning all history")
    for (var i = 0; i < historyListChildren.length; i++) {
      if (historyListChildren[i].classList.contains("expanded-history-item")) {
        historyListChildren[i].classList.add("open");
      }
      if (historyListChildren[i].classList.contains("history-expand-button")) {
        historyListChildren[i].innerText = "collapse"
      }
    }
    target.innerText = "Collapse All";
  }

  else {
    console.log("collapsing all history");
    for (var i = 0; i < historyListChildren.length; i++) {
      if (historyListChildren[i].classList.contains("expanded-history-item")) {
        historyListChildren[i].classList.remove("open");
      }
      if (historyListChildren[i].classList.contains("history-expand-button")) {
        historyListChildren[i].innerText = "expand"
      }
    }
    target.innerText = "Expand All";
  }
}

function editHistoryItem(objectType, objectID, objectForm) {
  console.log("editing history item");
  console.log(objectType);
  console.log(objectID);
  document.getElementById("obj-picker-button").value = objectType;
  document.getElementById("edit-object-id").value = objectID;
  document.getElementById("obj-picker-button").scrollIntoView({behavior: 'smooth'});
  window.setTimeout(function() {simplemde.codemirror.focus()}, 1000);
  simplemde.value(objectForm);
}
