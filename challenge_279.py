'''
A classroom consists of N students, whose friendships can be represented in an adjacency list.
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations.
In other words, this is the smallest set such that no student in the group has any friends outside this group.
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
'''

# Assumption: Input is a dictionary of lists. This can also be accomplished with a list of lists.

from typing import List, Dict

def friendGroups(adj_list: Dict[int, List[int]]):
    # Build a group of connected friends recursively
    def buildGroup(adj_list: Dict[int, List[int]], group: set, cur_index: int):
        for f in adj_list[cur_index]:
            if f not in group:
                # New person found. Add to group and check its friend list as it may have additional connections.
                group.add(f)
                buildGroup(adj_list, group, f)

        return
    # Check that the adjacency list is symmetrical.
    for key, friends in adj_list.items():
        for f in friends:
            if key not in adj_list[f]:
                raise ValueError("Friendship list is not symmetrical.")
    
    used = set()
    groups = []

    for key in adj_list.keys():
        if key not in used:
            # Create a new group starting with the current person. Ignore people already included in a group.
            new_group = set([key])
            buildGroup(adj_list, new_group, key)
            # Append the new group set to the groups list.
            groups.append(new_group)
            # Include all added to the new group to the used set, so they're not traversed again.
            used.update(new_group)

    return groups

classroom = {
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
}

print(friendGroups(classroom))