# BACK_END Folder
The `BACK_END` folder contains the core backend scripts used for managing the application's functionality. Below is a description of the contents of this folder:

## Files
- **`app.py`**: This is the main application script responsible for handling the core backend operations and routing within the project.
- **`course_schedule_manager.py`**: Manages the logic related to course scheduling, including processing times, dates, and other relevant scheduling data.

## Clash Detection Logic
One of the core features of this project is the **clash detection** system, which ensures that no two classes overlap in a student's schedule. The logic behind this system is both efficient and straightforward, leveraging binary operations to handle scheduling conflicts.
### How It Works
1. **Time Segmentation:**
   - Each day from **8 AM to 9 PM** is divided into **15-minute segments**, resulting in **52 segments per day**.
   - These segments are represented in the `ASSETS/details.json` file, where each time slot is either **1** (if there's a class) or **0** (if no class is scheduled).

2. **Binary Representation:**
   - For each course, a **52-bit long integer** is generated, where each bit corresponds to a 15-minute segment of the day.
   - If a segment has a class, the bit is set to **1**; otherwise, it remains **0**.
   - This binary representation effectively maps out the entire daily schedule for a course in a compact form.

3. **Detecting Clashes:**
   - To detect potential clashes between selected courses, we use **bitwise AND** operations:
     - If the AND operation between two courses results in **0** for all bits, it means there is **no clash** (i.e., no overlapping segments) 🟢.
   - To compile a complete schedule from multiple courses, we use **bitwise OR** operations:
     - The OR operation combines the schedules of all selected courses, highlighting the entire occupied time slots across the day 📅.

### Why This Works
- **Efficiency:** ⚡ Binary operations are computationally light and fast, making this approach ideal for handling multiple courses and large datasets.
- **Simplicity:** 🧠 The 52-bit integer representation is a neat and straightforward way to encode an entire day's schedule, reducing complexity in both storage and processing.
- **Scalability:** 📈 As the number of courses increases, the clash detection logic scales seamlessly, maintaining quick and accurate results.

### Real-World Application
Imagine you're selecting courses for the upcoming semester. With this clash detection system, you can easily add courses to your list, and the system will instantly alert you if any of them overlap in time. Plus, it will generate a comprehensive daily schedule by merging all your selected courses 📚.

This powerful feature ensures that you can plan your academic schedule with confidence, avoiding any unexpected conflicts and making the most of your time ⏳.

By integrating this clash detection logic, the project not only helps in visualizing schedules but also ensures that your academic planning is both efficient and error-free. Enjoy seamless scheduling with this smart, binary-powered solution! 🚀



## Functions in `course_schedule_manager.py`
### `extract_last_bracket_content(course_name)`
- **Purpose:** Extracts the content inside the last pair of brackets from a course name.
- **Usage:** Applied to the 'Course Name/Group Name' column in a DataFrame to extract specific course codes.
- **Returns:** A string containing the content from the last brackets or `None` if no brackets are found.

### `get_class_string(arr)`
- **Purpose:** Converts class schedule data (lectures, tutorials, labs) into a specific string format that includes start time, duration, and offset for each day.
- **Usage:** Used within the `get_schedule` function to format class schedules.
- **Returns:** A dictionary where the keys are days and the values are formatted class strings.

### `get_schedule(course)`
- **Purpose:** Retrieves the complete schedule (lectures, tutorials, labs) for a specific course.
- **Usage:** Provides detailed scheduling information for a course including formatted lecture, tutorial, and lab timings, as well as credit information.
- **Returns:** A list containing the schedule for lectures, tutorials, labs, and the number of credits.

### `get_available_courses(selected_courses)`
- **Purpose:** Identifies and returns a list of courses that do not have any time conflicts with the selected courses.
- **Usage:** Takes a list of selected course codes and determines which other courses can be taken without scheduling conflicts.
- **Returns:** A JSON-formatted dictionary where keys represent course branches, and values are lists of available courses under each branch.

## API Endpoints
The backend is written in `app.py` using Python based flask for API managements having the following endpoints:
- ### Fetch Course Schedule
    - **Endpoint:** `/API/schedule/<course>`
    - **Method:** `GET`
    - **Description:** Retrieves the schedule for a specific course
- ### Available Courses
    - **Endpoint:** `/API/available`
    - **Method:** `GET`
    - **Description:** Returns available courses based on the selected ones
    - **Parameters:** `courses[]` - List of selected courses.
### Serving Static and Asset Files
- **Static Files:** The static files (HTML, CSS, JS) are served from the `FRONT_END` directory.
- **Assets:** Assets like images and fonts are served from the `ASSETS` directorsy.

> [!IMPORTANT]
> Each files contains a sample test case under the `if __name__ == "__main__":` condition for Developers if needed
