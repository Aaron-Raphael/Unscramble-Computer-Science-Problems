"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

with open('calls.csv', 'r') as call_rec:
    call_reader = csv.reader(call_rec)
    call_duration = {}

    for record in list(call_reader):

        # record[0]
        # record[1]
        # record[3]

        for i in (0 , 1):
            call_duration[record[i]] = call_duration[record[i]] + int(record[3]) if record[i] in call_duration else int(record[3])

# Find phone number of maximum call duration
maxCallNum = max(call_duration, key= lambda x: call_duration[x])

# Print output
print(f'\n{maxCallNum} spent the longest time, {call_duration[maxCallNum]} seconds, on the phone during September 2016.')