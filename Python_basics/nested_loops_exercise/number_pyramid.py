n = int(input())
number = 1
for i in range(1, n + 1):
    for j in range(0, i):
        print(number, end=" ")
        number += 1
        if number > n:
            break
    if number > n:
        break
    print()
