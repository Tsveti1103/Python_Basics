poor_grades = int(input())
fail_times = 0
problems_count = 0
score_total = 0
last_problem = ""
problem_name = ""
while poor_grades > fail_times:
    last_problem = problem_name
    problem_name = input()
    if problem_name == "Enough":
        print(f"Average score: {score_total / problems_count:.2f}")
        print(f"Number of problems: {problems_count}")
        print(f"Last problem: {last_problem}")
        break
    score = float(input())
    problems_count += 1
    score_total += score
    if score <= 4:
        fail_times += 1
    if fail_times == poor_grades:
        print(f"You need a break, {fail_times} poor grades.")
        break
