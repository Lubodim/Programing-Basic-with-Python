needet_sum = int(input())
cash_sum = 0
cash_counter = 1
card_sum = 0
card_counter = 1
payment_counter = 0
average_cash_sum = cash_sum / cash_counter
average_card_sum = card_sum / card_counter
average_sum = average_card_sum + average_cash_sum
command = input()
while command != "End":
    command = int(command)
    payment_counter += 1
    if payment_counter % 2 != 0 and command > 100:
        print("Error in transaction!")
    elif payment_counter % 2 != 0 and command <= 100:
        print("Product sold!")
        cash_sum += command
        cash_counter += 1
    elif payment_counter % 2 == 0 and command < 10:
        print("Error in transaction!")
    elif payment_counter % 2 == 0 and command > 10:
        print("Product sold!")
        card_sum += command
        card_counter += 1
    if needet_sum <= average_sum:
        break
    command = input()

if command == "End":
    print("Failed to collect required money for charity.")
else:
    print(f"Average CS: {cash_sum:.2f}")
    print(f"Average CC: {card_sum:.2f}")
