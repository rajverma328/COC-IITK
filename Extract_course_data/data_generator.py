###### IMPORTANT LIBRARIES ######
import csv
import json
import os
import pandas as pd


###### SEARCHING FOR READING CSV,XLS,XLSX FILES ######
# Specify the directory you want to check
folder_path = './'

# List to store found files
files_found = []

# Iterate over all files in the folder
for file_name in os.listdir(folder_path):
    if file_name.endswith(('.csv', '.xlsx', '.xls')):
        files_found.append(file_name)

# Output the results
if files_found:
    print(f"Files found: {', '.join(files_found)}")
    if len(files_found) > 1:
        print("since the folder contains multiple readable fromat files please delete old ones")
else:
    print("No CSV, XLSX, or XLS files found in the folder.")



file_path = folder_path+files_found[0]
df = pd.read_excel(file_path)
# Display the data
print(df.head())