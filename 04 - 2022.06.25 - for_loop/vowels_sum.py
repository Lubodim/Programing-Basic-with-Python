txt = input()
a = 1
e = 2
i = 3
o = 4
u = 5

total_sum = 0

for ch in txt:
    if ch == "a":
        total_sum += a
    elif ch == "e":
        total_sum += e
    elif ch == "i":
        total_sum += i
    elif ch == "o":
        total_sum += o
    elif ch == "u":
        total_sum += u
print(total_sum)
