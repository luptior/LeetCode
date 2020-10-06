products = ["eggs", "milk", "cheese"]
productPrices = [2.89, 3.29, 5.79]
productSold = ["eggs", "eggs", "cheese", "milk"]
solsPrice = [2.89, 2.99, 5.97, 3.29]


count = 0
for i, d in enumerate(productSold):
    if productPrices[products.index(d)] != solsPrice[i]:
        count +=1

print(count)