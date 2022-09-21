number_of_days = int(input())
number_of_hours = int(input())
price = 0
total_price = 0


for i in range(1, number_of_days + 1):
    total_sum_per_day = 0
    for j in range(1, number_of_hours + 1):
        if i % 2 == 0 and j % 2 != 0:
            price = 2.5
        elif i % 2 != 0 and j % 2 == 0:
            price = 1.25
        else:
            price = 1
        total_price += price
        total_sum_per_day += price
    print(f"Day: {i} - {total_sum_per_day:.2f} leva")

print(f"Total: {total_price:.2f} leva")