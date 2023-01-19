budget = float(input())
category = input()
people_count = int(input())
ticket_price = 0.0
total_ticket_price = 0.0
if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99
if 1 <= people_count < 5:
    budget *= 0.25
elif 5 <= people_count < 10:
    budget *= 0.4
elif 10 <= people_count < 25:
    budget *= 0.5
elif 25 <= people_count < 25:
    budget *= 0.6
elif 25 <= people_count < 50:
    budget *= 0.6
elif people_count >= 50:
    budget *= 0.75
total_ticket_price = ticket_price * people_count
if budget >= total_ticket_price:
    print(f"Yes! You have {abs(budget - total_ticket_price):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - total_ticket_price):.2f} leva.")
