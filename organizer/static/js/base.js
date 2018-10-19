function handleTextEditorButton(buttonElement) {
  var buttonClass = buttonElement.className
  if (buttonClass == "closed") {
    console.log("opening text editor")
    buttonElement.innerText = "-"
    document.getElementById("text-editor").style.display = "block"
    buttonElement.className = "open"
  } else {
    console.log("closing text editor")
    buttonElement.innerText = "+"
    document.getElementById("text-editor").style.display = "none"
    buttonElement.className = "closed"
  }
}

function countChar(simplemde) {
  document.getElementById("num_characters").innerText = simplemde.value().length
  document.getElementById("num_words").innerText = simplemde.value().split(' ').length - 1;
  document.getElementById("num_lines").innerText = simplemde.value().split("\n").length
  document.getElementById("num_paragraphs").innerText = simplemde.value().split("\n\n").length
}