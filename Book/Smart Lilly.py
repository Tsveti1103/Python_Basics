age = int(input())
price_washing_machine = float(input())
toy_price = int(input())
money = 9
total_money = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        total_money += money
        money += 10
    elif i % 2 != 0:
        total_money += toy_price
if total_money >= price_washing_machine:
    print(f"Yes! {total_money - price_washing_machine:.2f}")
else:
    print(f"No! {price_washing_machine - total_money:.2f}")
