number = int(input())
sum_left = 0
sum_right = 0
for num in range(number * 2):
    current_number = int(input())
    if num < number:
        sum_left += current_number
    else:
        sum_right += current_number
if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    difference = abs(sum_right - sum_left)
    print(f"No, diff = {difference}")
