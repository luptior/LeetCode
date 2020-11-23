input = [-1, 1, 2, 3, -5]

input.sort()


result = []
while len(input) > 0:
    if len(input) % 2 == 0:
        result.append(input.pop(0))
    else:
        result.append(input.pop(-1))

print(result)