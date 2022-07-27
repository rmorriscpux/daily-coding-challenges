'''
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

    2
    1.5
    2
    3.5
    2
    2
    2
'''

# Using list sort() method.
def runningMedianSort(num_list):
    for i in range(1, len(num_list) + 1):
        sub_list = num_list[0:i]
        sub_list.sort()
        half = i // 2
        median = (sub_list[half] + sub_list[half-1]) / 2 if i % 2 == 0 else sub_list[half]
        print(median)
    return

# Not using list sort() method. Define custom quickSort() function.
def quickSort(num_list):
    if len(num_list) == 1:
        return num_list

    pivot_index = len(num_list) // 2
    ptr_index = 0
    
    while ptr_index < pivot_index:
        if num_list[ptr_index] > num_list[pivot_index]:
            num_list.append(num_list.pop(ptr_index))
            pivot_index -= 1
        else:
            ptr_index += 1

    ptr_index = pivot_index + 1
    while ptr_index < len(num_list):
        if num_list[ptr_index] < num_list[pivot_index]:
            num_list.insert(0, num_list.pop(ptr_index))
            pivot_index += 1
        ptr_index += 1

    sorted_list = []
    if pivot_index > 0:
        sorted_list.extend(quickSort(num_list[:pivot_index]))
    sorted_list.append(num_list[pivot_index])
    if pivot_index < len(num_list) - 1:
        sorted_list.extend(quickSort(num_list[pivot_index+1:]))

    return sorted_list

def runningMedian(num_list):
    for i in range(1, len(num_list) + 1):
        sub_list = quickSort(num_list[0:i])
        half = i // 2
        median = (sub_list[half] + sub_list[half-1]) / 2 if i % 2 == 0 else sub_list[half]
        print(median)
    return

runningMedianSort([2, 1, 5, 7, 2, 0, 5])
print('-----')
runningMedian([2, 1, 5, 7, 2, 0, 5])