n = int(input())
simbol1 = "*"
simbol2 = " "
p = 0
for i in range(1, n + 1):
    if i == 1 or i == n:
        p = simbol1 * n
        print(p)
    else:
        p = simbol2 * (n - 2)
        print(f"{simbol1}{p}{simbol1}")
