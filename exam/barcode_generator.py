begin = int(input())
finish = int(input())
begin = str(begin)
finish = str(finish)
for i in range(len(begin)):
    if i == 0:
        one_b = begin[0]
    elif i == 1:
        two_b = begin[1]
    elif i == 2:
        three_b = begin[2]
    elif i == 3:
        four_b = begin[3]
for j in range(len(finish)):

    if j == 0:
        one_f = finish[0]
    elif j == 1:
        two_f = finish[1]
    elif j == 2:
        three_f = finish[2]
    elif j == 3:
        four_f = finish[3]
for a in range(int(one_b), int(one_f) + 1):
    for b in range(int(two_b), int(two_f) + 1):
        for c in range(int(three_b), int(three_f) + 1):
            for d in range(int(four_b), int(four_f) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end=" ")
