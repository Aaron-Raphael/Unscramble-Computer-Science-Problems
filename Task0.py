"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

with open('texts.csv', 'r') as text_rec:
    text_reader = csv.reader(text_rec)

    # Get and Unpack the first text record
    (sender, reciever, timestamp) = list(text_reader)[0]

    # Print the output
    print(f'\nFirst record of texts, {sender} texts {reciever} at time {timestamp}')
