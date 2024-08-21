###### IMPORTANT LIBRARIES ######
import csv
import json
import os
import pandas as pd


###### SEARCHING FOR READING CSV FILES ######
# Specify the directory you want to check
folder_path = './'

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
