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

function expandHistoryItem(element) {
  if (event.target.tagName != "A") {
    console.log("expanding/collapsing history item");
    var elementChildren = element.children;
    for (var i = 0; i < elementChildren.length; i++) {
      if (elementChildren[i].classList.contains("expanded-history-item")) {
        elementChildren[i].classList.toggle("open");
      }
    }
  }
  else {
    console.log("not closing history item since 'A' tag was selected")
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
    }
    target.innerText = "Collapse All";
  }

  else {
    console.log("collapsing all history");
    for (var i = 0; i < historyListChildren.length; i++) {
      if (historyListChildren[i].classList.contains("expanded-history-item")) {
        historyListChildren[i].classList.remove("open");
      }
    }
    target.innerText = "Expand All";
  }
}
