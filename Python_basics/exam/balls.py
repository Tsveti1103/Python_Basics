import math

balls_count = int(input())
red_balls_counter = 0
orange_balls_counter = 0
yellow_balls_counter = 0
white_balls_counter = 0
other_balls_counter = 0
black_balls_counter = 0
points = 0
for i in range(balls_count):
    color = input()
    if color == "red":
        red_balls_counter += 1
        points += 5
    elif color == "orange":
        orange_balls_counter += 1
        points += 10
    elif color == "yellow":
        yellow_balls_counter += 1
        points += 15
    elif color == "white":
        white_balls_counter += 1
        points += 20
    elif color == "black":
        black_balls_counter += 1
        points = math.floor(points / 2)
    else:
        other_balls_counter += 1
print(f"Total points: {points}")
print(f"Points from red balls: {red_balls_counter}")
print(f"Points from orange balls: {orange_balls_counter}")
print(f"Points from yellow balls: {yellow_balls_counter}")
print(f"Points from white balls: {white_balls_counter}")
print(f"Other colors picked: {other_balls_counter}")
print(f"Divides from black balls: {black_balls_counter}")
