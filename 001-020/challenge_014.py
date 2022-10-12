import random, math

# Determine the value of pi using a Monte Carlo method. (i.e. taking a set of random values to get a deterministic result)

total_sims = 1000000
inside_count = 0

for i in range(0, total_sims):
    # Get two random coordinates between 0 and 1
    x_coordinate = random.random()
    y_coordinate = random.random()
    # Determine if the x and y coordinates are within a unit circle.
    if math.pow(x_coordinate, 2) + math.pow(y_coordinate, 2) <= 1:
        inside_count += 1

# Knowing the theoretical ratio of unit circle to unit square is pi/4, we can calculate pi using the results.
calculated_pi = inside_count / total_sims * 4
print(calculated_pi)