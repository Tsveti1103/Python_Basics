days = int(input())
total_wins = 0
total_loses = 0
total_money = 0
for i in range(days):
    current_wins = 0
    current_loses = 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            current_wins += 1
        elif result == "lose":
            current_loses += 1
        sport = input()
    current_money = current_wins * 20
    if current_wins > current_loses:
        current_money *= 1.1

    total_wins += current_wins
    total_loses += current_loses
    total_money += current_money
if total_wins > total_loses:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
