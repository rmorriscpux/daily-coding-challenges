'''
A builder is looking to build a row of N houses that can be of K different colors.
He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
'''

# In this matrix, each row (n) represents a house, and each column (k) represents a specific color.
# Each value in the matrix represents the cost to paint a specific house a specific color.
# Example Visualization:
    #  |R|G|B|Y|
    # A|1|2|3|4|
    # B|1|2|1|0|
    # C|6|1|1|5|
    # D|2|3|5|5|

# minCost() finds all valid color combinations and returns a tuple with the lowest cost and a list of house colors in order.
# This is time efficient but uses a lot of space. Perhaps I'll come back and make a space-efficient solution.
def minCost(house_color_matrix):

    def rMinCost(house_color_matrix, result, house_num, prev_color=-1, cost=0, color_sequence=[]):
        if house_num == len(house_color_matrix):
            result.append((cost, color_sequence))
            return
        
        for i in range(0, len(house_color_matrix[house_num])):
            if i != prev_color:
                rMinCost(house_color_matrix, result, house_num + 1, i, cost + house_color_matrix[house_num][i], color_sequence + [i])

    house_colors = []
    sequence = []
    rMinCost(house_color_matrix, house_colors, 0)
    return min(house_colors)

arr = [[1,2,3,4], [1,2,1,0], [6,1,1,5], [2,3,5,5]]
print(minCost(arr))