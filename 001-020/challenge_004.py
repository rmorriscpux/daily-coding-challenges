'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''
# NOTE: Python has a built-in sort function for lists, but I thought for an extra challenge I'd put in a merge sort from scratch.
#       The actual find lowest positive integer function begins on line 53.

# Function to split the list into individual single item lists, grouped binarily
def split_list(input_list):
    # At the end, return singular item list.
    if len(input_list) == 1:
        return input_list

    # Split the list recursively until we reach lists of 1.
    output_list = [split_list(input_list[:len(input_list)//2]), split_list(input_list[len(input_list)//2:])]

    return output_list

def merge_sort(list_1, list_2):
    sorted_list = []
    # Compare the first element from each list. Each list should be pre-sorted.
    while (len(list_1) != 0 and len(list_2) != 0):
        if list_1[0] < list_2[0]:
            sorted_list.append(list_1.pop(0))
        else:
            sorted_list.append(list_2.pop(0))

    # Catch any leftovers and clean up
    for i in list_1:
        sorted_list.append(i)
    for j in list_2:
        sorted_list.append(j)
    list_1.clear()
    list_2.clear()

    return sorted_list

# input_list is a list of single-integer lists. (e.g. [[6], [3], [5], [20]]). Can be output from split_list() above.
def full_merge_sort(split_list):
    if len(split_list[0]) > 1:
        split_list[0] = full_merge_sort(split_list[0])

    if len(split_list[1]) > 1:
        split_list[1] = full_merge_sort(split_list[1])

    return merge_sort(split_list[0], split_list[1])

def find_lowest_positive_integer(input_list):
    if len(input_list) == 0:
        return 1

    sorted_list = full_merge_sort(split_list(input_list))

    # Get rid of all negative integers
    while (sorted_list[0] < 0):
        sorted_list.pop(0)
        if len(sorted_list) == 0: #All numbers are gone from list. Return 1
            return 1
    
    # Check the first integer in the list. If it's greater than 1, then 1 is the lowest positive.
    if sorted_list[0] > 1:
        return 1

    # Go through the list to find the lowest positive.
    for i in range(1, len(sorted_list)):
        # End condition: Current integer is not the same or +1 as the integer before it.
        if sorted_list[i] > sorted_list[i-1] + 1:
            return sorted_list[i-1] + 1

    # At this point, we learned that all the numbers are sequential. Returned the last number in the list + 1.
    return sorted_list[len(sorted_list)-1] + 1

print(find_lowest_positive_integer([1, 2, 0]))
print(find_lowest_positive_integer([3, 4, -1, 1]))
print(find_lowest_positive_integer([3, 4, -1, 1, 2, 3, 4]))