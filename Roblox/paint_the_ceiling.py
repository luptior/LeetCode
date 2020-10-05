
seed = lambda s, k, b, m : ((k*s+b)%m)+1+s


n = 3
s = []
s.append(1)
k=1
b=1
m=2
a=4

for i in range(1, n):
    s.append(seed(s[i-1], k, b, m))


print(s)

i = 1
j= len(s)-1

result = 0
while i < n and j > -1:
    if s[i] * s[j] <= a:
        result += j + 1
        i += 1
    else:
        j -= 1


print(result)

