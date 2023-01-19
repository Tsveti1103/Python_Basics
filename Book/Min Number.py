import sys

n = int(input())
min_number = sys.maxsize
for i in range(n):
    number = int(input())
    if min_number > number:
        min_number = number
print(min_number)