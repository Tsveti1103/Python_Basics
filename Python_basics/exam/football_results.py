first_result = input()
second_result = input()
third_result = input()

win_cnt = 0
lost_cnt = 0
drawn_cnt = 0

home_result = int(first_result[0])
guest_result = int(first_result[2])
if home_result > guest_result:
    win_cnt += 1
elif home_result < guest_result:
    lost_cnt += 1
else:
    drawn_cnt += 1

home_result = int(second_result[0])
guest_result = int(second_result[2])
if home_result > guest_result:
    win_cnt += 1
elif home_result < guest_result:
    lost_cnt += 1
else:
    drawn_cnt += 1
home_result = int(third_result[0])
guest_result = int(third_result[2])
if home_result > guest_result:
    win_cnt += 1
elif home_result < guest_result:
    lost_cnt += 1
else:
    drawn_cnt += 1
print(f"Team won {win_cnt} games.")
print(f"Team lost {lost_cnt} games.")
print(f"Drawn games: {drawn_cnt}")
