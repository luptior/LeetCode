n = 6
m = 6

h = [2,3]
v = [4]


vspace = [1]*(m+1)
hspace = [1]*(n+1)

counter = 0

for i in v:
    toadd = vspace.pop(i)
    vspace[i-1]+= toadd

for i in h:
    toadd = hspace.pop(i)
    hspace[i-1]+= toadd

print(vspace)
print(hspace)

print(max(vspace)*max(hspace))


