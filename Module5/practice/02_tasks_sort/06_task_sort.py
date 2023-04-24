prices = [2, 1, 10, 50, 10]
prices.sort()

i = 0
total = 0
while i < len(prices) // 2:
    # print(prices[i], prices[-i - 1])
    total += prices[i] + prices[-i - 1]
    i += 1

print("Сумма чека:", total)
