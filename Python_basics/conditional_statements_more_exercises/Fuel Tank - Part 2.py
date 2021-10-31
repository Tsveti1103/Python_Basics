fuel_type = input()
amount_fuel = int(input())
club_card = input()
price = 0
if fuel_type == "Gasoline":
    price = 2.22
    if club_card == "Yes":
        price = price-0.18
elif fuel_type == "Gas":
    price = 0.93
    if club_card == "Yes":
        price = price-0.08
elif fuel_type == "Diesel":
    price = 2.33
    if club_card == "Yes":
        price = price - 0.12
final_price = price*amount_fuel
if 20<=amount_fuel<=25:
        final_price = final_price*0.92
elif amount_fuel>25:
        final_price = final_price*0.90
print(f"{final_price:.2f} lv.")