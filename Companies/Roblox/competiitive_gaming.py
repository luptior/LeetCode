"""

int k the cutoff rank
int scores[n]
"""

from collections import Counter

# scores = [100, 50, 50, 25]
# n = 4
# k = 3

scores = [2,2,3,4,5]
n = 5
k = 4

# O(n)
d = Counter(scores)

print(d)
counts = 0

# O(n)
for key in sorted(d, reverse=True):
    v = d[key ]
    if counts < k:
        counts += v
    print(key , counts)
    print( counts >= k)
    if counts >= k:
        print(k, v, counts)
        break

print(counts)



