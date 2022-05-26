degrees = int(input())
time_of_day = input()
outfit = ""
shoes = ""
if 10 <= degrees <= 18 and time_of_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif (10 <= degrees <= 18 and time_of_day == "Afternoon") or (
        18 < degrees <= 24 and time_of_day == "Morning") or time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
elif degrees >= 25 and time_of_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif (18 < degrees <= 24 and time_of_day == "Afternoon") or (degrees >= 25 and time_of_day == "Morning"):
    outfit = "T-Shirt"
    shoes = "Sandals"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
