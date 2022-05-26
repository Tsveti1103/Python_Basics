hours = int(input())
minutes = int(input())
minutes += 15
if minutes > 59:
    minutes -= 60
    hours += 1
if hours > 23:
    hours -= 24
if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")