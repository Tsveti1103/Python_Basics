stadium_capacity = int(input())
fans = int(input())
a_count = 0
b_count = 0
v_count = 0
g_count = 0
p_a = 0
p_b = 0
p_v = 0
p_g = 0
p_all = 0
for i in range(fans):
    sector = input()
    if sector == "A":
        a_count += 1
    elif sector == "B":
        b_count += 1
    elif sector == "V":
        v_count += 1
    elif sector == "G":
        g_count += 1

p_a = a_count / fans * 100
p_b = b_count / fans * 100
p_v = v_count / fans * 100
p_g = g_count / fans * 100
p_all = fans / stadium_capacity * 100
print(f"{p_a:.2f}%")
print(f"{p_b:.2f}%")
print(f"{p_v:.2f}%")
print(f"{p_g:.2f}%")
print(f"{p_all:.2f}%")
