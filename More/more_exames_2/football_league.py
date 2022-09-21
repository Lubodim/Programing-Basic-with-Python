stadium_volume = int(input())
fen_number = int(input())
a_counter = 0
b_counter = 0
c_counter = 0
d_counter = 0

for _ in range(fen_number):
    current_sector = input()
    if current_sector == "A":
        a_counter += 1
    elif current_sector == "B":
        b_counter += 1
    elif current_sector == "V":
        c_counter += 1
    elif current_sector == "G":
        d_counter += 1

percentage_a = a_counter / fen_number * 100
percentage_b = b_counter / fen_number * 100
percentage_c = c_counter / fen_number * 100
percentage_d = d_counter / fen_number * 100
total_percentage = fen_number / stadium_volume * 100

print(f"{percentage_a:.2f}%")
print(f"{percentage_b:.2f}%")
print(f"{percentage_c:.2f}%")
print(f"{percentage_d:.2f}%")
print(f"{total_percentage:.2f}%")
