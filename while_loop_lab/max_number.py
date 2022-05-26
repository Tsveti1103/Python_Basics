import sys

num = input()
max_number = -sys.maxsize
while num != "Stop":
    num = int(num)
    if max_number < num:
        max_number = num
    num = input()
print(max_number)
