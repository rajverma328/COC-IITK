// This can be used to add interactivity later
console.log("Timetable loaded successfully!");

const checkbox = document.getElementById("rc_switch");
const element_orient = document.getElementById("orienter");
function toggleClass(){
    if (checkbox.checked) {
        element_orient.classList.add("toggle0");
        element_orient.classList.remove("toggle1");
    } else {
        element_orient.classList.add("toggle1");
        element_orient.classList.remove("toggle0");
    }
}

function checkDocumentWidth() {
    if (window.innerWidth < 1300) {
        checkbox.checked = false;
        element_orient.classList.add("toggle1");
        element_orient.classList.remove("toggle0");
    }
}

// Run the function on window resize and when the page loads
window.addEventListener('resize', checkDocumentWidth);
window.addEventListener('load', checkDocumentWidth);