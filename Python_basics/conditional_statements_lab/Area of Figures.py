geometric_shape = input()
if geometric_shape == "square":
    square_length = float(input())
    area = square_length**2
    print(f"{area:.3f}")
if geometric_shape == "rectangle":
    rectangle_length = float(input())
    rectangle_height = float(input())
    area = rectangle_height*rectangle_length
    print(f"{area:.3f}")
if geometric_shape == "circle":
    circle_radius = float(input())
    from math import pi
    area = pi*circle_radius**2
    print(f"{area:.3f}")
if geometric_shape=="triangle":
    triangle_length = float(input())
    triangle_height = float(input())
    area = triangle_length*triangle_height/2
    print(f"{area:.3f}")