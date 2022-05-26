n = int(input())
# left site
left_sum = 0
for i in range(0, n):
    current_number = int(input())
    left_sum = left_sum + current_number
# right site
right_sum = 0
for i in range(0, n):
    current_number = int(input())
    right_sum = right_sum + current_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
