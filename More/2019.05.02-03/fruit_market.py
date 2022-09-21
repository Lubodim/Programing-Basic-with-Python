strawberries_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.5
orange_price = raspberries_price * 0.6
banana_price = raspberries_price * 0.2

needed_sum = banana_price * banana_quantity + orange_price * orange_quantity\
             + raspberries_price * raspberries_quantity + strawberries_price * strawberries_quantity

print(f"{needed_sum:.2f}")
