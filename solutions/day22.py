def secret_evolution(seed: int)-> int:

    secret = seed
    secret = ((secret * 64) ^ secret) % 16777216
    secret = ((secret //32) ^ secret) % 16777216

    return ((secret * 2048) ^ secret) % 16777216
    
# Part 1
total = 0 
with open('data/input22.txt','r') as f:
    for line in f:
        secret = int(line)
        for _ in range(2000):
            secret = secret_evolution(secret)
        total+=secret
print(total)

#Part 2

dp = []


with open('data/input22.txt','r') as f:
    buyers = [int(secret.strip()) for secret in f.readlines()]
    prices = []
    for i in range(len(buyers)):
        secret = buyers[i]
        price_buyer = []
        for _ in range(2000):
            price_buyer.append(int(str(secret)[-1]))
            secret = secret_evolution(secret)
        prices.append(price_buyer)

    windows = set()
    delta_prices = []
    for k in range(len(buyers)):
        deltas = []
        for i in range(1,len(prices[k])):
            delta = prices[k][i] - prices[k][i-1]
            deltas.append(delta)
        delta_prices.append(deltas)
    

    d ={}


    for k, delta_price in enumerate(delta_prices):
        visited = set()
        for i in range(len(delta_price)-4):
            window = tuple(delta_price[i:i+4])
            if window not in visited:
                d[window]=d.get(window,0) + prices[k][i+4]
                visited.add(window)

    print(max([v for _, v in d.items()]))


    

