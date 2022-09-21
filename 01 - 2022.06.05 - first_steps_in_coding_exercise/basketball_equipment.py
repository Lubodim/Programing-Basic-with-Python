year_tax = int(input())

sneakers = year_tax - year_tax * 0.4
dress = sneakers - sneakers * 0.2
ball = dress / 4
accessories = ball / 5

costs = year_tax + sneakers + dress + ball + accessories

print(costs)
