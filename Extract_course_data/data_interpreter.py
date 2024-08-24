from datetime import datetime
import pandas as pd
import numpy as np

#### CODE TO CALCULATE CLASS DURATION ####
def calculate_duration(start_time, end_time):
    """Calculate the duration between start and end times."""
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    duration = end - start
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, _ = divmod(remainder, 60)
    return f"({int(hours)}.{int(minutes / 15)})"  # Rounded to nearest quarter-hour

def clean_time_entry(entry):
    """Clean and format a time entry string."""
    if pd.isna(entry) or entry.lower() == 'nan':
        return None

    # Split the entry by spaces and process each part
    parts = entry.split()
    
    if len(parts) < 3:
        return None
    
    # Extract day and time range
    day = parts[0]
    time_range = parts[-1]  # Last part should be the time range
    
    if '-' in time_range:
        start_time, end_time = time_range.split('-')
        duration = calculate_duration(start_time, end_time)
        return f"{day} ({start_time}-{end_time}) {duration}"
    else:
        return None

def process_times(row):
    """Process and format times from the row."""
    times = [clean_time_entry(row[col]) for col in ['Time', 'Time.1', 'Time.2']]
    
    # Initialize a dictionary to track days and their corresponding times
    days = {
        'M': 'null',
        'T': 'null',
        'W': 'null',
        'Th': 'null',
        'F': 'null'
    }
    
    for time in times:
        if time:
            parts = time.split(' ', 1)
            if len(parts) == 2:
                day = parts[0]
                details = parts[1]
                if day in days:
                    days[day] = details
    
    # Format the output
    formatted_output = ', '.join(days[day] if days[day] != 'null' else 'null' for day in ['M', 'T', 'W', 'Th', 'F'])
    return formatted_output


def interpret_data(df):
    #### Managing Credits Column in Data Frame ####
    # Drop rows with any missing values
    df = df.drop_duplicates()  # Remove duplicate rows
    # Extract Credits as integers from the format '0-0-0-0(3)'
    df['Credits'] = df['Credits'].str.extract(r'\((\d+)\)')
    # Handle NaN values before conversion
    df['Credits'] = df['Credits'].fillna(0)  # Replace NaN with 0
    df['Credits'] = df['Credits'].astype(int)  # Convert to integer
    # Apply the processing function to each row
    df['Schedule'] = df.apply(process_times, axis=1)
    # Drop original columns if needed
    df = df.drop(columns=['Time', 'Time.1', 'Time.2'])
    #### Managing Credits Column in Data Frame ####
    return df

if __name__ == "__main__":
    print("NOT FOR THIS PURPOSE")
    ## DEV TOOLS
    data = {
    'Course Name/Group Name': ['Test Course'],
    'Credits': ['0-0-0-0(3)'],
    'Time': ['M (EEM117) W (EEM117) F (EEM117) 17:00-18:00'],
    'Time.1': ['T (EEM117) 09:00-10:00'],
    'Time.2': ['nan']
    }
    df = pd.DataFrame(data)
    output = interpret_data(df)
    print(output)
    print('..............................')
    print(output['Schedule'][0])
    # interpret_data(data)