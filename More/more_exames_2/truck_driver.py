season = input()
kilometers_per_mount = float(input())

price_per_kilometer = 0

if kilometers_per_mount <= 5000:
    if season == "Summer":
        price_per_kilometer = 0.9
    elif season == "Winter":
        price_per_kilometer = 1.05
    else:
        price_per_kilometer = 0.75
elif 5000 < kilometers_per_mount <= 10000:
    if season == "Summer":
        price_per_kilometer = 1.10
    elif season == "Winter":
        price_per_kilometer = 1.25
    else:
        price_per_kilometer = 0.95
elif 10000 < kilometers_per_mount <= 20000:
    price_per_kilometer = 1.45

sum_for_season = (kilometers_per_mount * price_per_kilometer * 4) * 0.9

print(f"{sum_for_season:.2f}")
