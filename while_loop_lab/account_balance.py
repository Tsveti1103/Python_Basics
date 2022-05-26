money = input()
balance = 0.0
while money != "NoMoreMoney":
    money = float(money)
    if money < 0:
        print("Invalid operation!")
        break
    balance += money
    print(f"Increase: {money:.2f}")
    money = input()
print(f"Total: {balance:.2f}")
