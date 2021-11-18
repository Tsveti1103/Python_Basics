student_count = int(input())
average_rating = 0.0
fail_count = 0
good_count = 0
very_good_count = 0
top_count = 0
fail_student = 0
good_student = 0
very_good_student = 0
top_student = 0
for i in range(1, student_count + 1):
    rating = float(input())
    average_rating += rating / student_count
    if rating < 3:
        fail_count += 1
    elif 3 <= rating < 4:
        good_count += 1
    elif 4 <= rating < 5:
        very_good_count += 1
    else:
        top_count += 1
fail_student = fail_count / student_count * 100
good_student = good_count / student_count * 100
very_good_student = very_good_count / student_count * 100
top_student = top_count / student_count * 100
print(f"Top students: {top_student:.2f}%")
print(f"Between 4.00 and 4.99: {very_good_student:.2f}%")
print(f"Between 3.00 and 3.99: {good_student:.2f}%")
print(f"Fail: {fail_student:.2f}%")
print(f"Average: {average_rating:.2f}")
