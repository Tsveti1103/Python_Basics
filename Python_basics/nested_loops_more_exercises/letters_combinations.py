start_letter = input()
end_letter = input()
without_letter = input()
counter = 0
for first in range(ord(start_letter), ord(end_letter) + 1):
    for second in range(ord(start_letter), ord(end_letter) + 1):
        for third in range(ord(start_letter), ord(end_letter) + 1):
            if chr(first) != without_letter and chr(second) != without_letter and chr(third) != without_letter:
                counter += 1
                print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")
print(counter)
