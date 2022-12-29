'''
You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, "count": 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, "count": 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty, i.e. with 0 people inside.
'''

from typing import List

def findBusiestTime(entries: List[dict]):
    # Order list by timestamp.
    entries.sort(key=lambda entry: entry['timestamp'])

    current_people_count = 0
    max_people_count = 0

    start, end = None, None
    max_flag = False

    for entry in entries:
        if entry['type'] == "enter":
            current_people_count += entry['count']
        else: #entry['type'] == "exit"
            current_people_count -= entry['count']

        if current_people_count < 0:
            raise ValueError("Cannot have negative people count.")

        if max_flag == True and current_people_count < max_people_count:
            end = entry['timestamp']
            max_flag = False

        if current_people_count > max_people_count:
            start = entry['timestamp']
            max_people_count = current_people_count
            max_flag = True

    return start, end

entries = [
    {'timestamp': 1526579928, 'count': 3, 'type': "enter"},
    {'timestamp': 1526579928 + 100, 'count': 2, 'type': "exit"},
    {'timestamp': 1526579928 + 200, 'count': 1, 'type': "enter"},
    {'timestamp': 1526579928 + 300, 'count': 3, 'type': "enter"},
    {'timestamp': 1526579928 + 400, 'count': 5, 'type': "exit"},
]

print(findBusiestTime(entries))