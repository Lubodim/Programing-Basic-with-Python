budget = float(input())
serials_number = int(input())
for _ in range(serials_number):
    serials_name = input()
    serials_price = float(input())
    if serials_name == "Thrones":
        serials_price *= 0.5
    elif serials_name == "Lucifer":
        serials_price *= 0.6
    elif serials_name == "Protector":
        serials_price *= 0.7
    elif serials_name == "TotalDrama":
        serials_price *= 0.8
    elif serials_name == "Area":
        serials_price *= 0.9
    budget -= serials_price
if budget >= 0:
    print(f"You bought all the series and left with {abs(budget):.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")