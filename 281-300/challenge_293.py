'''
You have N stones in a row, and would like to create from them a pyramid.
This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone,
after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary.
Given this information, determine the lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1].
'''

def createPyramid(stones: list[int]) -> tuple[int, list[int]]:
    # Pyramid length will wind up being an odd number less than or equal to the length of the input list.
    pyramid_length = len(stones)
    if pyramid_length % 2 == 0:
        pyramid_length -= 1
    # Default output.
    final_pyramid = [0] * len(stones)
    moves = -1

    while pyramid_length > 0 and moves == -1:
        # Peak height is length divided by 2 rounded up. Make pyramid list going from 1 to peak height and back down.
        peak_height = pyramid_length // 2 + 1
        pyramid = [i for i in range(1, peak_height)] + [j for j in range(peak_height, 0, -1)]

        # Check that the pyramid height is not higher than each stone starting from left or right.
        for offset in [0, len(stones) - pyramid_length]:
            is_valid = True
            for i, num in enumerate(pyramid):
                if num > stones[i + offset]:
                    is_valid = False
                    break

            if is_valid:
                # When a valid pyramid is found, construct the output based on the offset and calculate the moves it takes to make the valid pyramid.
                # Loop will end when this is accomplished.
                final_pyramid = ([0] * offset) + pyramid + ([0] * (len(stones) - offset - pyramid_length))
                moves = sum(stones) - sum(pyramid)
                break
        
        pyramid_length -= 2

    return moves, final_pyramid

if __name__ == "__main__":
    print(createPyramid([1, 1, 3, 3, 2, 1]))
    print(createPyramid([1, 2, 3, 3, 1, 1]))