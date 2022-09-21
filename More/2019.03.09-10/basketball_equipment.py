year_tax = int(input())
sneakers = year_tax * 0.6
outfit = sneakers * 0.8
ball = outfit / 4
accessories = ball / 5
needed_sum = year_tax + sneakers + outfit + ball + accessories
print(f"{needed_sum: .2f}")
