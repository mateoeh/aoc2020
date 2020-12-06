from functools import reduce
from operator import mul

with open("inputs/3") as f:
    trees = [[1 if c == '#' else 0 for c in line.strip()] for line in f]
height = len(trees)
width = len(trees[0])


def num_trees(right, down):
    x_pos, y_pos = 0, 0

    sum = 0
    while y_pos < height:
        sum += trees[y_pos][x_pos % width]
        y_pos += down
        x_pos += right
    return sum


# Problem 1
print(num_trees(3, 1))

# Problem 2
slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
print(reduce(mul, [num_trees(r, d) for r, d in slopes]))
