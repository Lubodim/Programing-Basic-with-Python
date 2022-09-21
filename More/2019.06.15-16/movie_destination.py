budget = float(input())
destination = input()
seasone = input()
number_of_days = int(input())
price_per_day = 0
if destination == "Dubai":
    if seasone == "Winter":
        price_per_day = 45000
    elif seasone == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if seasone == "Winter":
        price_per_day = 17000
    elif seasone == "Summer":
        price_per_day = 12000
    if destination == "Sofia":
        price_per_day *= 1.25
elif destination == "London":
    if seasone == "Winter":
        price_per_day = 24000
    elif seasone == "Summer":
        price_per_day = 20250
total_price = price_per_day * number_of_days
if destination == "Dubai":
    total_price *= 0.7

difference = abs(total_price - budget)
if budget > total_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")