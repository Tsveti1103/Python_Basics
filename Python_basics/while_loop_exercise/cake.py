cake_width = int(input())
cake_length = int(input())
cake = cake_length * cake_width
peaces_count = 0
while peaces_count < cake:
    peaces = input()
    if peaces == "STOP":
        print(f"{cake - peaces_count} pieces are left.")
        break
    peaces_count += int(peaces)
if peaces_count >= cake:
    print(f"No more cake left! You need {peaces_count - cake} pieces more.")
