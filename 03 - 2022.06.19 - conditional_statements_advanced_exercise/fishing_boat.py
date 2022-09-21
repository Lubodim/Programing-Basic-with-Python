bugget = int(input())
season = input()
number_fishers = int(input())

rent_of_boat = 0

if season == "Spring":
    rent_of_boat = 3000
elif season == "Winter":
    rent_of_boat = 2600
else:
    rent_of_boat = 4200

if number_fishers <= 6:
    rent_of_boat *= 0.9
elif number_fishers <= 11:
    rent_of_boat *= 0.85
else:
    rent_of_boat *= 0.75

if number_fishers % 2 == 0 and season != "Autumn":
    rent_of_boat *= 0.95
difference = abs(bugget - rent_of_boat)

if bugget >= rent_of_boat:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
