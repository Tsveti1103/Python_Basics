import sys

n = int(input())
max_number = - sys.maxsize
for i in range(n):
    number = int(input())
    if max_number < number:
        max_number = number
print(max_number)
