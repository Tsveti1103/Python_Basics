first_up = int(input())
second_up = int(input())
third_up = int(input())

for f in range(2, first_up + 1, 2):
    for s in range(1, second_up + 1):
        for t in range(2, third_up + 1, 2):
            if 1 < s < 8:
                counter = 0
                for d in range(1, 8):
                    if s % d == 0:
                        counter += 1
                if counter <= 2:
                    print(f"{f} {s} {t}")
