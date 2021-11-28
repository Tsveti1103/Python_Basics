number = int(input())
for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                if first + second == third + fourth:
                    number_sum = first + second
                    if number % number_sum == 0:
                        print(f"{first}{second}{third}{fourth}", end=" ")
