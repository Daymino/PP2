from datetime import datetime

# Input two date strings
date_str1 = input("(YYYY-MM-DD HH:MM:SS): ")
date_str2 = input("(YYYY-MM-DD HH:MM:SS): ")

# Convert the date strings to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")

# Calculate the time difference
time_difference = date2 - date1

# Extract the difference in seconds
difference_in_seconds = abs(time_difference.total_seconds())

# Print the result
print("Difference between the two dates in seconds:", difference_in_seconds)