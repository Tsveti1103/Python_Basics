flowers = input()
amount_flowers = int(input())
budget = int(input())
price = 0.0
if flowers == "Roses" and amount_flowers <= 80:
    price = 5
elif flowers == "Roses" and amount_flowers > 80:
    price = 5 - 5 * 0.1
elif flowers == "Tulips" and amount_flowers <= 80:
    price = 2.8
elif flowers == "Tulips" and amount_flowers > 80:
    price = 2.8 - 2.8 * 0.15
elif flowers == "Dahlias" and amount_flowers <= 90:
    price = 3.8
elif flowers == "Dahlias" and amount_flowers > 90:
    price = 3.8 - 3.8 * 0.15
elif flowers == "Narcissus" and amount_flowers >= 120:
    price = 3
elif flowers == "Narcissus" and amount_flowers < 120:
    price = 3 + 3 * 0.15
elif flowers == "Gladiolus" and amount_flowers >= 80:
    price = 2.5
elif flowers == "Gladiolus" and amount_flowers < 80:
    price = 2.5 + 2.5 * 0.2
total_price = price * amount_flowers
if total_price > budget:
    needed_money = total_price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
else:
    more_money = budget - total_price
    print(f"Hey, you have a great garden with {amount_flowers} {flowers} and {more_money:.2f} leva left.")