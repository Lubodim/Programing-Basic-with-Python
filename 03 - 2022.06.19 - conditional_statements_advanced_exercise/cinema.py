type_movie = input()
rows = int(input())
columns = int(input())

price = 0
volume = rows * columns

if type_movie == "Premiere":
    price = 12
elif type_movie == "Normal":
    price = 7.5
elif type_movie == "Discount":
    price = 5

income_sum = price * volume

print(f"{income_sum:.2f} leva")