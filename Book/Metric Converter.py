size = float(input())
fromMetric = input().lower()
toMetric = input().lower()
if fromMetric == "mm":
    size = size / 1000
elif fromMetric == "cm":
    size = size / 100
elif fromMetric == "mi":
    size = size / 0.000621371192
elif fromMetric == "in":
    size = size / 39.3700787
elif fromMetric == "km":
    size = size / 0.001
elif fromMetric == "ft":
    size = size / 3.2808399
elif fromMetric == "yd":
    size = size / 1.0936133
if toMetric == "mm":
    size = size * 1000
elif toMetric == "cm":
    size = size * 100
elif toMetric == "mi":
    size = size * 0.000621371192
elif toMetric == "in":
    size = size * 39.3700787
elif toMetric == "km":
    size = size * 0.001
elif toMetric == "ft":
    size = size * 3.2808399
elif toMetric == "yd":
    size = size * 1.0936133
elif toMetric == "m":
    size = size
print(f"{size} {toMetric}")