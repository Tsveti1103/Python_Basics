import math
hours_needed = int(input())
days = int(input())
workers_count = int(input())
training = days * 0.1
days_total = days-training
hours = days_total * 8
overtime = workers_count * days * 2
total = hours + overtime
total = math.floor(total)
if total>=hours_needed:
    more_hours = total - hours_needed
    print(f"Yes!{more_hours} hours left.")
else:
    less_hours = hours_needed-total
    print(f"Not enough time!{less_hours} hours needed.")