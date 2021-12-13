letter = ""
word = ""
counter_c = 0
counter_o = 0
counter_n = 0
new_word = ""
while letter != "End":
    letter = input()
    if letter == "End":
        break
    if letter == "c":
        counter_c += 1
        if counter_c > 1:
            word += letter
    elif letter == "o":
        counter_o += 1
        if counter_o > 1:
            word += letter
    elif letter == "n":
        counter_n += 1
        if counter_n > 1:
            word += letter
    elif "a" <= letter <= "z" or "A" <= letter <= "Z":
        word += letter
    if counter_o >= 1 and counter_n >= 1 and counter_c >= 1:
        word += " "
        counter_o = 0
        counter_n = 0
        counter_c = 0
        new_word = word
print(new_word)
