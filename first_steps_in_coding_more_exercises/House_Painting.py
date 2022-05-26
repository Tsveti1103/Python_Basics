x = float(input())  # house height
y = float(input())  # side wall length
h = float(input())  # height triangular wall
# green
door = 1.2 * 2
frond_back_area = 2 * x * x - door
windows = 1.5 * 1.5 * 2
side_area = 2 * x * y - windows
area = frond_back_area + side_area
green = area / 3.4
# red
rectangle_area = 2 * x * y
triangle_area = 2 * (x * h / 2)
area = rectangle_area + triangle_area
red = area / 4.3
print(f'{green:.2f}')
print(f'{red:.2f}')