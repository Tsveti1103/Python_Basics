month = input()
nights = int(input())
studio_price = 0
apartment_price = 0
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < nights <= 14:
        studio_price = 0.95 * studio_price
    elif nights > 14:
        studio_price = 0.7 * studio_price
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price = 0.8 * studio_price
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
if nights > 14:
    apartment_price = 0.9 * apartment_price
total_price_apartment = nights * apartment_price
total_price_studio = nights * studio_price
print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")
