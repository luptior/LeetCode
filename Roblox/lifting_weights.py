maxCapacity = 6
weights = [1, 3, 5]

weights.sort()

i = 0
s = 0

result = []

def findpath(visited, left):

    if len(left) > 0 and sum(visited) < maxCapacity:
        for x in left:
            new_left = left[:]
            new_left.remove(x)
            if sum(visited+[x]) < maxCapacity:
                findpath(visited+[x], new_left)
            else:
                result.append(visited)
    else:
        result.append(visited)

findpath([], weights)

print(result)
