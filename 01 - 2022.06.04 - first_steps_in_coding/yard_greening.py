landscaping_square_price = 7.61
square_metres_for_landscapeing = float(input())
discount = 0.18

price_of_work = square_metres_for_landscapeing * landscaping_square_price
discount_price = price_of_work * discount
total_price = price_of_work - discount_price

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount_price} lv.')
