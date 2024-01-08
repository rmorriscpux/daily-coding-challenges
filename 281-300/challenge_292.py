'''
A teacher must divide a class of students into two teams to play dodgeball. Unfortunately, not all the kids get along,
and several refuse to be put on the same team as that of their enemies.

Given an adjacency list of students and their enemies, write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}
On the other hand, given the input below, you should return False.

students = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}
'''

from typing import NamedTuple

class Team(NamedTuple):
    members: set
    enemies: set

def validateAdjacencyList(students: dict[int, list[int]]) -> bool:
    for s, e_list in students.items():
        if s in e_list:
            return False
        for e in e_list:
            if not(e in students and s in students[e]):
                return False
    return True

def teamPair(students: dict[int, list[int]]) -> tuple[set[int], set[int]] | bool:
    # Optional check for valid adjacency list. (see above)
    if not validateAdjacencyList(students): raise ValueError("Student adjacency list not valid.")
    # Instantiate teams.
    team_1 = Team(members=set(), enemies=set())
    team_2 = Team(members=set(), enemies=set())
    # Split students into teams based on whether or not an enemy is already on that team.
    for student, e_list in students.items():
        if not(team_1.members and student in team_1.enemies):
            team_1.members.add(student)
            team_1.enemies.update(e_list)
        elif not(team_2.members and student in team_2.enemies):
            team_2.members.add(student)
            team_2.enemies.update(e_list)
    # Check that a student isn't on both teams.
    team_cross = team_1.members.intersection(team_2.members)
    if team_cross:
        raise ValueError(f"Invalid members of both teams: {team_cross}")
    # Students completely split into two teams with no enemies on the same team.
    if team_1.members.union(team_2.members) == set(students.keys()):
        return team_1.members, team_2.members
    # No valid case where 
    return False

if __name__ == "__main__":
    class_a = {
        0: [3],
        1: [2],
        2: [1, 4],
        3: [0, 4, 5],
        4: [2, 3],
        5: [3]
    }

    class_b = {
        0: [3],
        1: [2],
        2: [1, 3, 4],
        3: [0, 2, 4, 5],
        4: [2, 3],
        5: [3]
    }

print(teamPair(class_a)) # ({0, 1, 4, 5}, {2, 3})
print(teamPair(class_b)) # False