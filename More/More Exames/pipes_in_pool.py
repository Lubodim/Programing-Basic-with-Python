volume_swimminf_pool = int(input())
debit_p1_per_hour = int(input())
debit_p2_per_hour = int(input())
hours_worker_missing = float(input())

p1_total_debit = debit_p1_per_hour * hours_worker_missing
p2_total_debit = debit_p2_per_hour * hours_worker_missing

input_debit = p1_total_debit + p2_total_debit

p1_precent = p1_total_debit * 100 / input_debit    #смятане на процент от число - процент от цяло = част х 100 / цялото
p2_precent = p2_total_debit * 100 / input_debit
pool_percent = input_debit * 100 / volume_swimminf_pool

if volume_swimminf_pool >= input_debit:
    print(f"The pool is {pool_percent:.2f}% full. Pipe 1: {p1_precent:.2f}%. Pipe 2: {p2_precent:.2f}%.")
else:
    print(f"For {hours_worker_missing} hours the pool overflows with {input_debit - volume_swimminf_pool} liters.")
