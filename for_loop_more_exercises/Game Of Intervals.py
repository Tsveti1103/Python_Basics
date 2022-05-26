moves = int(input())
result = 0.0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
for i in range(1, moves + 1):
    number = int(input())
    if 0 <= number < 10:
        p1 += 1
        result += 0.2 * number
    elif 10 <= number < 20:
        p2 += 1
        result += 0.3 * number
    elif 20 <= number < 30:
        p3 += 1
        result += 0.4 * number
    elif 30 <= number < 40:
        p4 += 1
        result += 50
    elif 40 <= number <= 50:
        p5 += 1
        result += 100
    elif 0 > number or number > 50:
        p6 += 1
        result *= 0.5

print(f"{result:.2f}")
print(f"From 0 to 9: {p1 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 10 to 19: {p2 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 20 to 29: {p3 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 30 to 39: {p4 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"From 40 to 50: {p5 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
print(f"Invalid numbers: {p6 / (p1 + p2 + p3 + p4 + p5 + p6) * 100:.2f}%")
