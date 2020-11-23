salePrice = 10
costPerCut = 1

lengths = [30, 59, 110]

# rods * saleLength * salePrice - totalCuts * costPerCut

rods = 0
totalCuts = 0
saleLength  = 30

for length in lengths:
    rod = length // saleLength
    rods += rod
    # print(length)
    # print(rod-(1 if length%saleLength == 0 else 0))
    totalCuts += rod-(1 if length%saleLength == 0 else 0)

print("rods", rods)
print("totalCuts" , totalCuts)
print("saleLength" , saleLength)

print(rods * saleLength * salePrice - totalCuts * costPerCut)