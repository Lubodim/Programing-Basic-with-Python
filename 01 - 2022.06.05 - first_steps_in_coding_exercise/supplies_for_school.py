pen = int(input())
marker = int(input())
detergent = int(input())
percent_discount = int(input())

pen_price = 5.80 * pen
marker_price = 7.20 * marker
detergent_price = 1.20 * detergent

percent_discount = percent_discount * 0.01

all_price = (pen_price + marker_price + detergent_price)

price_with_discount = all_price - all_price * percent_discount

print(price_with_discount)