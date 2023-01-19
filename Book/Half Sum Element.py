import sys

n = int(input())
number_sum = 0
max_number = - sys.maxsize
for i in range(n):
    number = int(input())
    if max_number < number:
        max_number = number
    number_sum += number
if number_sum == max_number * 2:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    dif = abs(number_sum - max_number*2)
    print("No")
    print(f"Diff = {dif}")
