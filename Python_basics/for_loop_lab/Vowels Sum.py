text = input()
sum = 0
for i in range(0, len(text)):
    symbol = text[i]
    if symbol == "a":
        sum = sum + 1
    elif symbol == "e":
        sum = sum + 2
    elif symbol == "i":
        sum = sum + 3
    elif symbol == "o":
        sum = sum + 4
    elif symbol == "u":
        sum = sum + 5
print(sum)
