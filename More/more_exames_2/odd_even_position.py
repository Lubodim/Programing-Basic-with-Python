from sys import maxsize

num = int(input())
odd_sum = 0
odd_min = float(maxsize)
odd_max = float(-maxsize)
even_sum = 0
even_min = float(maxsize)
even_max = float(-maxsize)

for i in range(1, num + 1):
    current_num = float(input())
    if i % 2 == 0:
        even_sum += current_num
        if even_min > current_num:
            even_min = current_num
        if even_max < current_num:
            even_max = current_num
    else:
        odd_sum += current_num
        if odd_min > current_num:
            odd_min = current_num
        if odd_max < current_num:
            odd_max = current_num
if odd_sum != 0:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin=No,")
    print(f"OddMax=No,")
if even_sum != 0:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
else:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
