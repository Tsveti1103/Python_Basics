number = int(input())
number_sum = 0
sum_new = 0
difference = 0
max_difference = 0
for i in range(1, number + 1):
    number1 = int(input())
    number2 = int(input())
    number_sum = number1 + number2
    if i == 1:
        sum_new = number_sum
    if number_sum != sum_new:
        difference = abs(number_sum - sum_new)
        sum_new = number_sum
    if max_difference < difference:
        max_difference = difference
if max_difference == 0:
    print(f"Yes, value={number_sum}")
else:
    print(f"No, maxdiff={max_difference}")
