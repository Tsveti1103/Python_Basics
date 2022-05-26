lilly_age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())
toy_count = 0
money_spend = 0
birthday_money = 9

for age in range(1, lilly_age + 1):
    if age % 2 == 0:
        money_spend = money_spend + birthday_money
        birthday_money = birthday_money + 10
    else:
        toy_count = toy_count + 1
total_toys_price = toy_count * single_toy_price
final_money = money_spend + total_toys_price
if final_money >= washing_machine_price:
    money_left = final_money - washing_machine_price
    print(f"Yes! {money_left:.2f}")
else:
    needed_money = washing_machine_price - final_money
    print(f"No! {needed_money:.2f}")
