###### IMPORTANT LIBRARIES ######
import json
import os
import pandas as pd
import numpy as np
import data_interpreter as DI     # Custom defined shit

###### SEARCHING FOR READING CSV FILES ######
# Specify the directory you want to check

# IF RUNNING FROM VSCODE
json_path = 'ASSETS/courses.json'
folder_path = './'
course_json_path = 'ASSETS/details.json'

# IF USING BASH
if __name__ == "__main__":
    print("FOLLOW THE STEPS IN README PLEASE")
# json_path = '../ASSETS/courses.json'
# folder_path = '../'
#course_json_path = '../ASSETS/details.json'

# List to store found files
files_found = []

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        files_found.append(file_name)

# Output the results
if files_found:
    print(f"Files found: {', '.join(files_found)}")
    if len(files_found) > 1:
        print("since the folder contains multiple readable fromat files please delete old ones")
else:
    print("No CSV files found in the folder.")


###### READING CSV FILES ######
file_path = folder_path+files_found[0]
df = pd.read_csv(file_path)
# Display the headings of data
print(df.columns.tolist())
col_name = df.columns.tolist()

branch_name = df['Br'].unique()
branch_name = np.append(['All Branches'], branch_name)
branch_name = branch_name.tolist()
print("Branch names extracted succesfully")

# Grouping courses by department
branches_grouped = df.groupby('Br')['Course Name/Group Name'].apply(list).to_dict()
courses = {'All Branches': df['Course Name/Group Name'].tolist(), **branches_grouped}
with open(json_path, 'w') as json_file:
    json.dump(courses, json_file, indent=4)

# Columns to extract
columns_to_extract = ['Course Name/Group Name', 'Credits', 'Time', 'Time.1', 'Time.2']
extracted_df = df[columns_to_extract]
# Saving the extracted data to a JSON file
extracted_df = DI.interpret_data(extracted_df)
# pd.set_option("display.max_columns", None)
print(extracted_df)

extracted_df.to_json(course_json_path, orient='records', indent=4)
print(f"Data extracted and saved to {course_json_path}")