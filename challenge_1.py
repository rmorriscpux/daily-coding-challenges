'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def sum_to_k(num_list, k):
    # Keep input clean.
    if not isinstance(num_list, list):
        return False
    if not all(list(map(lambda n: type(n) == (int or float), num_list))):
        return False
    if type(k) != (int or float):
        return False

    # Search for suitable sums.
    for i in range(0, len(num_list)-1):
        for j in range(i+1, len(num_list)):
            if num_list[i] + num_list[j] == k:
                # Sum found.
                return True

    # No sum found in list. Return here.
    return False

print(sum_to_k([10, 15, 3, 7], 17)) #True
print(sum_to_k([10, 15, 3, 7], 18)) #True
print(sum_to_k([10, 15, 3, 7], 19)) #False
print(sum_to_k([10, 15, 3, 7], 10)) #True
print(sum_to_k([10, 15, 3, 7], 15)) #False
print(sum_to_k([10.1, 15, 3, 6.9], 17)) #True
print(sum_to_k([10, -15.78, 3, -6], 4)) #True
print(sum_to_k([10, 15, 'Hi!', 7], 18)) #False