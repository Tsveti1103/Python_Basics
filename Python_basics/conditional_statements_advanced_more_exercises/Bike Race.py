juniors_count = int(input())
seniors_count = int(input())
track_type = input()
money = 0.0
if track_type == "trail":
    money = juniors_count * 5.5 + seniors_count * 7
elif track_type == "cross-country":
    money = juniors_count * 8 + seniors_count * 9.5
    if juniors_count + seniors_count >= 50:
        money = 0.75 * money
elif track_type == "downhill":
    money = juniors_count * 12.25 + seniors_count * 13.75
elif track_type == "road":
    money = juniors_count * 20 + seniors_count * 21.50
total_money = money * 0.95
print(f"{total_money:.2f}")
