amount = float(input())
input_currency = input()
output_currency = input()
bgn = 0
if input_currency == "USD":
    bgn = amount * 1.79549
elif input_currency == "EUR":
    bgn = amount * 1.95583
elif input_currency == "GBP":
    bgn = amount * 2.53405
elif input_currency == "BGN":
    bgn = amount
result = 0
if output_currency == "USD":
    result = bgn / 1.79549
elif output_currency == "EUR":
    result = bgn / 1.95583
elif output_currency == "GBP":
    result = bgn / 2.53405
elif output_currency == "BGN":
    result = bgn
print(f"{result:.2f}")