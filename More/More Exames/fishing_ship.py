bugget = int(input())
seasone = input()
fishing_mans = int(input())

rent_ship = 0
discount = 0

if seasone == "Spring":
    rent_ship = 3000
elif seasone == "Summer" and "Autumn":
    rent_ship = 4200
elif seasone == "Winter":
    rent_ship = 2600

if fishing_mans >= 6:
    discount = rent_ship - rent_ship * 0.1
elif 7 <= fishing_mans <= 11:
    discount = rent_ship - rent_ship * 0.15
elif fishing_mans >= 12:
    discount = rent_ship - rent_ship * 0.25

if fishing_mans % 2 == 0 and seasone != "Autumn":
    extra_discount = discount * 0.05

total = abs(bugget - extra_discount)

if bugget >= extra_discount:
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total:.2f} leva.")
