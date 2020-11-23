prices = [2, 5, 1, 4]

if len(prices) == 1:
    print( prices[0])
else:

    lowest = prices[0]
    s = prices[0]
    for i in range(1, len(prices)):

        s += max(prices[i] - lowest, 0)

        if prices[i] < lowest:
            lowest = prices[i]

    print(s)