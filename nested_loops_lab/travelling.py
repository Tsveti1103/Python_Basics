destination = input()
while not destination == "End":
    target = float(input())
    money_saved = 0.0
    while money_saved < target:
        current_money = float(input())
        money_saved += current_money
    print(f"Going to {destination}!")
    destination = input()
