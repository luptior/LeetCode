"""
https://www.1point3acres.com/bbs/thread-670144-1-1.html
"""

from collections import Counter

# wordSet = ["listen", "silent", "it", "is"]
# sentence = "listen it is silent"

wordSet = ["the", "bats", "tabs", "in", "cat", "act"]
# sentence = "cat the bats"
# sentence = "in the act"
sentence = "act tabs in"

def groupAnagrams(strs: [str]) -> [[str]]:
    d = {}

    for s in strs:
        k = "".join(sorted(s))
        if k in d:
            d[k].append(s)
        else:
            d[k] = [s]

    return list(d.values())

groups = groupAnagrams(wordSet)
d = {}

for group in groups:
    l = len(group)

    for word in group:
        d[word] = l

result = 1

for word in sentence.split(" "):
    result *= d[word]

print(result)