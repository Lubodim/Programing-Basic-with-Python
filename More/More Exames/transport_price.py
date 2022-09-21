number_kilometers = int(input())
part_of_day = input()

train_travel = number_kilometers * 0.06
bus_travel = number_kilometers * 0.09
taxy_day_travel = 0.7 + number_kilometers * 0.79
taxy_night_travel = 0.7 + number_kilometers * 0.9


if number_kilometers >= 100:
    print(f"{train_travel:.2f}")
elif number_kilometers >= 20:
    print(f"{bus_travel:.2f}")
else:
    if part_of_day == "day":
        print(f"{taxy_day_travel:.2f}")
    else:
        print(f"{taxy_night_travel:.2f}")
