'''
A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A

does not validate, since A cannot be both north and south of C.

A NW B
A N B

is considered valid.
'''

from typing import List

def validateMapRules(rule_set: List[str]):
    OPPOSITE = {
        "N": "S",
        "S": "N",
        "W": "E",
        "E": "W"
    }

    def getEndPosition(direction, start_pos):
        end_x, end_y = start_pos
        for d in direction:
            if d == "N":
                end_y += 1
            elif d == "E":
                end_x += 1
            elif d == "S":
                end_y -= 1
            elif d == "W":
                end_x -= 1
        return end_x, end_y

    def rValidateMapRules(rule_set, index, map_dict):
        if index == len(rule_set):
            return True

        end, direction, start = rule_set[index].split()

        if start == end:
            return False
        
        if start in map_dict and end in map_dict:
            if map_dict[start] == map_dict[end]:
                map_dict[end] = getEndPosition(direction, map_dict[start])
                return rValidateMapRules(rule_set[:index] + rule_set[index+1:], 0, map_dict)
            else:
                for d in direction:
                    if ((d == "N" and map_dict[start][1] >= map_dict[end][1]) or
                        (d == "S" and map_dict[start][1] <= map_dict[end][1]) or
                        (d == "W" and map_dict[start][0] >= map_dict[end][0]) or
                        (d == "E" and map_dict[start][0] <= map_dict[end][0])):
                        return False
        elif start in map_dict:
            map_dict[end] = getEndPosition(direction, map_dict[start])
        elif end in map_dict:
            opp_direction = ""
            for d in direction:
                opp_direction += OPPOSITE[d]
            map_dict[start] = getEndPosition(opp_direction, map_dict[end])
        else:
            map_dict[start] = (0, 0)
            map_dict[end] = getEndPosition(direction, map_dict[start])

        return rValidateMapRules(rule_set, index+1, map_dict)

    return rValidateMapRules(rule_set, 0, dict())

print(validateMapRules([
    "A N B",
    "B NE C",
    "C N A"
]))

print(validateMapRules([
    "A NW B",
    "A N B"
]))