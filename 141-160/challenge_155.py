'''
Given a list of elements, find the majority element, which appears more than half the times (> floor(len(lst) / 2.0)).

You can assume that such an element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
'''

def getMajorityElement(element_list: list):
    element_count = {}
    threshold = len(element_list) // 2
    for e in element_list:
        if e not in element_count:
            element_count[e] = 0
        element_count[e] += 1
        if element_count[e] > threshold:
            return e
    return None

print(getMajorityElement([1, 2, 1, 1, 3, 4, 1]))