a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())
width = max(b1, b2) - min(b1, b2)
height = max(a1, a2) - min(a1, a2)
area = width * height
perimeter = 2 * (width + height)
print("area = " ,area)
print("perimeter = "  ,perimeter)