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
    try:
        index = course_code.index(course)
        # print(f"The index of {course} is {index}.")
    except ValueError:
        print(f"{course} is not in the list.")
    sched_lec = df['lec'][index]
    sched_lec = get_class_string(sched_lec)

    sched_tut = df['tut'][index]
    sched_tut = get_class_string(sched_tut)

    sched_lab = df['lab'][index]
    sched_lab = get_class_string(sched_lab)

    credits = str(df['Credits'][index])

    # print(sched_lec)
    return [sched_lec,sched_tut,sched_lab,credits]

if __name__ == "__main__":
    print("NOT FOR THIS PURPOSE")
    ## DEV TOOLS
    get_schedule('EE380')