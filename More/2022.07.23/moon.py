from math import ceil

average_speed = float(input())
liters_fuel_per_100_km = float(input())
moon_distance = 384400 * 2
time_traveling = ceil(moon_distance / average_speed + 3)
needed_fuel = int(liters_fuel_per_100_km * moon_distance / 100)
print(time_traveling)
print(needed_fuel)