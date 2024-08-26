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

function deleteDivs(liId) {
    // Get the <li> element by its ID
    var liElement = document.getElementById(liId);
    // Check if the <li> element exists
    if (liElement) {
        // Select all div elements inside the <li> element
        var divs = liElement.querySelectorAll('div');
        // Iterate over each div and remove it
        divs.forEach(function(div) {
            if (div !== liElement.querySelector('.name')) {
                div.remove();
            }
        });
    }
}

function reset_button() {
    // Reset the branch dropdown to the default option
    document.getElementById("branch-select").selectedIndex = 0;
    // Disable and reset the course dropdown to the default option
    const courseSelect = document.getElementById("course-select");
    deleteDivs('M')
    deleteDivs('T')
    deleteDivs('W')
    deleteDivs('Th')
    deleteDivs('F')
    courseSelect.selectedIndex = 0;
    courseSelect.disabled = true;
}
function extractBracketContent(optionValue) {
    const matches = [...optionValue.matchAll(/\(([^)]+)\)/g)];
    // Return the last match if it exists
    return matches.length > 0 ? matches[matches.length - 1][1] : null;
}

async function fetchCourseSchedule(course) {
    try {
        const url = `/API/schedule/${course}`; // Construct the URL
        // console.log(url); // Log the constructed URL for debugging
        const response = await fetch(url);
        // console.log(response)
        const data = await response.json();
        return data
    } catch (error) {
        console.error('Error fetching the course schedule data:', error);
        return null
    }
}

function add_to_timetable(day_id, schedule, course, class_type, credits, class_color){
    if(schedule != "null"){
        var dayElement = document.getElementById(day_id);
        const newDiv = document.createElement('div');
        newDiv.className = 'hour' + ' ' + schedule + ' ' + class_color;
        newDiv.innerHTML = `<div class="title">${course}</div> <div>${class_type} [${credits}]</div>`
        dayElement.appendChild(newDiv);
    }
}

function iterateAndCheckClashes(inputDiv) {
    // Get all direct child divs of the inputDiv
    inputDiv = document.getElementById(inputDiv)
    let childDivs = inputDiv.querySelectorAll(':scope > div');
    
    // Iterate over each div
    for (let i = 0; i < childDivs.length; i++) {
        for (let j = i + 1; j < childDivs.length; j++) {
            if (isOverlapping(childDivs[i], childDivs[j])) {
                childDivs[i].classList.add("clash");
                childDivs[j].classList.add("clash");
                childDivs[j].classList.add("width_clash");
            }
        }
    }
}

// Function to check if two divs are overlapping
function isOverlapping(div1, div2) {
    const rect1 = div1.getBoundingClientRect();
    const rect2 = div2.getBoundingClientRect();

    return !(rect1.right < rect2.left + 2 ||  // Add 1px offset to the right comparison
        rect1.left > rect2.right - 2 ||  // Subtract 1px offset from the left comparison
        rect1.bottom < rect2.top + 2 ||  // Add 1px offset to the bottom comparison
        rect1.top > rect2.bottom - 2);   // Subtract 1px offset from the top comparison
}

async function add_button(){
    const courseSelect = document.getElementById("course-select");
    // console.log(extractBracketContent(courseSelect.value))
    const secourse = extractBracketContent(courseSelect.value);
    const schedule = await fetchCourseSchedule(secourse);
    lec = schedule[0];
    tut = schedule[1];
    lab = schedule[2];
    credits = schedule[3];

    if (lec != "null"){
        for (const key in lec) {
            if (lec.hasOwnProperty(key)) {
                // console.log(`${key}: ${lec[key]}`);
                add_to_timetable(key, lec[key], secourse, "LEC", credits, "normal_lec");
            }
        }
    }
    console.log("...................................")
    if (tut != "null"){
        for (const key in tut) {
            if (tut.hasOwnProperty(key)) {
                // console.log(`${key}: ${tut[key]}`);
                add_to_timetable(key, tut[key], secourse, "TUT", credits, "normal_tut");
            }
        }
    }
    console.log("...................................")
    if (lab != "null"){
        for (const key in lab) {
            if (lab.hasOwnProperty(key)) {
                // console.log(`${key}: ${lab[key]}`);
                add_to_timetable(key, lab[key], secourse, "LAB", credits, "normal_lab");
            }
        }
    }
    iterateAndCheckClashes("M")
    iterateAndCheckClashes("T")
    iterateAndCheckClashes("W")
    iterateAndCheckClashes("Th")
    iterateAndCheckClashes("F")
}