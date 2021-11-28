men_count = int(input())
women_count = int(input())
max_table_count = int(input())
table_counter = 0
for m in range(1, men_count + 1):
    for w in range(1, women_count + 1):
        print(f"({m} <-> {w})", end=" ")
        table_counter += 1
        if table_counter == max_table_count:
            break
    if table_counter == max_table_count:
        break
