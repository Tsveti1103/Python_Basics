n = int(input())
left_sum = 0
right_sum = 0
for i in range(0, n):
    left_number = float(input())
    left_sum += left_number
for i in range(0, n):
    right_number = float(input())
    right_sum += right_number
if left_sum == right_sum:
    print(f"Yes, Sum = {right_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
