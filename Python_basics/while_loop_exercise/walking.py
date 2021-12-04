steps = 0
while steps < 10000:
    current_steps = input()
    if current_steps == "Going home":
        current_steps = int(input())
        steps += current_steps
        if steps < 10000:
            print(f"{10000 - steps} more steps to reach goal.")
        else:
            print("Goal reached! Good job!")
            print(f"{steps - 10000} steps over the goal!")
        break
    steps += int(current_steps)
    if steps > 10000:
        print("Goal reached! Good job!")
        print(f"{steps - 10000} steps over the goal!")
