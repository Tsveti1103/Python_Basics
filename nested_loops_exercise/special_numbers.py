n = int(input())
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                if n % first == 0 and n % second == 0 and n % third == 0 and n % fourth == 0:
                    print(f"{first}{second}{third}{fourth}", end=" ")
