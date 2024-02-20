document.getElementById("addButton").addEventListener("click", function() {
    var form = document.getElementById("addtask");
    if (form.style.display === "none") {
        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
});

document.getElementById("myTextarea").addEventListener("input", function() {
    this.style.height = "auto";
    this.style.height = (this.scrollHeight) + "px";
});
