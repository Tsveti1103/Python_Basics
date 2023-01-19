month = input()
days_count = int(input())
apartment_price = 0
studio_price = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if days_count > 14:
        studio_price *= 0.7
    elif days_count > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days_count > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
if days_count > 14:
    apartment_price *= 0.9
print(f"Apartment: {apartment_price * days_count:.2f} lv.")
print(f"Studio: {studio_price * days_count:.2f} lv.")
