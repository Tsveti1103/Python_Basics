import sys

max_num = - sys.maxsize
n = int(input())
sum_of_elements = 0
for i in range(1, n + 1):
    number = int(input())
    sum_of_elements += number
    if number > max_num:
        max_num = number
sum_of_elements -= max_num
if sum_of_elements == max_num:
    print("Yes")
    print(f"Sum = {sum_of_elements}")
else:
    print("No")
    print(f"Diff = {abs(sum_of_elements - max_num)}")
