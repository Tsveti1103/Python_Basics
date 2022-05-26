import sys

min_number = sys.maxsize
max_number = -sys.maxsize
numbers = int(input())
for i in range(0, numbers):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    if current_number < min_number:
        min_number = current_number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
