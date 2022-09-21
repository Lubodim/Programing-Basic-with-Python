type_flower = input()
number_of_flowers = int(input())
bugger = int(input())

price_of_flowers = 0

if type_flower == "Roses":
    price_of_flowers = 5
    if number_of_flowers > 80:
        price_of_flowers *= 0.9
elif type_flower == "Dahlias":
    price_of_flowers = 3.80
    if number_of_flowers > 90:
        price_of_flowers *= 0.85
elif type_flower == "Tulips":
    price_of_flowers = 2.80
    if number_of_flowers > 80:
        price_of_flowers *= 0.85
elif type_flower == "Narcissus":
    price_of_flowers = 3
    if number_of_flowers < 120:
        price_of_flowers *= 1.15
elif type_flower == "Gladiolus":
    price_of_flowers = 2.50
    if number_of_flowers < 80:
        price_of_flowers *= 1.20
total_price = price_of_flowers * number_of_flowers
difference = abs(total_price - bugger)

if bugger >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flower} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")