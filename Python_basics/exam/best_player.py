player_name = ""
best_player = ""
max_goals = 0
while player_name != "END":
    player_name = input()
    if player_name == "END":
        break
    current_goals = int(input())
    if current_goals > max_goals:
        max_goals = current_goals
        best_player = player_name
    if max_goals >= 10:
        break
print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
