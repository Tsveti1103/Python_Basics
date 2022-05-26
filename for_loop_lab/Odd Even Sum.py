n = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, n + 1):
    current_number = int(input())
    if i % 2 == 0:
        even_sum = even_sum + current_number
    else:
        odd_sum = odd_sum + current_number
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print("No")
    print(f"Diff = {diff}")
