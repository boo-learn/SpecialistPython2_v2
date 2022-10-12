prices = [2, 1, 10, 50, 10, 6]
prices.sort()
half = len(prices) // 2
summa = sum(prices[half:])
print(summa)
