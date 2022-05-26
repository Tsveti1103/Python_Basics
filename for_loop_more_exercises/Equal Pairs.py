number = int(input())
sum = 0
sum_new = 0
difference = 0
max_difference = 0
for i in range(1, number + 1):
    number1 = int(input())
    number2 = int(input())
    sum = number1 + number2
    if i == 1:
        sum_new = sum
    if sum != sum_new:
        difference = abs(sum - sum_new)
        sum_new = sum
    if max_difference < difference:
        max_difference = difference
if max_difference == 0:
    print(f"Yes, value={sum}")
else:
    print(f"No, maxdiff={max_difference}")
