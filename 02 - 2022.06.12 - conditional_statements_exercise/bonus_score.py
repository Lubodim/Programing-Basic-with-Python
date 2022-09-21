start_number = int(input())
bonus = 0
if start_number <= 100:
    bonus += 5
elif start_number > 1000:
    bonus += start_number * 0.1
else:
    bonus += start_number * 0.2

if start_number % 2 == 0:
    bonus += 1
if start_number % 10 == 5:
    bonus += 2

print(bonus)
print(bonus + start_number)