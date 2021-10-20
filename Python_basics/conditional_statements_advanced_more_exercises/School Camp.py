season = input()
gender = input()
students_count = int(input())
days_count = int(input())
sport = ""
price = 0.0
if season == "Winter":
    if gender == "girls":
        price = 9.60
        sport = "Gymnastics"
    elif gender == "boys":
        price = 9.60
        sport = "Judo"
    elif gender == "mixed":
        price = 10.0
        sport = "Ski"
elif season == "Spring":
    if gender == "girls":
        price = 7.20
        sport = "Athletics"
    elif gender == "boys":
        price = 7.20
        sport = "Tennis"
    elif gender == "mixed":
        price = 9.50
        sport = "Cycling"
elif season == "Summer":
    if gender == "girls":
        price = 15.0
        sport = "Volleyball"
    elif gender == "boys":
        price = 15.0
        sport = "Football"
    elif gender == "mixed":
        price = 20.0
        sport = "Swimming"
final_price = price * days_count * students_count
if 10 <= students_count < 20:
    final_price *= 0.95
elif 20 <= students_count < 50:
    final_price *= 0.85
elif students_count >= 50:
    final_price *= 0.5
print(f"{sport} {final_price:.2f} lv.")
