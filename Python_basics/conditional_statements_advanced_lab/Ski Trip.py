days = int(input())
room = input()
rating = input()
nights = days - 1
price = 0.0
if room == "room for one person":
    price = 18
elif room == "apartment":
    price = 25
    if days < 10:
        price = price * 0.7
    elif 10 <= days <= 15:
        price = price * 0.65
    else:
        price = price * 0.5
elif room == "president apartment":
    price = 35
    if days < 10:
        price = price * 0.9
    elif 10 <= days <= 15:
        price = price * 0.75
    else:
        price = price * 0.8
final_price = nights * price
if rating == "positive":
    final_price = final_price * 1.25
elif rating == "negative":
    final_price = final_price * 0.9
print(f"{final_price:.2f}")
