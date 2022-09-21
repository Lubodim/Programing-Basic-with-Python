budget = float(input())
spend_money_counter = 0
product_counter = 0
while True:
    command = input()
    if command == "Stop":
        print(f"You bought {product_counter} products for {spend_money_counter:.2f} leva.")
        break
    current_price = float(input())

    product_counter += 1
    if product_counter % 3 == 0:
        current_price *= 0.5
    spend_money_counter += current_price
    if spend_money_counter > budget:
        break
if spend_money_counter > budget:
    print(f"You don't have enough money!")
    print(f"You need {abs(spend_money_counter - budget):.2f} leva!")