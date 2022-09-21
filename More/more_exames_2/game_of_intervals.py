num_of_move = int(input())

counter_0_9 = 0
counter_10_19 = 0
counter_20_29 = 0
counter_30_39 = 0
counter_40_50 = 0
invalid_counter = 0
total_counter = 0
for _ in range(num_of_move):
    current_number = int(input())
    if 0 <= current_number <= 9:
        counter_0_9 += 1
        total_counter += current_number * 0.2
    elif 10 <= current_number <= 19:
        counter_10_19 += 1
        total_counter += current_number * 0.3
    elif 20 <= current_number <= 29:
        counter_20_29 += 1
        total_counter += current_number * 0.4
    elif 30 <= current_number <= 39:
        counter_30_39 += 1
        total_counter += 50
    elif 40 <= current_number <= 50:
        counter_40_50 += 1
        total_counter += 100
    elif current_number > 50:
        invalid_counter += 1
        total_counter /= 2
    elif current_number < 0:
        invalid_counter += 1
        total_counter /= 2

percentage_0_9 = counter_0_9 / num_of_move * 100
percentage_10_19 = counter_10_19 / num_of_move * 100
percentage_20_29 = counter_20_29 / num_of_move * 100
percentage_30_39 = counter_30_39 / num_of_move * 100
percentage_40_50 = counter_40_50 / num_of_move * 100
invalid_percentage = invalid_counter / num_of_move * 100

print(f"{total_counter:.2f}")
print(f"From 0 to 9: {percentage_0_9:.2f}%")
print(f"From 10 to 19: {percentage_10_19:.2f}%")
print(f"From 20 to 29: {percentage_20_29:.2f}%")
print(f"From 30 to 39: {percentage_30_39:.2f}%")
print(f"From 40 to 50: {percentage_40_50:.2f}%")
print(f"Invalid numbers: {invalid_percentage:.2f}%")
