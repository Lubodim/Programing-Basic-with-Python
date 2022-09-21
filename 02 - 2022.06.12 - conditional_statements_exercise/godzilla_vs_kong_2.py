bugget = float(input())
number_of_statists = int(input())
price_for_one_dress = float(input())

decor = bugget * 0.1
prire_for_dreses = price_for_one_dress * number_of_statists

if number_of_statists > 150:
    prire_for_dreses *= 0.9

needet_money = prire_for_dreses + decor

something = abs(needet_money - bugget)

if needet_money > bugget:
    print("Not enough money!")
    print(f"Wingard needs {something:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {something:.2f} leva left.")
