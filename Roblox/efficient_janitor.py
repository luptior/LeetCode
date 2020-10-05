"""
Given weights : [1.99, 1.01, 2.5, 1.5, 1.01]
Maximum bag size is 3.0 find the minimum number trips required by the janitor to dump the garbage.
Output for the example :
[1.01 + 1.99], [1.01 + 1.5], [2.5] so min steps is 3.
"""

"""
Find the minimum number of groups who's sum of each group is at max 3, and every element must be in a group.
Given an Array like: [1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]
return the minimum number of groups, in this case it would be 5 groups: (1.01 , 1.99), (1.01, 1.7), (3.0), (2.7), (2.3)
Constraint: all elements are between 1.01-3 inclucsive, and each groups sum is at max 3
"""

l = [1.01, 1.01, 3.0, 2.7, 1.99, 2.3, 1.7]

result = []
used = []

# nlog(n)
sortedL = sorted(l)

# log(n)
i = 0
j = len(l)-1

result = 0

while i<j:
    # print(sortedL[i], sortedL[j])
    if sortedL[i] + sortedL[j] < 3:
        i += 1
        j -= 1
    else:
        j -= 1
    result += 1

print(result)
