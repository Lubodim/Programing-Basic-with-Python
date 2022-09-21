naylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_of_work = int(input())


paint_needed = paint_needed + paint_needed * 0.1
naylon_needed = naylon_needed + 2

bags_price = 0.40
naylon_price = naylon_needed * 1.50
paint_price = paint_needed * 14.50
thinner_price = thinner_needed * 5.00

all_matirials_price = bags_price + naylon_price + paint_price + thinner_price
salary_per_hour = all_matirials_price * 30 / 100

all_costs = all_matirials_price + salary_per_hour * hours_of_work

print(all_costs)
