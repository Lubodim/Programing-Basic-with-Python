deposit_sum = float(input())
term_deposit = int(input())
annual_interest = float(input())

term_deposit=term_deposit * 0.01

term_deposit_per_mount = deposit_sum * annual_interest / 12

sum = deposit_sum + term_deposit * term_deposit_per_mount

print(sum)
