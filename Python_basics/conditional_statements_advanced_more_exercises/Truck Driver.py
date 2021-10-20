season = input()
kilometers = int(input())
salary = 0
if season == "Spring" or season == "Autumn":
    if kilometers <= 5000:
        salary = kilometers * 0.75
    elif 5000 < kilometers <= 10000:
        salary = kilometers * 0.95
elif season == "Summer":
    if kilometers <= 5000:
        salary = kilometers * 0.90
    elif 5000 < kilometers <= 10000:
        salary = kilometers * 1.1
elif season == "Winter":
    if kilometers <= 5000:
        salary = kilometers * 1.05
    elif 5000 < kilometers <= 10000:
        salary = kilometers * 1.25
if 10000 < kilometers <= 20000:
    salary = kilometers * 1.45
final_salary = salary * 0.9 * 4
print(f"{final_salary:.2f}")
