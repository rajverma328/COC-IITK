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

// Fetch Data from JSON file
async function fetchCourseData() {
    try {
        const response = await fetch('/ASSETS/courses.json'); // Path to courses.json
        const data = await response.json();
        populateBranchDropdown(data);
    } catch (error) {
        console.error('Error fetching the course data:', error);
    }
}

// Populate Branch Dropdown
function populateBranchDropdown(data) {
    const branchSelect = document.getElementById('branch-select');
    const branches = Object.keys(data);

    branches.forEach(branch => {
        const option = document.createElement('option');
        option.value = branch;
        option.textContent = branch;
        branchSelect.appendChild(option);
    });

    // Add event listener to load courses when a branch is selected
    branchSelect.addEventListener('change', (event) => {
        const selectedBranch = event.target.value;
        populateCourseDropdown(data[selectedBranch]);
    });
}

// Populate Course Dropdown
function populateCourseDropdown(courses) {
    const courseSelect = document.getElementById('course-select');
    courseSelect.innerHTML = ''; // Clear previous options
    courseSelect.disabled = false; // Enable the course dropdown

    // Add an initial option
    const initialOption = document.createElement('option');
    initialOption.value = '';
    initialOption.textContent = 'Select Course';
    courseSelect.appendChild(initialOption);

    // Populate course options
    if (courses) {
        courses.forEach(course => {
            const option = document.createElement('option');
            option.value = course;
            option.textContent = course;
            courseSelect.appendChild(option);
        });
    } else {
        // If no courses, disable the dropdown
        courseSelect.disabled = true;
    }
}

// Initialize the application
fetchCourseData();
