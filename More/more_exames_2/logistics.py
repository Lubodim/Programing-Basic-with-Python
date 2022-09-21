num_package_for_transport = int(input())

minibus_counter = 0
truck_counter = 0
train_counter = 0
cargo_counter = 0

for _ in range(num_package_for_transport):
    current_cargo_tons = int(input())
    cargo_counter +=current_cargo_tons
    if current_cargo_tons <= 3:
        minibus_counter += current_cargo_tons
    elif current_cargo_tons <= 11:
        truck_counter += current_cargo_tons
    elif current_cargo_tons > 11:
        train_counter += current_cargo_tons

average_price_per_ton = (minibus_counter * 200 + truck_counter *175 + train_counter * 120) / cargo_counter
minibus_percentage = minibus_counter / cargo_counter * 100
truck_percentage = truck_counter / cargo_counter * 100
train_percentage = train_counter / cargo_counter * 100

print(f"{average_price_per_ton:.2f}")
print(f"{minibus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
