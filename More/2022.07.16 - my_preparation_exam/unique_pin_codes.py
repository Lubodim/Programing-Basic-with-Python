top_border_n1 = int(input())
top_border_n2 = int(input())
top_border_n3 = int(input())
for i in range(1, top_border_n1 + 1):
    for j in range(1, top_border_n2 + 1):
        for x in range(1, top_border_n3 + 1):
            if i % 2 == 0:
                if j == 2 or j == 3 or j == 5 or j == 7:
                    if x % 2 == 0:
                        print(f"{i} {j} {x}")