budget = float(input())
category = input()
people = int(input())
ticket_price = 0.0
if category == "Normal":
    ticket_price = 249.99
elif category == "VIP":
    ticket_price = 499.99
if 1 <= people <= 4:
    budget = 0.25 * budget
elif 5 <= people <= 9:
    budget = 0.4 * budget
elif 10 <= people <= 24:
    budget = 0.5 * budget
elif 25 <= people <= 49:
    budget = 0.6 * budget
else:
    budget = 0.75 * budget
total_ticket_price = people * ticket_price
if budget >= total_ticket_price:
    more_money = budget - total_ticket_price
    print(f"Yes! You have {more_money:.2f} leva left.")
else:
    needed_money = total_ticket_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
