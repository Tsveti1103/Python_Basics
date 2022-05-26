projection = input()
r = int(input())
c = int(input())
places = c * r
income = 0.0
if projection == "Premiere":
    income = places * 12
elif projection == "Normal":
    income = places * 7.50
elif projection == "Discount":
    income = places * 5
print(f"{income:.2f} leva")