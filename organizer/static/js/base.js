function countChar(simplemde) {
  document.getElementById("num_characters").innerText = simplemde.value().length;
  document.getElementById("num_words").innerText = simplemde.value().split(' ').length - 1;
  document.getElementById("num_lines").innerText = simplemde.value().split("\n").length;
  document.getElementById("num_paragraphs").innerText = simplemde.value().split("\n\n").length;
}

function expandSideNav() {
  console.log("expanding side navigation");
  document.getElementById("side-nav").style.transform = "translate(0, 0)";
}

function closeSideNav() {
  console.log("closing side navigation");
  document.getElementById("side-nav").style.transform = "translate(-70vw, 0)";
}
