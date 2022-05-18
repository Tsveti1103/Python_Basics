budget = int(input())
season = input()
fishermen = int(input())
price = 0.0
if season == "Spring":
    price = 3000
elif season == "Summer":
    price = 4200
elif season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600
if fishermen <= 6:
    price *= 0.9
elif 7 <= fishermen <= 11:
    price *= 0.85
elif fishermen >= 12:
    price *= 0.75
if fishermen % 2 == 0 and season != "Autumn":
    price = 0.95 * price
if budget >= price:
    more_money = budget - price
    print(f"Yes! You have {more_money:.2f} leva left.")
else:
    needed_money = price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
