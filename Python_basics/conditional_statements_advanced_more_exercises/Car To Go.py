budget = float(input())
season = input()
class_type = ""
car_type = ""
price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = 0.35 * budget
    elif season == "Winter":
        car_type = "Jeep"
        price = 0.65 * budget
if 500 >= budget > 100:
    class_type = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = 0.45 * budget
    elif season == "Winter":
        car_type = "Jeep"
        price = 0.80 * budget
if budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    price = 0.90 * budget
print(f"{class_type}")
print(f"{car_type} - {price:.2f}")
