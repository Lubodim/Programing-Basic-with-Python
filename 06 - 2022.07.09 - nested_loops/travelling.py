destination = input()
budget = float(input())
current_money_counter = 0
go_to_trip = False
while destination != "end":
    while True:
        current_money = float(input())
        current_money_counter += current_money
        if current_money_counter > budget:
            go_to_trip = True
            current_money_counter = 0
        if go_to_trip:
            print(f"Going to {destination}!")
            destination = input()
            budget = float(input())
            go_to_trip = False
            break
