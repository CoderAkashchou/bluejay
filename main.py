import pandas as pd
from datetime import timedelta

file_path = 'Assignment_Timecard.csv'
data = pd.read_csv(file_path)


def is_within_range(value, lower, upper):
    return lower <= value <= upper


for index, row in data.iterrows():
    start_time = pd.to_datetime(row['start_time'])
    end_time = pd.to_datetime(row['end_time'])
    duration = end_time - start_time

    if duration >= timedelta(days=7):
        print(f"Employee: {row['name']}, Position: {row['position']}, Condition: Worked for 7 consecutive days")

    if is_within_range(duration, timedelta(hours=1), timedelta(hours=10)):
        print(f"Employee: {row['name']}, Position: {row['position']}, Condition: Less than 10 hours between shifts but greater than 1 hour")

    if duration >= timedelta(hours=14):
        print(f"Employee: {row['name']}, Position: {row['position']}, Condition: Worked for more than 14 hours in a single shift")


