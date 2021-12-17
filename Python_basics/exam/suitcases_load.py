trunk_capacity = float(input())
used_volume = 0
counter = 0
data = input()

while data != "End":
    volume = float(data)
    counter += 1
    if counter % 3 == 0:
        volume *= 1.1
    if volume > trunk_capacity:
        counter -= 1
        break

    trunk_capacity -= volume
    data = input()
if data == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {counter} suitcases loaded.")
