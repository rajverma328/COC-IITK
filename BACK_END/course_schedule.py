import pandas as pd

df = pd.read_json('../ASSETS/details.json')
course_code = df['Course Name/Group Name'].to_list()
def extract_last_bracket_content(course_name):
    # Find all occurrences of content in brackets
    brackets = []
    start = 0
    while True:
        start = course_name.find('(', start)
        if start == -1:
            break
        end = course_name.find(')', start)
        if end == -1:
            break
        brackets.append(course_name[start + 1:end])
        start = end + 1
    return brackets[-1] if brackets else None

# Apply the function to the 'Course Name/Group Name' column and convert to list
course_code = df['Course Name/Group Name'].apply(extract_last_bracket_content).to_list()

def get_schedule(course):
    try:
        index = course_code.index(course)
        print(f"The index of {course} is {index}.")
    except ValueError:
        print(f"{course} is not in the list.")
    sched_lec = df['lec'][index]
    sched_tut = df['tut'][index]
    sched_lab = df['lab'][index]
    return [sched_lec,sched_tut,sched_lab]

if __name__ == "__main__":
    print("NOT FOR THIS PURPOSE")
    ## DEV TOOLS
    get_schedule('EE380')