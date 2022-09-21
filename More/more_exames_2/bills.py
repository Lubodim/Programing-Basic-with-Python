mounts = int(input())

electricity_counter = 0
water_counter = 0
internet_counter = 0

for _ in range(mounts):
    current_mount_electricity_bill = float(input())
    electricity_counter += current_mount_electricity_bill
    water_counter += 20
    internet_counter += 15

other_counter = (electricity_counter + water_counter + internet_counter) * 1.2
average_sum = (electricity_counter + water_counter + internet_counter + other_counter) / mounts

print(f"Electricity: {electricity_counter:.2f} lv")
print(f"Water: {water_counter:.2f} lv")
print(f"Internet: {internet_counter:.2f} lv")
print(f"Other: {other_counter:.2f} lv")
print(f"Average: {average_sum:.2f} lv")
