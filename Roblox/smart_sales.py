from collections import Counter

ids = [1,2,3,1,2,2]
m = 3

d = Counter(ids)

d = [x for x in reversed(d.most_common(len(d)))]

counter = 0

result = 0

new_d = {k:v for k, v in d}

for k,v in d:

    if counter >= m:
        result = len(new_d)
        break
    else:
        counter += v
        del new_d[k]



print(result)