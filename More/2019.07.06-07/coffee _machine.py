drink = input()
suggar = input()
number_drinks = int(input())
price = 0
if drink == "Espresso":
    price = 0.9
    if suggar == "Without":
        price *= 0.65
    elif suggar == "Normal":
        price = 1
    elif suggar == "Extra":
        price = 1.2
    if number_drinks > 5:
        price *= 0.75
elif drink == "Cappuccino":
    price = 1
    if suggar == "Without":
        price *= 0.65
    elif suggar == "Normal":
        price = 1.2
    elif suggar == "Extra":
        price = 1.6
elif drink == "Tea":
    price = 0.5
    if suggar == "Without":
        price *= 0.65
    elif suggar == "Normal":
        price = 0.6
    elif suggar == "Extra":
        price = 0.7
price = number_drinks * price
if price > 15:
    price *= 0.8
print(f"You bought {number_drinks} cups of {drink} for {price:.2f} lv.")
