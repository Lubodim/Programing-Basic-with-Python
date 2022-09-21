factorial = int(input("Write the factorial number here: "))
factorial_sum = 1
factorial_formula = "1"
for i in range(1, factorial + 1):
    if i != 1:
        factorial_formula += f"*{i}"
        factorial_sum *= i
print(f"{factorial_formula} = {factorial_sum} = {factorial}!")
