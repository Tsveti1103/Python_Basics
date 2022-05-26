computers_count = int(input())
total_sales = 0
total_rating = 0
for i in range(computers_count):
    number = int(input())
    rating = number % 10
    total_rating += rating
    possible_sales = number // 10
    if rating == 2:
        sales = possible_sales * 0
        total_sales += sales
    elif rating == 3:
        sales = possible_sales * 0.5
        total_sales += sales
    elif rating == 4:
        sales = possible_sales * 0.7
        total_sales += sales
    elif rating == 5:
        sales = possible_sales * 0.85
        total_sales += sales
    elif rating == 6:
        sales = possible_sales
        total_sales += sales
total_rating = total_rating / computers_count
print(f"{total_sales:.2f}")
print(f"{total_rating:.2f}")
