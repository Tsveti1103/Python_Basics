n = int(input())
average = 0
for i in range(n):
    number = int(input())
    average += number / n
print(f"{average:.2f}")
