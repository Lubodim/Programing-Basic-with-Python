current_record = float(input())
meeters_of_swim = float(input())
meeters_per_second = float(input())

water_delay = (meeters_of_swim // 15) * 12.5    # забавяне на водата

ivan_swim = meeters_of_swim * meeters_per_second + water_delay

something = abs(current_record - ivan_swim)

if ivan_swim < current_record:
    print(f" Yes, he succeeded! The new world record is {ivan_swim:.2f} seconds.")
else:
    print(f"No, he failed! He was {something:.2f} seconds slower.")
