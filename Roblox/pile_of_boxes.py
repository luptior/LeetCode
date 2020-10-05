n = 5

from collections import Counter

piles = [4,5,5,2,4]

d = Counter(piles)

keys = list(set(piles))
keys.sort(reverse=True)

print(keys)
counter = 0

for i in range(len(keys)-1):
    print(i, len(keys)-1-i , d[keys[i]])
    counter += (len(keys)-1-i )*d[keys[i]]

print(counter)

# solution 2
def minStepEqualPiles(A):
    cnt = Counter(A)
    nums = sorted(cnt.keys(), reverse=True)
    k, ans = 0, 0
    for x in nums[:-1]:
        k += cnt[x]
        ans += k
    return ans








