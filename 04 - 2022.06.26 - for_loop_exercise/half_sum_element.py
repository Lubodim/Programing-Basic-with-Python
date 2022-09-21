from sys import maxsize

input_number = int(input())

max_size = - maxsize
total_sum = 0

for num in range(input_number):
    current_number = int(input())
    if current_number > max_size:
        max_size = current_number
    total_sum += current_number
half_total_sum = total_sum - max_size
if half_total_sum == max_size:
    print("Yes")
    print(f"Sum = {max_size}")
else:
    difference = abs(max_size - half_total_sum)
    print("No")
    print(f"Diff = {difference}")
