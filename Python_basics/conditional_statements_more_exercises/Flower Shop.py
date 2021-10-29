import math
number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
price_of_gift = float(input())
total_price = number_of_magnolias * 3.25 + number_of_hyacinths * 4 + number_of_roses * 3.5 + number_of_cacti * 8
profit = total_price * 0.95
if profit >= price_of_gift:
    money_left = profit - price_of_gift
    print(f"She is left with {math.floor(money_left)} leva.")
else:
    needed_money = price_of_gift - profit
    print(f"She will have to borrow {math.ceil(needed_money)} leva.")