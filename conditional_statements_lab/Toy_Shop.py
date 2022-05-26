trip_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_price = puzzles_count * 2.6
talking_dolls_price = talking_dolls_count * 3
teddy_bears_price = teddy_bears_count * 4.10
minions_price = minions_count * 8.20
trucks_price = trucks_count * 2
total_price = puzzles_price + talking_dolls_price + teddy_bears_price + minions_price + trucks_price
total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

if total_count >= 50:
    total_price = total_price * 0.75

total_price = total_price * 0.9
if total_price >= trip_price:
    money_left = total_price - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_need = trip_price - total_price
    print(f"Not enough money! {money_need:.2f} lv needed.")
