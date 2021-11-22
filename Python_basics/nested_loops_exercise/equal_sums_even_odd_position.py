number1 = int(input())
number2 = int(input())
even_sum = 0
odd_sum = 0
for number in range(number1, number2 + 1):
    str_number = str(number)
    even_sum = int(str_number[1]) + int(str_number[3]) + int(str_number[5])
    odd_sum = int(str_number[0]) + int(str_number[2]) + int(str_number[4])
    if even_sum == odd_sum:
        print(number, end=" ")
