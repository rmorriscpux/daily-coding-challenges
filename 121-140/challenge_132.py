'''
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
'''

from datetime import datetime

class HitCounter:
    def __init__(self):
        self._hit_log = []

    def record(self, timestamp: datetime):
        self._hit_log.append(timestamp)
        return

    def total(self):
        return len(self._hit_log)

    def range(self, lower: datetime, upper: datetime):
        if lower > upper:
            return 0

        lower_bound = 0
        while self._hit_log[lower_bound] < lower and lower_bound < len(self._hit_log):
            lower_bound += 1

        if lower_bound == len(self._hit_log):
            return 0

        upper_bound = len(self._hit_log) - 1
        while self._hit_log[upper_bound] > upper and upper_bound >= 0:
            upper_bound -= 1

        if upper_bound == -1:
            return 0

        return len(self._hit_log[lower_bound:upper_bound+1])

hc = HitCounter()
for i in range(1, 21):
    hc.record(datetime(2022, 11, i, 12, 15, 20, 12345))

print(hc.total())
print(hc.range(datetime(2022, 11, 5, 0, 0, 0, 0), datetime(2022, 11, 15, 21, 0, 0, 0)))