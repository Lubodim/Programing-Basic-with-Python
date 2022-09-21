from math import ceil

fen_name = input()
budget = float(input())
beer_number = int(input())
chips_number = int(input())
beer_price = beer_number * 1.20
chips_price = ceil(chips_number * (beer_price * 0.45))
total_sum = beer_price + chips_price
difference = abs(total_sum - budget)
if budget >= total_sum:
    print(f"{fen_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fen_name} needs {difference:.2f} more leva!")