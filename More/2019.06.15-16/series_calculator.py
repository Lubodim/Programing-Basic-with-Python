serial_name = input()
season_number = int(input())
episod_number = int(input())
episod_time_no_promotion = float(input())

episod_with_promotion = episod_time_no_promotion * 1.2
serial_time = season_number * (episod_number * episod_with_promotion + 10)
print(f"Total time needed to watch the {serial_name} series is {int(serial_time)} minutes.")