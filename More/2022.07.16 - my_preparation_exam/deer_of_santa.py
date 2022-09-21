from math import ceil

number_missing_days = int(input())
total_food_for_deer = int(input())
food_per_day_d1 = float(input())
food_per_day_d2 = float(input())
food_per_day_d3 = float(input())

eaten_food = food_per_day_d1 * number_missing_days\
             + food_per_day_d2 * number_missing_days + food_per_day_d3 * number_missing_days
difference = abs(total_food_for_deer - eaten_food)
if total_food_for_deer > eaten_food:
    print(f"{int(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")