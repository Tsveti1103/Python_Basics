start_number = int(input())
end_number = int(input())
for first in range(start_number, end_number + 1):
    for second in range(start_number, end_number + 1):
        for third in range(start_number, end_number + 1):
            for fourth in range(start_number, end_number + 1):
                if (first % 2 == 0 and fourth % 2 != 0) or (first % 2 != 0 and fourth % 2 == 0):
                    if first > fourth:
                        if (second + third) % 2 == 0:
                            print(f"{first}{second}{third}{fourth}",end=" ")