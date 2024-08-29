# [Extract_course_data Folder](Extract_course_data)

> [!IMPORTANT]
> This folder contains code for updating json data

## Files
### **`data_generator.py`**
This files contain the code that is called to read csv and update the json file, the code uses the packages `json`, `os`, `numpy`, `pandas` and `data_interpreter` defined below 
The key features of this code are:
- Designed to be called directly from bash
- Gives a interactive CLI interface to user asking a [Y/n] question
- Handle Dataframe objects and dumps in json where-ever required

### **`data_interpreter.py`**
This file act as a package to interpret data wherever required in the *data_generator.py* file, the code uses the packages `datetime`, `pandas` and `tqdm`. Defined inside are multiple functions that tackle the task of sgregating and making timetables, creating binaries for causes the concepts of which are explained in [BACK_END Folder](../BACK_END/)

> [!IMPORTANT]
> Each files contains a sample test case under the `if __name__ == "__main__":` condition for Developers if needed