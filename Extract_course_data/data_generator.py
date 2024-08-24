###### IMPORTANT LIBRARIES ######
import json
import os
import pandas as pd
import numpy as np
import data_interpreter as DI     # Custom defined shit

###### SEARCHING FOR READING CSV FILES ######
# Specify the directory you want to check

# IF RUNNING FROM VSCODE
# json_path = 'ASSETS/courses.json'
# folder_path = './'
# course_json_path = 'ASSETS/details.json'

# IF USING BASH
json_path = '../ASSETS/courses.json'
folder_path = '../'
course_json_path = '../ASSETS/details.json'

print('\033[31mWARNING:\033[0m Proceeding forward will cause deletion of existing data in json files')
user_input = input("Do you want to continue? [Y/n]: ").strip().lower()
# Handle the input
while(1):
    if user_input == 'y' or user_input == '':
        print("You chose to continue.")
        break
    elif user_input == 'n':
        print("You chose not to continue.")
        exit()
    else:
        print("Invalid input. Please enter 'Y' or 'n'.")

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
    exit()


###### READING CSV FILES ######
file_path = folder_path+files_found[0]
df = pd.read_csv(file_path)
# Display the headings of data
# print(df.columns.tolist())
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
print("Drop down menu updated in ./ASSETS/courses.json")
# Columns to extract
columns_to_extract = ['Course Name/Group Name', 'Credits', 'Time', 'Time.1', 'Time.2']
extracted_df = df[columns_to_extract]
# Saving the extracted data to a JSON file
print("printing head of data farme")
print(extracted_df.head())
print("...................................................")
extracted_df = DI.interpret_data(extracted_df)
extracted_df.to_json(course_json_path, orient='records', indent=4)
print(f"Data extracted and saved to ./ASSETS/details.json")
print("...................................................")
print("DATA UPDATES SUCCESFULLY")