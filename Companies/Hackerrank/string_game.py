import sys
from collections import Counter

for line in sys.stdin:
    words = [word.lower().strip() for word in line.split(",")]
    d = Counter(words)
    print(list(d.keys()))

line = input()
nums = [int(x) for x in line.split(",")]
f3 = [num for num in nums if sum([x for x in range(1, num) if num % x == 0]) == 3]
print(sum(f3))
