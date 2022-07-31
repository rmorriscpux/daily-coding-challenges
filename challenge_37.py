'''
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

def powerSet(input_set):
    # NOTE: Python does not allow sets as items within sets. Therefore the power set is being constructed as a list.
    # First, set up list with empty set, then sets of individual items in the input_set.
    power_set = [set()]
    for item in input_set:
        power_set.append({item})

    # Now make set unions until all unique subsets are added.
    i = 1 # Skip the first index; i.e. the empty set, as it will not contribute.
    while i < len(power_set):
        for j in range(i, len(power_set)):
            u = power_set[i].union(power_set[j])
            # Add only if the union was not already added.
            if u not in power_set:
                power_set.append(u)
        # Increment
        i += 1

    return power_set

print(powerSet({1, 2, 3}))
print(powerSet({1, 2, 3, 4}))