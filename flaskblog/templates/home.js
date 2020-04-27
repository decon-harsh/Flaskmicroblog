function Choice(elem) {
    var box = document.getElementById("box");
    if (elem.id == "no") {
      box.style.backgroundColor = "red";
    } else if (elem.id == "yes") {
      box.style.backgroundColor = "green";
    } else {
      box.style.backgroundColor = "purple";
    };
};