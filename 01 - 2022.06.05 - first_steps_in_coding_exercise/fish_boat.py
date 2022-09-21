bugget = int(input())
season = input()
number_fishmans = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer, Autumn":
    price = 4200
elif season == "Winter":
    price = 2600


print(price)