import math
days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input()) / 1000
total_food = (dog_food + cat_food + turtle_food) * days
if food>=total_food:
    residue = food - total_food
    print(f"{math.floor(residue)} kilos of food left.")
else:
    shortage = total_food - food
    print(f"{math.ceil(shortage)} more kilos of food are needed.")