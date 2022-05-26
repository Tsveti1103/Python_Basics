change = float(input())
change_to_coins = int(change * 100)
coins_count = 0
while change_to_coins >= 1:
    if change_to_coins >= 200:
        change_to_coins -= 200

    elif change_to_coins >= 100:
        change_to_coins -= 100

    elif change_to_coins >= 50:
        change_to_coins -= 50

    elif change_to_coins >= 20:
        change_to_coins -= 20

    elif change_to_coins >= 10:
        change_to_coins -= 10

    elif change_to_coins >= 5:
        change_to_coins -= 5

    elif change_to_coins >= 2:
        change_to_coins -= 2


    elif change_to_coins >= 1:
        change_to_coins -= 1

    coins_count += 1
print(coins_count)
