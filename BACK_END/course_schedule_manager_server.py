import pandas as pd
import json
import re 

# with open('../ASSETS/courses.json', 'r') as file: # change for bash execution
#     my_dict = json.load(file)
# keys = list(my_dict.keys())
# print(keys)

df = pd.read_json('ASSETS/details.json')
# df = pd.read_json('ASSETS/details.json')
course_code = df['Course Name/Group Name'].to_list()
course_name = course_code

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

unique_texts = set()
# Iterate through each course code
for code in course_code:
    # Use regular expression to find the text prefix
    match = re.match(r'([A-Za-z]+)', code)
    if match:
        text_prefix = match.group(1)
        unique_texts.add(text_prefix)
# Convert the set to a list (if needed) and print the result
keys = list(unique_texts)
keys = sorted(keys)
keys.insert(0, "Select Branch")
keys.insert(1, "All Branches")
# print(keys)

def get_class_string(arr):
    # print(arr)
    if arr=="null":
        return "null"
    output_dict = {}
    for day, value in arr.items():
        if value == 'null':
            output_dict[day] = 'null'
        else:
            # Extract time period and duration
            time_period, duration = value
            duration = duration.replace('.', '-')
            # Extract hour from time period
            start_time = time_period.split('-')[0]
            hour = start_time.split(':')[0]
            minute = start_time.split(':')[1]
            # Format as .hour__<hour> .hour--<duration> .hour-<--offset>
            formatted_value = f'hour__{hour} hour--{duration} hour-{int(minute)}'
            output_dict[day] = formatted_value
    return output_dict

def get_schedule(course):
    # print(course)
    try:
        index = course_code.index(course)
        # print(f"The index of {course} is {index}.")
    except ValueError:
        print(f"{course} is not in the list.")
    # print(index)
    sched_lec = df['lec'][index]
    sched_lec = get_class_string(sched_lec)

    sched_tut = df['tut'][index]
    sched_tut = get_class_string(sched_tut)

    sched_lab = df['lab'][index]
    sched_lab = get_class_string(sched_lab)

    credits = str(df['Credits'][index])

    # print(sched_lec)
    return [sched_lec,sched_tut,sched_lab,credits]

def get_available_courses(selected_coursers):
    available_courses= []
    M = 0
    T = 0
    W = 0
    Th = 0 
    F = 0
    for course in  selected_coursers:
        try:
            index = course_code.index(course)
            # print(f"The index of {course} is {index}.")
        except ValueError:
            print(f"{course} is not in the list.")
        M = M | df['M'][index]
        T = T | df['T'][index]
        W = W | df['W'][index]
        Th = Th | df['Th'][index]
        F = F | df['F'][index] 

    for index, tc in df.iterrows():
        if ((M & tc['M'])|(T & tc['T'])|(W & tc['W'])|(Th & tc['Th'])|(F & tc['F']) == 0):
            available_courses.append(tc['Course Name/Group Name'])
    available_courses_codes = list(map(extract_last_bracket_content, available_courses))
    return_dict = {}
    return_dict[keys[0]] = ""
    return_dict[keys[1]] = available_courses 
    for i in range(2, len(keys)):
        indices = [j for j, s in enumerate(available_courses_codes) if s.startswith(keys[i])]
        return_dict[keys[i]] = [available_courses[i] for i in indices]
    return_dict = json.dumps(return_dict)
    return return_dict

if __name__ == "__main__":
    print("NOT FOR THIS PURPOSE")
    ## DEV TOOLS
    # get_available_courses(['EE380'])
