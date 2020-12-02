def is_valid(line):
    quantity, char, password = line.split(" ")
    char = char[0] # remove trailing :
    q_min, q_max = (int(x) for x in quantity.split("-"))
    q_actual = sum(1 for _ in filter(lambda c: c == char, password))
    return q_min <= q_actual <= q_max

def is_valid2(line):
    quantity, char, password = line.split(" ")
    char = char[0] # remove trailing :
    q_min, q_max = (int(x) for x in quantity.split("-"))
    return (password[q_min-1] == char) != (password[q_max-1] == char)

with open("inputs/2") as f:
    valid = sum(1 for _ in filter(is_valid, f))
    f.seek(0)
    valid2 = sum(1 for _ in filter(is_valid2, f))
    print(valid)
    print(valid2)
