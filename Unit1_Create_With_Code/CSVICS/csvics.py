import csv
from ics import Calendar, Event
from datetime import datetime

# Define your date format
date_format = "%d/%m/%Y %H:%Maa"

def csv_to_ics(csv_file_name, ics_file_name):
    # Create a new calendar
    c = Calendar()

    # Open the CSV file
    with open(csv_file_name, newline='') as csvfile:
        #reader = csv.reader(csvfile, delimiter='\t')
        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # Skip the header

        # Loop through each row in the CSV file
        for row in reader:
            e = Event() # Create a new event
            e.name = row[0]
            e.begin = datetime.strptime(row[4], date_format) if row[4] else None
            e.end = datetime.strptime(row[4], date_format) if row[4] else None
            #e.end = datetime.strptime(row[6], date_format) if row[6] else None
            c.events.add(e) # Add the event to the calendar

    # Write the calendar to the ICS file
    with open(ics_file_name, 'w') as my_file:
        my_file.writelines(c)

# Convert a CSV file to an ICS file
csv_to_ics('my_input.csv', 'my_output.ics')
