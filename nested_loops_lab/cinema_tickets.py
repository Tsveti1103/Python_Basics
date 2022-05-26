movie_name = input()
student_cnt = 0
standard_cnt = 0
kid_cnt = 0
while not movie_name == "Finish":
    free_seats = int(input())
    taken_seats = 0
    for i in range(free_seats):
        current_ticket = input()
        if current_ticket == "student":
            student_cnt += 1
        elif current_ticket == "standard":
            standard_cnt += 1
        elif current_ticket == "kid":
            kid_cnt += 1
        elif current_ticket == "End":
            break
        taken_seats += 1
    print(f"{movie_name} - {taken_seats / free_seats * 100:.2f}% full.")
    movie_name = input()
total_tickets = standard_cnt + kid_cnt + student_cnt
print(f"Total tickets: {total_tickets}")
print(f"{student_cnt / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_cnt / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_cnt / total_tickets * 100:.2f}% kids tickets.")
