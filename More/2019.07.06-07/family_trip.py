bugget = float(input())
number_nights = int(input())
price_per_night = float(input())
percentage_more_spends = int(input())
if number_nights > 7:
    price_per_night *= 0.95
price_per_night = price_per_night * number_nights
percentage_more_spends = bugget * percentage_more_spends / 100
total_sum = percentage_more_spends + price_per_night
difference = abs(total_sum - bugget)
if total_sum > bugget:
    print(f"{difference:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")