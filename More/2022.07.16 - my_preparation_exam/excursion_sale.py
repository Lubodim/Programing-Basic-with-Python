number_sea_trip = int(input())
number_mountain_trip = int(input())
total_profit = 0
while True:
    command = input()
    if command == "Stop":
        break
    elif command == "sea":
        number_sea_trip -= 1
        if number_sea_trip < 0:
            total_profit += 0
            number_sea_trip += 1
        else:
            total_profit += 680
    elif command == "mountain":
        number_mountain_trip -= 1
        if number_mountain_trip < 0:
            total_profit += 0
            number_mountain_trip += 1
        else:
            total_profit += 499
    if number_mountain_trip == 0 and number_sea_trip == 0:
        print(" Good job! Everything is sold.")
        break
print(f"Profit: {total_profit} leva.")