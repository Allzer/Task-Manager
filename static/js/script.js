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

document.getElementById('dataToday').valueAsDate = new Date();

document.addEventListener('DOMContentLoaded', function() {
        var checkboxes = document.querySelectorAll('.task_checkbox');

        checkboxes.forEach(function(checkbox) {
            checkbox.addEventListener('change', function() {
                var taskTitle = this.parentElement.textContent.trim();
                var taskElement = this.parentElement;

                if (this.checked) {
                    taskElement.style.textDecoration = 'line-through';
                } else {
                    taskElement.style.textDecoration = 'none';
                }
            });
        });
    });


















