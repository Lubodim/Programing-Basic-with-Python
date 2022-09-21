price_vegetables = float(input())
price_fruits = float(input())
kilograms_vegetables = int(input())
kilograms_fruits = int(input())

total_price = (price_vegetables * kilograms_vegetables + price_fruits * kilograms_fruits) / 1.94

print(format(total_price, ".2f"))