budget = float(input())
liters_fuel = float(input())
day_of_week = input()

needed_sum = liters_fuel * 2.10 + 100
if day_of_week == "Saturday":
    needed_sum *= 0.9
elif day_of_week == "Sunday":
    needed_sum *= 0.8

difference = abs(budget - needed_sum)
if budget >= needed_sum:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")