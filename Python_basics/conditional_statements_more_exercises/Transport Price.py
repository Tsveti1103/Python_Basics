kilometers = int(input())
day_or_night = input()
if kilometers < 20 and day_or_night == "day":
    money = kilometers * 0.79 + 0.70
    print(f"{money:.2f}")
elif kilometers < 20 and day_or_night == "night":
    money = kilometers * 0.90 + 0.70
    print(f"{money:.2f}")
elif 100 > kilometers >= 20:
    money = kilometers * 0.09
    print(f"{money:.2f}")
elif kilometers >= 100:
    money = kilometers * 0.06
    print(f"{money:.2f}")
