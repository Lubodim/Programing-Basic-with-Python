number_input = int(input())
number_input = str(number_input)
for i in range(1, int(number_input[2]) + 1):
    for j in range(1, int(number_input[1]) + 1):
        for x in range(1, int(number_input[0]) + 1):
            if i > 0 and j > 0 and x > 0:
                num_sum = i * j * x
                print(f'{i} * {j} * {x} = {num_sum};')
