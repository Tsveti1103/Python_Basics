cargo_count = int(input())
price_minibus = 0
price_truck = 0
price_train = 0
cargo_weight_total = 0
price_for_ton = 0
cargo_weight_minibus = 0
cargo_weight_truck = 0
cargo_weight_train = 0
p1 = 0
p2 = 0
p3 = 0
for i in range(1, cargo_count + 1):
    cargo_weight = int(input())
    cargo_weight_total += cargo_weight
    if cargo_weight <= 3:
        price_minibus += cargo_weight * 200
        cargo_weight_minibus += cargo_weight
    elif 3 < cargo_weight < 12:
        price_truck += cargo_weight * 175
        cargo_weight_truck += cargo_weight
    else:
        price_train += cargo_weight * 120
        cargo_weight_train += cargo_weight
price_for_ton = (price_train + price_truck + price_minibus) / cargo_weight_total
p1 = cargo_weight_minibus / (cargo_weight_truck + cargo_weight_train + cargo_weight_minibus) * 100
p2 = cargo_weight_truck / (cargo_weight_truck + cargo_weight_train + cargo_weight_minibus) * 100
p3 = cargo_weight_train / (cargo_weight_truck + cargo_weight_train + cargo_weight_minibus) * 100
print(f"{price_for_ton:.2f}")
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
