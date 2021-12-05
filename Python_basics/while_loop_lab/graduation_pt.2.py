name = input()
clas = 1
fail = 0
rating = 0.0
while clas <= 12:
    current_rating = float(input())
    if current_rating < 4:
        fail += 1
        if fail == 2:
            print(f"{name} has been excluded at {clas} grade")
            break
    else:
        clas += 1
        rating += current_rating
if fail != 2:
    print(f"{name} graduated. Average grade: {(rating / 12):.2f}")
