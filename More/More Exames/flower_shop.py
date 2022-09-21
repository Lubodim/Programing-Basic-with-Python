from math import floor, ceil

number_magnolia = int(input())
number_hyacinth = int(input())
number_rose = int(input())
number_cactus = int(input())
gift_price = float(input())

order_sum = number_magnolia * 3.25 + number_hyacinth * 4 + number_rose * 3.5 + number_cactus * 8
order_sum *= 0.95

something = abs(gift_price - order_sum)

if order_sum >= gift_price:
    print(f"She is left with {floor(something)} leva.")
else:
    print(f"She will have to borrow {ceil(something)} leva.")
