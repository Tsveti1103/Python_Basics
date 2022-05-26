days = int(input())
room_type = input()
rating = input()
nights = days - 1
if room_type == "room for one person":
    price = 18 * nights
elif room_type == "apartment":
    price = 25 * nights
    if days < 10:
        price *= 0.7
    elif 10 <= days <= 15:
        price *= 0.65
    elif days > 15:
        price *= 0.5
elif room_type == "president apartment":
    price = 35 * nights
    if days < 10:
        price *= 0.9
    elif 10 <= days <= 15:
        price *= 0.85
    elif days > 15:
        price *= 0.8
if rating == "positive":
    price *= 1.25
elif rating == "negative":
    price *= 0.9
print(f"{price:.2f}")
