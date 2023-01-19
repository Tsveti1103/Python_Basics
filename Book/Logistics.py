cargo_count = int(input())
price = 0
p_m = 0
p_t = 0
p_v = 0
total_cargo = 0
total_cargo_price = 0
for i in range(1, cargo_count + 1):
    cargo = int(input())
    total_cargo += cargo
    if cargo <= 3:
        p_m += cargo
        price = cargo * 200
    elif 3 < cargo <= 11:
        p_t += cargo
        price = cargo * 175
    elif cargo > 11:
        p_v += cargo
        price = cargo * 120
    total_cargo_price += price
print(f"{total_cargo_price / total_cargo:.2f}")
print(f"{p_m / total_cargo * 100:.2f}%")
print(f"{p_t / total_cargo * 100:.2f}%")
print(f"{p_v / total_cargo * 100:.2f}%")
