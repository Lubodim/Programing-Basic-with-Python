total_needed_timing = int(input())
number_scenes = int(input())
time_fo_scene = int(input())

total_time = number_scenes * time_fo_scene + (total_needed_timing * 0.15)
difference = abs(total_time - total_needed_timing)
if total_needed_timing > total_time:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")