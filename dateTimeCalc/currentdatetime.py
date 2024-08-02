import datetime
from datetime import timezone

# The current date and time
now = datetime.datetime.now()

# Getting just the current date
today = datetime.date.today()

# Turning July 4, 1776 as a datetime object
independence_day = datetime.date(1776, 7, 4)

# Turning 12:00 PM into a datetime object
# Note: This is a generic 12:00 PM time and has no date 
noon = datetime.time(12, 0, 0)

# Adding days to a date
tomorrow = today + datetime.timedelta(days=1)

# Calculating the difference between two dates
duration = tomorrow - today

# Formatting Date and Time
now = datetime.datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted)

# Parsing Date and Time Strings
date_string = "2021-04-30"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# UTC time
utc_time = datetime.datetime.now(timezone.utc)
print("UTC Time:", utc_time)