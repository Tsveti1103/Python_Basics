budget = float(input())
season = input()
destination = ""
vacation_type = ""
spent_money = 0.0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = 0.3 * budget
        vacation_type = "Camp"
    elif season == "winter":
        spent_money = 0.7 * budget
        vacation_type = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = 0.4 * budget
        vacation_type = "Camp"
    elif season == "winter":
        spent_money = 0.8 * budget
        vacation_type = "Hotel"
elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    spent_money = 0.90 * budget
print(f"Somewhere in {destination}")
print(f"{vacation_type} - {spent_money:.2f}")
