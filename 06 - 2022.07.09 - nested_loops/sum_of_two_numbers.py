start = int(input())
end = int(input())
magic_number = int(input())
combination_counter = 0
flag = False
for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        combination_counter += 1
        if n1 + n2 == magic_number:
            flag = True
            print(f"Combination N:{combination_counter} ({n1} + {n2} = {magic_number})")
            break
    if flag:
        break
if not flag:
    print(f"{combination_counter} combinations - neither equals {magic_number}")