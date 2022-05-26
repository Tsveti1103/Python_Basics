n = int(input())
p1 = 0  # < 200
p2 = 0  # 200 … 399
p3 = 0  # 400 … 599
p4 = 0  # 600 … 799
p5 = 0  # ≥ 800
for i in range(1, n + 1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    else:
        p5 += 1
print(f"{(p1 / n * 100):.2f}%")
print(f"{(p2 / n * 100):.2f}%")
print(f"{(p3 / n * 100):.2f}%")
print(f"{(p4 / n * 100):.2f}%")
print(f"{(p5 / n * 100):.2f}%")
