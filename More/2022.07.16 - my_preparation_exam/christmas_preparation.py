paper_number = int(input())
cloth_number = int(input())
glue = float(input())
percentage_discount = int(input())

total_sum = paper_number * 5.80 + cloth_number * 7.20 + glue * 1.20
total_sum -= (percentage_discount * total_sum / 100)
print(f"{total_sum:.3f}")
