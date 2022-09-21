chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
seasone = input()
weekend = input()

price_chrysanthemums = 0
price_roses = 0
price_tulips = 0

sum_of_flawer = chrysanthemums + roses + tulips

if seasone == "Spring" or seasone == "Summer":
    if chrysanthemums:
        price_chrysanthemums = 2
    if roses:
        price_roses = 4.10
    if tulips:
        price_tulips = 2.50

if seasone == "Autumn" or seasone == "Winter":
    if chrysanthemums:
        price_chrysanthemums = 3.75
    if roses:
        price_roses = 4.50
    if tulips:
        price_tulips = 4.15


total_price = chrysanthemums * price_chrysanthemums + roses * price_roses + tulips * price_tulips

if weekend == "Y":
    total_price *= 1.15
if seasone == "Spring" or seasone == "Summer" or seasone == "Autumn" or seasone == "Winter":
    if (sum_of_flawer) > 20:
        total_price *= 0.8
if seasone == "Spring" and tulips >7:
    total_price *= 0.95
if seasone == "Winter" and roses >= 10:
    total_price *= 0.90

total_price += 2    # аранжиране на букет

print(f"{total_price:.2f}")
