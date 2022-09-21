number_location = int(input())

for i in range(number_location):
    expected_gold = float(input())
    mining_days = int(input())
    average_mining = 0
    for j in range(mining_days):
        gold_per_day = float(input())
        average_mining += gold_per_day
    average_mining /= mining_days
    if average_mining >= expected_gold:
        print(f"Good job! Average gold per day: {average_mining:.2f}.")
    else:
        print(f"You need {(expected_gold - average_mining):.2f} gold.")
