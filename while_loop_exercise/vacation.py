trip_money = float(input())
owned_money = float(input())
days_counter = 0
spend_counter = 0
while owned_money < trip_money:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "spend":
        spend_counter += 1
        owned_money -= money
        if owned_money < 0:
            owned_money = 0
    elif command == "save":
        spend_counter = 0
        owned_money += money
    if spend_counter == 5:
        print("You can't save the money.")
        print(days_counter)
        break
    if owned_money >= trip_money:
        print(f"You saved the money for {days_counter} days.")
