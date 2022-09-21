rent_of_hall = int(input())
statuettes = rent_of_hall * 0.7
catering = statuettes * 0.85
voicing = catering * 0.5

total_money_costs = rent_of_hall + statuettes + catering + voicing
print(f"{total_money_costs:.2f}")
