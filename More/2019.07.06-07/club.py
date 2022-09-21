desired_profit = float(input())
command = input()
money_counter = 0
current_money_order = 0
while True:
    if command == "Party!":
        break
    command = len(command)
    order = int(input())
    current_money_order = command * order
    if current_money_order % 2 != 0:
        current_money_order *= 0.75
    money_counter += current_money_order
    if money_counter >= desired_profit:
        break
    command = input()
difference = abs(money_counter - desired_profit)
if command == "Party!":
    print(f"We need {difference:.2f} leva more.")
    print(f"Club income - {money_counter:.2f} leva.")
elif money_counter >= desired_profit:
    print("Target acquired.")
    print(f"Club income - {money_counter:.2f} leva.")
