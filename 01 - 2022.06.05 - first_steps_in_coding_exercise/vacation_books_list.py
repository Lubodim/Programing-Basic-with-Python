number_of_pages = int(input())
pages_per_hour = int(input())
days_for_reeding = int(input())

time_for_reed_a_book = number_of_pages / pages_per_hour

hours_per_day_reeding = time_for_reed_a_book / days_for_reeding

print(int(hours_per_day_reeding))
