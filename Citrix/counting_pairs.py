

k = 1

numbers = [1,1,1,2]

result = []

for i in numbers:
    if  {i, i+k} not in result and i+k in numbers:
        result.append({i, i+k})

print(result)