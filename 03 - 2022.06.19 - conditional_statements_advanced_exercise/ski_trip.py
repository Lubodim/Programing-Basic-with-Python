days_in_hotel = int(input())
type_room = input()
evaluation = input()

nights = days_in_hotel - 1
price_per_night = 0

if type_room == "room for one person":
    price_per_night = 18
elif type_room == "apartment":
    price_per_night = 25
    if days_in_hotel < 10:
        price_per_night *= 0.7
    elif days_in_hotel > 15:
        price_per_night *= 0.5
    else:
        price_per_night *= 0.65
elif type_room == "president apartment":
    price_per_night = 35
    if days_in_hotel < 10:
        price_per_night *= 0.9
    elif days_in_hotel > 15:
        price_per_night *= 0.8
    else:
        price_per_night *= 0.85

if evaluation == "positive":
    price_per_night *= 1.25
else:
    price_per_night *= 0.9

total_price = price_per_night * nights

print(f"{total_price:.2f}")
