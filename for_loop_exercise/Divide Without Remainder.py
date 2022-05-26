n = int(input())

group1_counter = 0  # делят се на 2 без остатък
group2_counter = 0  # делят се на 3 без остатък
group3_counter = 0  # делят се на 4 без остатък
for i in range(0, n):
    number = int(input())
    if number % 2 == 0:
        group1_counter += 1
    if number % 3 == 0:
        group2_counter += 1
    if number % 4 == 0:
        group3_counter += 1
p1 = group1_counter / n * 100
p2 = group2_counter / n * 100
p3 = group3_counter / n * 100
print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
