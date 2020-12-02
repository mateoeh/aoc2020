entries = []
with open("inputs/1") as f:
    for line in f:
        entries.append(int(line))
entries.sort()

left = 0
right = len(entries) - 1
while left < right:
    cur = entries[left] + entries[right]
    if cur == 2020:
        break
    elif cur > 2020:
        right -= 1
    else:
        left += 1

# Problem 1
print(entries[left] * entries[right])

for first in range(0, len(entries)):
    second = 0
    third = len(entries) - 1
    cur = 0
    while second < third:
        if second == first:
            second += 1
            continue
        elif third == first:
            third -= 1
            continue
        
        cur = entries[first] + entries[second] + entries[third]
        if cur == 2020:
            break
        elif cur < 2020:
            second += 1
        else:
            third -= 1
    if cur == 2020:
        break

print(entries[first] * entries[second] * entries[third])
