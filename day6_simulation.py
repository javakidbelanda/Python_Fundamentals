









import random
Proportion = []

for i in range(1000):
    flips = []
    for _ in range(100):
        flip = random.choice(['H', 'T'])
        flips.append(flip)

    heads = flips.count('H')
    proportion_heads = heads / 100
    Proportion.append(proportion_heads)

average_proportion = sum(Proportion) / len(Proportion)


print("Average proportion of heads:", average_proportion)

def simulate_coin_flips(num_flips, num_simulations):
    proportions = []
    for _ in range(num_simulations):
        heads = 0
        for _ in range(num_flips):
            if random.choice(['H', 'T']) == 'H':
                heads += 1

        proportions.append(heads / num_flips)
    return sum (proportions) / len(proportions)

print("100 flips avg:", simulate_coin_flips(100, 1000))
print("1000 flips avg:", simulate_coin_flips(1000, 10000))
