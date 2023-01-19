text = input()
text_sum = 0
for i in text:
    if i == "a":
        text_sum += 1
    elif i == "e":
        text_sum += 2
    elif i == "i":
        text_sum += 3
    elif i == "o":
        text_sum += 4
    elif i == "u":
        text_sum += 5
print(text_sum)
