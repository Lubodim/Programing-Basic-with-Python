number = int(input())

invalid_number = False

if (100 <= number <= 200):
    invalid_number = True
if number == 0:
    invalid_number = True

if not invalid_number:
    print("invalid")
