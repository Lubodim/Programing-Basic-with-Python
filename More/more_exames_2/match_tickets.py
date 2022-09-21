bugget = float(input())
ticket_type = input()
fens = int(input())

money_for_ticket = 0

if 1 <= fens <= 4:
    bugget *= 0.25
elif 5 <= fens <= 9:
    bugget *= 0.4
elif 10 <= fens <= 24:
    bugget *= 0.5
elif 25 <= fens <= 49:
    bugget *= 0.6
elif fens >= 50:
    bugget *= 0.75


if ticket_type == "VIP":
    money_for_ticket = fens * 499.99
else:
    money_for_ticket = fens * 249.99

difference = abs(money_for_ticket - bugget)

if bugget >= money_for_ticket:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
