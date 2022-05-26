price_strawberry = float(input())
amount_of_bananas = float(input())
amount_of_oranges = float(input())
amount_of_raspberries = float(input())
amount_of_strawberry = float(input())
price_raspberries = price_strawberry / 2
price_oranges = price_raspberries - 0.40 * price_raspberries
price_banannas = price_raspberries - 0.80 * price_raspberries
money = price_strawberry * amount_of_strawberry + amount_of_bananas * price_banannas + amount_of_oranges * price_oranges + amount_of_raspberries * price_raspberries
print(money)
