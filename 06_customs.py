with open("inputs/6") as f:
    groups = f.read().rstrip().split("\n\n")


def any_yes(group):
    chars = set(c for c in group)
    chars.discard("\n")
    return len(chars)


# Problem 1
print(sum(any_yes(g) for g in groups))


def all_yes(group):
    sets = []
    for person in group.strip().split("\n"):
        sets.append(set(c for c in person))
    return len(set.intersection(*sets))


# Problem 2
print(sum(all_yes(g) for g in groups))
