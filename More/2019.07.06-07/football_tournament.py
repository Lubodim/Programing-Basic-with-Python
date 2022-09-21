team_name = input()
number_play_machs = int(input())
win_counter = 0
equal_counter = 0
loss_counter = 0
points_counter = 0
for _ in range(number_play_machs):
    if number_play_machs == 0:
        break
    type_exit_of_mach = input()
    if type_exit_of_mach == "W":
        win_counter +=1
        points_counter += 3
    elif type_exit_of_mach == "D":
        equal_counter +=1
        points_counter += 1
    elif type_exit_of_mach == "L":
        loss_counter +=1
if number_play_machs == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    percentage_wins = win_counter / number_play_machs * 100
    print(f"{team_name} has won {points_counter} points during this season.")
    print("Total stats:")
    print(f"## W: {win_counter}")
    print(f"## D: {equal_counter}" )
    print(f"## L: {loss_counter}")
    print(f"Win rate: {percentage_wins:.2f}%")