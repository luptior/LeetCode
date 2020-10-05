height = [1,1,3,4,1]
sh = sorted(height)

count = [1 if height[i] != sh[i] else 0 for i in range(len(height)) ]

print(sum(count))