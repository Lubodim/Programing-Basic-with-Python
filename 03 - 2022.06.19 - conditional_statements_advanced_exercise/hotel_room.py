month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or "October":
    studio = 50
    apartment = 65
    if nights > 14:
        studio *= 0.7
        apartment *= 0.9
    elif nights > 7:
        studio *= 0.95
elif month == "June" or "September ":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio *= 0.8
        apartment *= 0.9
elif month == "July" or "August":
    studio = 76
    apartment = 77
    if nights > 14:
        apartment *= 0.9

total_nights_at_studio = studio * nights
total_nights_at_apartment = apartment * nights

print(f"Apartment: {total_nights_at_apartment:.2f} lv.")
print(f"Studio: {total_nights_at_studio} lv.")
