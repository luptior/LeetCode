"""
https://leetcode.com/discuss/interview-question/541160/Twilio-OA-2020

"""

from collections import Counter
from collections import defaultdict

# n = 6
# items = [4,5,6,5,4,3]

n=8
items = [8,5,5,5,5,1,1,1,4,4]

d = Counter(items)

store = defaultdict(list)

for k, v in d.most_common():
    store[v].append(k)

result = []

for key in sorted(store.keys()):
    for element in sorted(store[key]):
        result += [element] * key

print(result)
