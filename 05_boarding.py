ROW_RANGE = 128
COL_RANGE = 8
SUFFIX_LEN = 3

with open("inputs/5") as f:
    seats = [l.rstrip() for l in f]


def bsp(seat, range, upper_char):
    low = 0
    high = range
    for char in seat:
        if char == upper_char:
            low += (high - low) // 2
        else:
            high -= (high - low) // 2
    return low


def seat_id(seat):
    row = bsp(seat[:-SUFFIX_LEN], ROW_RANGE, "B")
    col = bsp(seat[-SUFFIX_LEN:], COL_RANGE, "R")
    return row * 8 + col


# Problem 1
print(max(seat_id(seat) for seat in seats))

# Problem 2
ids = set(seat_id(seat) for seat in seats)
for i in range(ROW_RANGE * COL_RANGE):
    if i not in ids and i-1 in ids and i+1 in ids:
        print(i)
        break
