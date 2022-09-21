period_of_time = int(input())

doctors = 7
not_examined_counter = 0
examined_counter = 0

for time in range(1, period_of_time +1):
    number_of_patients = int(input())
    if time % 3 == 0:
        if not_examined_counter > examined_counter:
            doctors += 1
    if doctors >= number_of_patients:
        examined_counter += number_of_patients
    else:
        not_examined_counter += number_of_patients - doctors
        examined_counter += doctors


print(f"Treated patients: {examined_counter}.")
print(f"Untreated patients: {not_examined_counter}.")
