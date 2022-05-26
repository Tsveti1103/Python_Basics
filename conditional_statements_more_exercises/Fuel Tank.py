fuel_type = input().lower()
liters_fuel = int(input())
if (fuel_type == "diesel" or fuel_type == "gasoline" or fuel_type == "gas") and liters_fuel < 25:
    print(f"Fill your tank with {fuel_type}!")
elif (fuel_type == "diesel" or fuel_type == "gasoline" or fuel_type == "gas") and liters_fuel >= 25:
    print(f"You have enough {fuel_type}.")
else:
    print("Invalid fuel!")