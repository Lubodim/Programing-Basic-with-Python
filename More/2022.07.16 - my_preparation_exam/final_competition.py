dancers_number = int(input())
points = float(input())
season = input()
place = input()

won_price = 0

if place == "Bulgaria":
    won_price = points * dancers_number
else:
    won_price = (dancers_number * points) * 1.5
if season == "summer" and place == "Bulgaria":
    won_price *= 0.95
elif season == "winter" and place == "Bulgaria":
    won_price *= 0.92
elif season == "summer" and place == "Abroad":
    won_price *= 0.90
elif season == "winter" and place == "Abroad":
    won_price *= 0.85
charity = won_price * 0.75
won_price -= charity
won_price /= dancers_number
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {won_price:.2f}")
