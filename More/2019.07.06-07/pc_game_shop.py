number_sale_games = int(input())
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
other_counter = 0
for _ in range(number_sale_games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_counter += 1
    elif game_name == "Fornite":
        fornite_counter +=1
    elif game_name == "Overwatch":
        overwatch_counter +=1
    else:
        other_counter +=1
percentage_heaethstone = hearthstone_counter / number_sale_games * 100
percentage_fornite = fornite_counter / number_sale_games * 100
percentage_overwatch = overwatch_counter / number_sale_games * 100
percentage_others = other_counter / number_sale_games * 100

print(f"Hearthstone - {percentage_heaethstone:.2f}%")
print(f"Fornite - {percentage_fornite:.2f}%")
print(f"Overwatch - {percentage_overwatch:.2f}%")
print(f"Others - {percentage_others:.2f}%")
