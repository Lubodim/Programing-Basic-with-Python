n = int(input())
roof = (n + 1) // 2

for i in range(1, roof + 1):
    if n % 2 != 0:
        if i == 1:
            print((((n - 1) // 2) * "-") + i * "*" + (((n - 1) // 2) * "-"))
        elif roof - i == 0:
            print(n * "*")
        else:
            print((((n - 2 * (i - 1)) // 2) * "-") + (i * 2 - 1) * "*" + (((n - 2 * (i - 1)) // 2) * "-"))
    if n % 2 == 0:
        if i == 1:
            print((((n - 1) // 2) * "-") + i * "**" + (((n - 1) // 2) * "-"))
        elif roof - i == 0:
            print(n * "*")
        else:
            print((((n - 2 * i) // 2) * "-") + (i * 2) * "*" + (((n - 2 * i) // 2) * "-"))
for j in range(n // 2):
    print("|" + ((n - 2) * "*") + "|")
