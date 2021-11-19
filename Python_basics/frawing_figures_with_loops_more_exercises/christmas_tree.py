n = int(input())
a = "*"
b = " "
c = " | "
for i in range(0, n + 1):
    print(f"{(n - i) * b}{i * a}{c}{i * a}{(n - i) * b}")
