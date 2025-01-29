from ics import Calendar, Event
from datetime import datetime
import csv
import arrow

def csv_to_ics(csv_path, ics_path):
    c = Calendar()

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        next(reader)  # Skip the header row
        for row in reader:
            e = Event()
            e.name = row[0]
            e.description = row[1]
            e.location = row[2]
            e.uid = row[3]
            if row[4]:  # If there is a start time
                start_time = arrow.get(row[4], "YYYY-MM-DD").replace(hour=9, minute=0)
                e.begin = start_time
                e.end = datetime.strptime(row[6], date_format) if row[6] else start_time.shift(hours=1)
            else:  # If there is no start time, create an all-day event
                start_date = arrow.get(row[4], "YYYY-MM-DD").date()
                e.begin = start_date
                e.end = arrow.get(row[6], "YYYY-MM-DD").shift(days=1).date() if row[6] else start_date.shift(days=1).date()
            c.events.add(e)

    with open(ics_path, 'w') as my_file:
        my_file.writelines(c)

date_format = "%Y-%m-%d %H:%M:%S"
csv_to_ics('my_input2.csv', 'my_output2.ics')