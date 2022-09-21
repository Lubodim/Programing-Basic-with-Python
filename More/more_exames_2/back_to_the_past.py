heritage = float(input())  # наследство
year_to_live = int(input())
year_old_counter = 17
for num in range(1800, year_to_live + 1):
    year_old_counter += 1
    if num % 2 == 0:
        heritage -= 12000
    else:
        heritage -= 12000 + year_old_counter * 50

if heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.")
else:
    heritage = abs(heritage)
    print(f"He will need {heritage:.2f} dollars to survive.")
