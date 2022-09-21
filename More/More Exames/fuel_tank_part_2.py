fuel_type = input()
fuel_quantity = float(input())
club_card = input()

fuel_price = 0

if fuel_type == "Gas" and club_card == "Yes":
    fuel_price = fuel_quantity * (0.93 - 0.08)
elif fuel_type == "Gas" and club_card == "No":
    fuel_price = fuel_quantity * 0.93
elif fuel_type == "Diesel" and club_card == "Yes":
    fuel_price = fuel_quantity * (2.33 - 0.12)
elif fuel_type == "Diesel" and club_card == "No":
    fuel_price = fuel_quantity * 2.33
elif fuel_type == "Gasoline" and club_card == "Yes":
    fuel_price = fuel_quantity * (2.22 - 0.18)
elif fuel_type == "Gasoline" and club_card == "No":
    fuel_price = fuel_quantity * 2.22

if 20 <= fuel_quantity <= 25:
    fuel_price *= 0.92
elif fuel_quantity > 25:
    fuel_price *= 0.90
else:
    fuel_price = fuel_price

print(f"{fuel_price:.2f} lv.")
