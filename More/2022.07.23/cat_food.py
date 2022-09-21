cat_number = int(input())
small_cat = 0
big_cat = 0
huge_cat = 0
total_eaten_food = 0
for _ in range(cat_number):
    eaten_food = float(input())
    if 100 <= eaten_food < 200:
        small_cat += 1
        total_eaten_food += eaten_food
    elif 200 <= eaten_food < 300:
        big_cat += 1
        total_eaten_food += eaten_food
    elif 300 <= eaten_food < 400:
        huge_cat += 1
        total_eaten_food += eaten_food
total_eaten_food /= 1000

print(f"Group 1: {small_cat} cats.")
print(f"Group 2: {big_cat} cats.")
print(f"Group 3: {huge_cat} cats.")
print(f"Price for food per day: {(total_eaten_food * 12.45):.2f} lv.")
