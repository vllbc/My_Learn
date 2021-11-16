prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
print(max(zip(prices.values(),prices.keys())))
print(max(prices.items(),key=lambda x:x[1]))
print(max(prices,key=lambda k:prices[k]))
