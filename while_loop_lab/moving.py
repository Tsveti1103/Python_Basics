x = int(input())  # Широчина на свободното пространство
y = int(input())  # Дължина на свободното пространство
z = int(input())  # Височина на свободното пространство
apartment_place = x * y * z
package = input()
while package != "Done":
    package = int(package)
    apartment_place -= package
    if apartment_place <= 0:
        print(f"No more free space! You need {abs(apartment_place)} Cubic meters more.")
        break
    package = input()
if package == "Done":
    print(f"{apartment_place} Cubic meters left.")
