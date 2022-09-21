from sys import maxsize

number = int(input())
min_size = maxsize
max_size = -maxsize

for _ in range(number):
    current_num_1 = int(input())
    current_num_2 = int(input())
    sum_of_current_num = current_num_2 + current_num_1
