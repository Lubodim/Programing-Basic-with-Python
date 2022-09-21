number_1 = int(input())
number_2= int(input())
operator = input()

moving = 0
type_number = ""

if operator == "+":
    moving = number_1 + number_2
    if moving % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
elif operator == "-":
    moving = number_1 - number_2
    if moving % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
elif operator == "*":
    moving = number_1 * number_2
    if moving % 2 == 0:
        type_number = "even"
    else:
        type_number = "odd"
elif operator == "/":
    if number_2 == 0:
        pass
    else:
        moving = number_1 / number_2
elif operator == "%":
    if number_2 == 0:
        pass
    else:
        moving = number_1 % number_2


if operator == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} / {number_2} = {moving:.2f}")
elif operator == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        print(f"{number_1} % {number_2} = {moving}")
if operator == "+" or "-" or "*":
    print(f"{number_1} {operator} {number_2} = {moving} - {type_number}")

