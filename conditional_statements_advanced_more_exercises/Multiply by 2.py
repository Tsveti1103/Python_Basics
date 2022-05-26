import sys

for i in range(- sys.maxsize, sys.maxsize):
    number = float(input())
    if number >= 0:
        number *= 2
        print(f"Result: {number:.2f}")
    else:
        print("Negative number!")
        break
