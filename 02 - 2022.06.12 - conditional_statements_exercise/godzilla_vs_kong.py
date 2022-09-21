bugget = float(input())
number_of_statists = int(input())
price_for_dress = float(input())

decor = bugget * 0.1

if number_of_statists > 150:
    price_for_dress *= 0.9

needet_money = price_for_dress + decor

something = abs(needet_money - bugget)

if needet_money > bugget:
    print("Not enough money!")
    print(f"Wingard needs {something:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {something:.2f} leva left.")
