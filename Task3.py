"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
"""

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

TASK 3:
(080) is the area code for fixed line teleph_numbers in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)
Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def number_type(ph_number):
    if ph_number[:5] == '(080)':
        return 'bangalore'
    elif ph_number[:3] == '140':
        return 'telemarketer'
    elif ph_number[:1] in ['7', '8', '9']:
        return 'mobile_number'
    else:
        return 'fixed_lines'

def area_code(calls):
    receiver_list = []
    codes = []  
    
    for call in calls:
        (caller, receiver) = call[:2]
        caller_type = number_type(caller)

        if caller_type == 'bangalore':
            receiver_list.append(receiver)
          
    for ph_number in receiver_list:
        if number_type(ph_number) == 'bangalore': 
            codes.append(ph_number[1:4])
        elif number_type(ph_number) == 'telemarketer': 
            codes.append(ph_number[:3])
        elif number_type(ph_number) == 'fixed_lines': 
            codes.append(ph_number.split('(', 1)[1].split(')')[0])
        else:
            codes.append(ph_number[:4]) # mobile: first 4 digits
    
    return codes



def from_to_percent(calls):
    from_count = 0         
    to_count = 0

    for call in calls:
        caller, receiver = call[0], call[1]
        caller_type = number_type(caller)
        receiver_type = number_type(receiver)

        if caller_type == 'bangalore':
            from_count += 1             # counter 

        if caller_type == 'bangalore' and receiver_type == 'bangalore': 
            to_count += 1   # counter 
    
    answer = to_count / from_count * 100
    percent = round(answer, 2)
    return percent


with open('calls.csv', 'r') as call_rec:
    call_reader = csv.reader(call_rec)
    calls = list(call_reader)

    codes = sorted(set(area_code(calls)))
    
    percent = from_to_percent(calls)

# Part A:
print('The numbers called by people in Bangalore have codes:')
for area_code in codes:
    print('\t' + area_code)

# Part B:
print(f'\n{percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')