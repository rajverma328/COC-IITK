# COC-IIT-K: Clash Of Courses - IIT Kanpur

<div align="center">
  <img src="FRONT_END/name.png" alt="Prefer Dark Mode Please" width="400"/>
</div>

Welcome to **COC-IIT-K**, short for *Clash Of Courses IIT Kanpur*, a web application designed to streamline and simplify your course timetable management. Whether you're dealing with course conflicts or just trying to keep your schedule organized, this tool provides an intuitive interface to help you manage your academic life at IIT Kanpur.

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
│   ├── (OTHER_OBJECTS)  # images & stuff  
│   └── README.md  
│  
├── RECOMMENDATION/  
│   └── README.md  
│  
├── Playground/  
│   ├── test.html  
│   └── README.md  
│  
└── README.md  # This README file

```
### [ASSETS Folder](ASSETS)
The `ASSETS` folder contains important JSON files used for managing course data in the repository. Below is a description of the contents of this folder:
#### Files
- **`courses.json`**: This file includes course information categorized by branch. It organizes courses based on different branches, making it easier to manage and access courses specific to each branch.
- **`details.json`**: This file contains detailed information about the courses, such as time, credits, and other relevant details. It provides a comprehensive overview of each course, including additional attributes that are important for course management.
- You can view or download these files directly using the links below:
  - [courses.json](ASSETS/courses.json)
  - [details.json](ASSETS/details.json)
---

### [BACK_END](BACK_END)
---

### [Extract_course_data](Extract_course_data)

> [!NOTE]
> This folder contains code for updating json data

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

### [RECOMMENDATION](RECOMMENDATION)
---

### [Playground](Playground)
---