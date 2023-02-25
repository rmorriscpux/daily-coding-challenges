'''
You are given an array of length 24, where each element represents the number of new subscribers during the corresponding hour.
Implement a data structure that efficiently supports the following:

- update(hour: int, value: int): Increment the element at index hour by value.
- query(start: int, end: int): Retrieve the number of subscribers that have signed up between start and end (inclusive).
  You can assume that all values get cleared at the end of the day, and that you will not be asked for start and end values that wrap around midnight.
'''

class SubsPerHour:
    def __init__(self):
        self.subscriptions = [0] * 24

    def update(self, hour: int, value: int):
        assert 0 <= hour < 24

        self.subscriptions[hour] += value
        return self

    def query(self, start: int, end: int):
        assert 0 <= start < 24
        assert 0 <= end < 24
        assert start <= end

        return sum(self.subscriptions[start:end+1])