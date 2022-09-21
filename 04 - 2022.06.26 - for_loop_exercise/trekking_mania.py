group_number = int(input())

musala_climber = 0
monblan_climber = 0
kilimandjaro_climber = 0
k2_climber = 0
everest_climber = 0
total_group_size = 0
for _ in range(group_number):
    group_size = int(input())
    total_group_size += group_size
    if group_size <= 5:
        musala_climber += group_size
    elif group_size <= 12:
        monblan_climber += group_size
    elif group_size <= 25:
        kilimandjaro_climber += group_size
    elif group_size <= 40:
        k2_climber += group_size
    else:
        everest_climber += group_size

musala_climber_percentage = musala_climber / total_group_size * 100
monblan_climber_percentage = monblan_climber / total_group_size * 100
kilimandjaro_climber_percentage = kilimandjaro_climber / total_group_size * 100
k2_climber_percentage = k2_climber / total_group_size * 100
everest_climber_percentage = everest_climber / total_group_size * 100

print(f"{musala_climber_percentage:.2f}%")
print(f"{monblan_climber_percentage:.2f}%")
print(f"{kilimandjaro_climber_percentage:.2f}%")
print(f"{k2_climber_percentage:.2f}%")
print(f"{everest_climber_percentage:.2f}%")
