import math
x = int(input())  # кв.м е лозето
y = float(input())  # грозде за един кв.м
z = int(input())  # нужни литри вино
workers_count = int(input())  # брой работници
harvest = x * y
wine = harvest * 0.4 / 2.5
if wine<z:
    not_enough_wine = z-wine
    print(f"It will be a tough winter! More {math.floor(not_enough_wine)} liters wine needed.")
elif wine>=z:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    remaining_wine = wine - z
    wine_for_worker = remaining_wine/workers_count
    print(f"{math.ceil(remaining_wine)} liters left -> {math.ceil(wine_for_worker)} liters per person.")