from math import ceil

tennis_racket_price = float(input())
number_of_rackets = int(input())
number_of_sneakers = int(input())
sneakers_price = tennis_racket_price / 6
total_sum = (sneakers_price * number_of_sneakers +
             tennis_racket_price * number_of_rackets) * 1.2
djokovic_sum = total_sum / 8
sponsors_sum = total_sum - djokovic_sum

print(f"Price to be paid by Djokovic {int(djokovic_sum)}")
print(f"Price to be paid by sponsors {ceil(sponsors_sum)}")
