from math import ceil

serial_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4

free_time = break_time - (lunch_time + rest_time)

something = abs(episode_time - free_time)

if free_time >= episode_time:
    print(f"You have enough time to watch {serial_name} and left with {ceil(something)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(something)} more minutes.")
