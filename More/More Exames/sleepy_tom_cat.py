weekend_days = int(input())
tom_want_to_play = 30000
work_days = 365 - weekend_days

weekend_time_for_play = weekend_days * 127
work_days_time_for_play = work_days * 63

year_time_to_play = weekend_time_for_play + work_days_time_for_play

something = abs(tom_want_to_play - year_time_to_play)

hours = something // 60
minutes = something % 60

if year_time_to_play > tom_want_to_play:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
