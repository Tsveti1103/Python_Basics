number1 = int(input())
number2 = int(input())
n_operator = input()
result = 0
even_odd = ""
if n_operator == "+" or n_operator == "-" or n_operator == "*":
    if n_operator == "+":
        result = number1 + number2
    elif n_operator == "-":
        result = number1 - number2
    elif n_operator == "*":
        result = number1 * number2
    if result % 2 == 0:
        even_odd = "even"
    else:
        even_odd = "odd"
    print(f"{number1} {n_operator} {number2} = {result} - {even_odd}")
if n_operator == "/" or n_operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    elif n_operator == "/":
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
    elif n_operator == "%":
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")
