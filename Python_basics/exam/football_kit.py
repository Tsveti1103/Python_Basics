shirt_price = float(input())
needed_price = float(input())
shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.2
buttons_price = 2 * (shirt_price + shorts_price)
total_price = shirt_price + shorts_price + socks_price + buttons_price
after_discount = total_price * 0.85
if after_discount >= needed_price:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {after_discount:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.")
    money_need = needed_price - after_discount
    print(f"He needs {money_need:.2f} lv. more.")
