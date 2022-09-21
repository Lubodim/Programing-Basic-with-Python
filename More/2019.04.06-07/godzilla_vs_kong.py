budget = float(input())
statists_number = int(input())
price_for_dreses_per_statist = float(input())
decoration = budget * 0.1
dres_price = price_for_dreses_per_statist * statists_number
if statists_number > 150:
    dres_price *= 0.9
total_money_costs = dres_price + decoration
difference = abs(total_money_costs - budget)
if total_money_costs > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print(f"Action!" )
    print(f"Wingard starts filming with {difference:.2f} leva left.")
