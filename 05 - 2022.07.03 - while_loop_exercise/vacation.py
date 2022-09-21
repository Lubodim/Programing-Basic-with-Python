needed_money = float(input())
money_in_wallet = float(input())
day_counter = 0
spending_day = 0
is_save_money = False
while needed_money > money_in_wallet:
    doing = input()
    current_money = float(input())
    day_counter += 1
    if doing == "spend":
        spending_day += 1
        money_in_wallet -= current_money
        if money_in_wallet < 0:
            money_in_wallet = 0
        if spending_day == 5:
            break
    else:
        money_in_wallet += current_money
        spending_day = 0
        if money_in_wallet >= needed_money:
            is_save_money = True
if is_save_money:
    print(f"You saved the money for {day_counter} days.")
else:
    print("You can't save the money.")
    print(f"{day_counter}")
