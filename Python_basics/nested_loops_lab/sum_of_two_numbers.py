start = int(input())
stop = int(input())
magic_number = int(input())
counter = 0
flag = False
for i in range(start, stop + 1):
    for j in range(start, stop + 1):
        current_sum = i + j
        counter += 1
        if current_sum == magic_number:
            flag = True
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            break
    if flag:
        break
if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")
