season = input()
group_type = input()
number_students = int(input())
number_of_nights = int(input())

price_for_night = 0
sports = ""
if group_type == "mixed":
    if season == "Winter":
        price_for_night = 10
    elif season == "Spring":
        price_for_night = 9.50
    elif season == "Summer":
        price_for_night = 20
else:
    if season == "Winter":
        price_for_night = 9.60
    elif season == "Spring":
        price_for_night = 7.20
    elif season == "Summer":
        price_for_night = 15

if group_type == "mixed":
    if season == "Winter":
        sports = "Ski"
    elif season == "Spring":
        sports = "Cycling"
    elif season == "Summer":
        sports = "Swimming"
elif group_type == "girls":
    if season == "Winter":
        sports = "Gymnastics"
    elif season == "Spring":
        sports = "Athletics"
    elif season == "Summer":
        sports = "Volleyball"
else:
    if season == "Winter":
        sports = "Judo"
    elif season == "Spring":
        sports = "Tennis"
    elif season == "Summer":
        sports = "Football"
total_price = number_students * number_of_nights * price_for_night

if number_students >= 50:
    total_price *= 0.5
elif number_students >= 20:
    total_price *= 0.85
elif number_students >= 10:
    total_price *= 0.95

print(f"{sports} {total_price:.2f} lv.")
