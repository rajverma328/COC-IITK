# COC-IIT-K: Clash Of Courses - IIT Kanpur

<div align="center">
  <img src="FRONT_END/name.svg" alt="Prefer Dark Mode Please" width="400"/>
</div>

Welcome to **COC-IIT-K**, short for *Clash Of Courses IIT Kanpur*, a web application designed to streamline and simplify your course timetable management. Whether you're dealing with course conflicts or just trying to keep your schedule organized, this tool provides an intuitive interface to help you manage your academic life at IIT Kanpur.

## Description

**COC-IIT-K** is a powerful tool designed to help IIT Kanpur students efficiently create their academic schedules. 🎓 It offers an intuitive and user-friendly website 🌐 that automatically navigates through over 700+ courses 📚 across 20+ departments, ensuring that none of the selected courses clash with the user's existing schedule. ⏰ Built with a Flask backend, 🐍 **COC-IIT-K** provides comprehensive course coverage, handling all available courses without exceptions, making the scheduling process seamless and stress-free. 🎉

**`MOTIVATION`**: At IIT Kanpur, the heavy emphasis on competitive programming often sidelines real coding, creating an isolating environment. To navigate this, I turned to my side project, **COC-IIT-K**. This endeavor allows me to channel my passion for coding into something valuable for my peers, reminding me that coding is about creativity and problem-solving, not just competition.

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/rajverma328/COC-IITK.git
```
It is optimised to run with debugging off on your local server, you can change by modiying [app.py](BACK_END/app.py)

### 2. Prepare Course CSV
Please follow the steps mentioned here to procure the course data from [here](Extract_course_data/README.md) and place it in the cloned repository

### 3. Run the Server
```bash
bash update_and_launch.sh
```
Run the above code to update the .json files and view the web-app work on `http://127.0.0.1:5000/` 

## Project Structure

```

COC-IIT-K  
│  
├── ASSETS/  
│   ├── courses.json  
│   ├── details.json  
│   └── README.md  
│  
├── BACK_END/  
│   ├── app.py  
│   ├── check_clash.py  
│   ├── course_schedule.py  
│   └── README.md  
│  
├── Extract_course_data/  
│   ├── data_generator.py  
│   ├── data_interpreter.py  
│   └── README.md  
│  
├── FRONT_END/  
│   ├── index.html  
│   ├── styles.css  
│   ├── scripts.js  
│   ├── (OTHER_OBJECTS)                 # images & stuff  
│   └── README.md  
│  
├── RECOMMENDATION/  
│   └── README.md  
│  
├── Playground/  
│   ├── test.html  
│   └── README.md  
│  
├── LICENSE
├── Course_schedule_from_pingala.csv    # CSV taken from Pingala
├── updata_data.sh                      # Called to update
└── README.md                           # This README file

```
### [ASSETS Folder](ASSETS)
The `ASSETS` folder contains important JSON files used for managing course data in the repository. Below is a description of the contents of this folder:
#### Files
- **`courses.json`**: This file includes course information categorized by branch. It organizes courses based on different branches, making it easier to manage and access courses specific to each branch.
- **`details.json`**: This file contains detailed information about the courses, such as time, credits, and other relevant details. It provides a comprehensive overview of each course, including additional attributes that are important for course management and scheduling.

- You can view or download these files directly using the links below:
  - [courses.json](ASSETS/courses.json)
  - [details.json](ASSETS/details.json)

---
### [BACK_END Folder](BACK_END)
The `BACK_END` folder contains the core backend scripts used for managing the application's functionality. Below is a description of the contents of this folder:

#### Files
- **`app.py`**: This is the main application script responsible for handling the core backend operations and routing within the project.
- **`check_clash.py`**: This script is used to check for scheduling conflicts between courses. It ensures that no two courses overlap in timing.
- **`course_schedule.py`**: Manages the logic related to course scheduling, including processing times, dates, and other relevant scheduling data.

- You can view or download these files directly using the links below:
  - [app.py](BACK_END/app.py)
  - [check_clash.py](BACK_END/check_clash.py)
  - [course_schedule.py](BACK_END/course_schedule.py)

---
### [Extract_course_data Folder](Extract_course_data)

> [!IMPORTANT]
> This folder contains code for updating json data

#### Files
- **`data_generator.py`**: This files contain the code that is called to read csv and update the json file.
- **`data_interpreter.py`**: This file act as a package to interpret data wherever required in the *data_generator.py* file.

- You can view or download these files directly using the links below:
  - [data_generator.py](Extract_course_data/data_generator.py)
  - [data_interpreter.py](Extract_course_data/data_interpreter.py)

---
### [FRONT_END Folder](FRONT_END)
The `FRONT_END` folder contains all the essential files for the frontend of the project. Below is a detailed description of each item in this folder:
#### Files
- **`index.html`**: The main HTML file for the project. This file serves as the entry point for the application, defining the structure and content of the web page.
- **`styles.css`**: The CSS file used for styling the HTML content. It includes all the styles and design elements that determine the visual appearance of the web page.
- **`scripts.js`**: The JavaScript file that contains the logic and functionality for the frontend. It handles interactions, dynamic content, and other client-side behaviors.
- **`(OTHER_OBJECTS)`**: This directory includes various assets such as images, icons, and other resources used in the frontend. It is organized to keep the media files separate from the core HTML, CSS, and JavaScript files.

- You can view or download these files directly using the links below:
  - [index.html](FRONT_END/index.html)
  - [styles.css](FRONT_END/styles.css)
  - [scripts.js](FRONT_END/scripts.js)
  - [Other assets](FRONT_END)

---
### [RECOMMENDATION Folder](RECOMMENDATION)

---
### [Playground Folder](Playground) 
The `PLAYGROUND` folder is your experimental space 🚀! It's where all the magic happens, from major milestones to all the little tweaks and fidgeting along the way. Whether it's testing new ideas, refining features, or just having some fun with code, this is where creativity meets functionality. Dive in to see the journey, trials, and triumphs that have shaped the project!🎨🔧

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
