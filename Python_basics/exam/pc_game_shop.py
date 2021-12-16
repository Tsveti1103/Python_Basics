n = int(input())
hearthstone_cnt = 0
fornite_cnt = 0
overwatch_cnt = 0
other_cnt = 0
for i in range(n):
    game = input()
    if game == "Hearthstone":
        hearthstone_cnt += 1
    elif game == "Fornite":
        fornite_cnt += 1
    elif game == "Overwatch":
        overwatch_cnt += 1
    else:
        other_cnt += 1
print(f"Hearthstone - {hearthstone_cnt / n * 100:.2f}%")
print(f"Fornite - {fornite_cnt / n * 100:.2f}%")
print(f"Overwatch - {overwatch_cnt / n * 100:.2f}%")
print(f"Others - {other_cnt / n * 100:.2f}%")
