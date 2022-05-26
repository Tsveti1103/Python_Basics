import math

year_type = input()
p = int(input())
h = int(input())
weekends_in_sofia = 48 - h
play_weekends = weekends_in_sofia * 3 / 4
play_holidays = p * 2 / 3
total = play_weekends + play_holidays + h
if year_type == "leap":
    total = total * 1.15
print(f"{math.floor(total)}")
