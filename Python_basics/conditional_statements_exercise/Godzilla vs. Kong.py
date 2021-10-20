budget = float(input())
extras_count = int(input())
clothing_price = float(input())
decor = budget * 0.1
if extras_count > 150:
    clothing_price = clothing_price * 0.9
cost = extras_count * clothing_price + decor
if cost > budget:
    print("Not enough money!")
    needed_money = cost - budget
    print(f"Wingard needs {needed_money:.2f} leva more.")
elif cost <= budget:
    print("Action!")
    remaining_money = budget - cost
    print(f"Wingard starts filming with {remaining_money:.2f} leva left.")