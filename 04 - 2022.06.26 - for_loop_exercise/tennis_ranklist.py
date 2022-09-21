from math import floor


tournament_number = int(input())
start_points = int(input())
current_points = 0
winner_counter = 0
for play in range(tournament_number):
    current_stage = input()
    if current_stage == "W":
        current_points += 2000
        winner_counter +=1
    elif current_stage == "F":
        current_points += 1200
    elif current_stage == "SF":
        current_points += 720

total_points = current_points + start_points
average_points = current_points / tournament_number
percentage_of_win = winner_counter / tournament_number * 100

print(f"Final points: {total_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percentage_of_win:.2f}%")
