# ASSETS Folder
Welcome to the ASSETS folder, the heart of our data-driven project! This folder is where all the essential JSON files live, powering the core functionalities of our application. Below is a quick tour of what you'll find inside:

## Files Overview
### **`courses.json`** 
This file includes course information categorized by branch. It organizes courses based on different branches, making it easier to manage and access courses specific to each branch. This contain the branch wise courses and is made in a following structure:
```json
{
     "All Branches": ["array of ',' seperated courses of all branches"],
     "AE": ["array of ',' seperated courses of AE branches"],
     "BSBE": ["array of ',' seperated courses of AE branches"],
     .
     .
     .
     // AND REST BRANCHES
}
```

### **`details.json`**
This file contains detailed information about the courses, such as time, credits, and other relevant details. It provides a comprehensive overview of each course, including additional attributes that are important for course management and scheduling. This contain the branch wise courses and is made in a following structure:
```json
[
    {
        "Course Name\/Group Name":"COURSE NAME(COURSE CODE)",
        "Credits":5,
        "lec":{
            "M":"null", // if no class present
            "T":["lec time and duration"], // EX: []"08:00-09:00", "1.0"]
            "W":["lec time and duration"],
            "Th":["lec time and duration"],
            "F":["lec time and duration"]
        },
        "tut":"null", // if no lab or tut
        "lab":"null",
        "M":1030792151040, // binary of course for easy computation
        "T":0,
        "W":1030792151040,
        "Th":0,
        "F":1030792151040
    },
    .
    .
    .
    // AND REST COURSES
]
```
> [!IMPORTANT]
> More on generation of course day binaries can be found in [BACK_END Folder](BACK_END)