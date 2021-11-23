jury_count = int(input())
presentation_name = input()

average = 0
counter = 0
while presentation_name != "Finish":
    total_rating = 0
    for i in range(jury_count):
        rating = float(input())
        total_rating += rating

    current_average = total_rating / jury_count
    print(f"{presentation_name} - {current_average:.2f}.")

    average += current_average
    counter += 1
    presentation_name = input()

print(f"Student's final assessment is {average / counter:.2f}.")
