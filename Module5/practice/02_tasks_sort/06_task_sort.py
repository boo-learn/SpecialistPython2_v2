prices =[2, 1, 10, 50, 10]

prices.sort()

print(sum(prices[-(len(prices) // 2 + len(prices) %2 ):]))
