budget = float(input())
season = input()
destination = ""
trip_type = ""
money_spend = 0.0
if budget <= 100:
    destination = "Somewhere in Bulgaria"
    if season == "summer":
        trip_type = "Camp"
        money_spend = budget * 0.3
    elif season == "winter":
        trip_type = "Hotel"
        money_spend = budget * 0.7
elif 100 < budget <= 1000:
    destination = "Somewhere in Balkans"
    if season == "summer":
        trip_type = "Camp"
        money_spend = budget * 0.4
    elif season == "winter":
        trip_type = "Hotel"
        money_spend = budget * 0.8
else:
    destination = "Somewhere in Europe"
    trip_type = "Hotel"
    money_spend = budget * 0.9
print(destination)
print(f"{trip_type} - {money_spend:.2f}")
