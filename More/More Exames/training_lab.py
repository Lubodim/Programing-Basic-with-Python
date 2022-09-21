width_room = float(input())
height_room = float(input())

var: bool = 3 <= height_room <= width_room <= 100

width_room = width_room - 1

width_work_place = 1.2
height_work_place = 0.7

work_place_roll = height_room // height_work_place
work_place_colon = width_room // width_work_place

sum_work_place = int(work_place_roll * work_place_colon) - 3

print(sum_work_place)
