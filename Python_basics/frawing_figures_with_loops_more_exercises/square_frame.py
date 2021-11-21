n = int(input())
for i in range(1, n + 1):
    s = "+"
    d = "- "
    c = "|"
    if i == 1 or i == n:
        print(f"{s} {d * (n - 2)}{s}")
    elif 1 < i < n:
        print(f"{c} {d * (n - 2)}{c}")
