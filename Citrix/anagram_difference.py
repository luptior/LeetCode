from collections import  Counter

a = ["tea", "tea", "act"]
b = ["ate", "toa", "acts"]
result = []

for i in range(len(a)):
    if len(a[i]) != len(b[i]):
        result.append(-1)
    else:
        c1 = Counter(a[i])
        c2 = Counter(b[i])
        c3 = c1 - c2
        result.append(sum(c3.values()))

print(result)


