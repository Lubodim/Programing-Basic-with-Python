current_ages_of_lily = int(input())
price_of_washing_machine = float(input())
price_per_toy = int(input())

save_money = 0
current_money = 0
toy_counter = 0
brother_money_counter = 0

for age in range(1, current_ages_of_lily + 1):
    if age % 2 == 0:
        current_money += 10
        save_money += current_money
        brother_money_counter +=1
    else:
        toy_counter += 1

save_money -= brother_money_counter
total_save_money = save_money + toy_counter * price_per_toy

difference = abs(total_save_money - price_of_washing_machine)
if total_save_money >= price_of_washing_machine:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
