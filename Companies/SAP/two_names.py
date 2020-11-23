
input = "tim mary,scott grey"

names = input.split(",")

c1 = names[1].split(" ")[1]
c2 = names[0].split(" ")[0]

print( f"{c1} {c2}")