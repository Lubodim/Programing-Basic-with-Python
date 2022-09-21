bank_balance = 0
command = input()
while command != "NoMoreMoney":
    income_sum = float(command)
    if income_sum < 0:
        print("Invalid operation!")
        print(f"Total: {bank_balance:.2f}")
        break
    print(f"Increase: {income_sum:.2f}")
    bank_balance += income_sum
    command = input()
else:
    print(f"Total: {bank_balance:.2f}")
