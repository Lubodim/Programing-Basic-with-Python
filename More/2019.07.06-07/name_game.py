player_name = input()
point_counter = 0
win_counter = 0
win_name = ""
while player_name != "Stop":
    for ch in player_name:
        number = int(input())
        if number == ord(ch):
            point_counter += 10
        else:
            point_counter += 2
    if point_counter >= win_counter:
        win_counter = point_counter
        win_name = player_name
    point_counter = 0
    player_name = input()
else:
    print(f"The winner is {win_name} with {win_counter} points!")