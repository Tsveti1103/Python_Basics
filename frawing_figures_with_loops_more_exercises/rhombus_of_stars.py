n = int(input())
s = " *"
d = " "
a = "*"
for i in range(1, n + 1):
    print(f"{(n - i) * d}{a}{(i - 1) * s}")
for j in range(n - 1, 0, -1):
    print(f"{(n - j) * d}{a}{(j - 1) * s}")
