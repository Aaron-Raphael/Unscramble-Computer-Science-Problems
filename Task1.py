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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# Define function to return number of unique numbers
def get_unique_numbers():

    # Initialize a set to find unique numbers
    unique_nums = set()

    # Get combined unique sender and receiver numbers from text.csv
    for record in texts:
        for i in (0 , 1):
            unique_nums.add(record[i])

    # Get combined unique calller and receiver numbers from calls.csv
    for record in calls:
        for i in (0 , 1):
            unique_nums.add(record[i])
    
    return len(unique_nums)

result = get_unique_numbers()

print(f"\nThere are {result} different telephone numbers in the records.")