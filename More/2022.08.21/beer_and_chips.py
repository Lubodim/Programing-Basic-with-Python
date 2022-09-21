from math import ceil

fen_name = input()
budget = float(input())
beer_bottles = int(input())
chips_pacs = int(input())


one_chips_price = (beer_bottles * 1.2) * 0.45

chips_price = ceil(one_chips_price * chips_pacs)
beer_price = beer_bottles * 1.2
total_price = beer_price +  chips_price

difference = abs(total_price - budget)

if budget >= total_price:
    print(f"{fen_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fen_name} needs {difference:.2f} more leva!")
