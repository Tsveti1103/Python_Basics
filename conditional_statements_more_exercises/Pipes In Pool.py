v = int(input())  # Обем на басейна в литри
p1 = int(input())  # дебит на първата тръба за час
p2 = int(input())  # дебит на втората тръба за час
h = float(input())  # часовете които работникът отсъства
liters_t1 = p1 * h
liters_t2 = p2 * h
total_liters = liters_t1 + liters_t2
if total_liters <= v:
    occupancy = total_liters / v * 100
    percentage_of_water1 = liters_t1 / total_liters * 100
    percentage_of_water2 = liters_t2 / total_liters * 100
    print(
        f"The pool is {occupancy:.2f}% full. Pipe 1: {percentage_of_water1:.2f}%. Pipe 2: {percentage_of_water2:.2f}%.")
elif total_liters > v:
    water_in_more = total_liters - v
    print(f"For {h:.2f} hours the pool overflows with {water_in_more:.2f} liters.")
