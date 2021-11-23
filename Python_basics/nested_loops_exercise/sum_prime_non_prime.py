number = input()
counter = 0
prime_sum = 0
non_prime_sum = 0
while number != "stop":
    if number == "stop":
        break
    int_number = int(number)
    if int_number < 0:
        print("Number is negative.")
        number = input()
        continue
    for divider in range(1, int_number + 1):
        if int_number % divider == 0:
            counter += 1
    if counter > 2:
        non_prime_sum += int_number
    else:
        prime_sum += int_number
    number = input()
    counter = 0
print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
