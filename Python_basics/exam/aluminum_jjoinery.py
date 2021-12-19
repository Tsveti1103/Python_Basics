joinery_count = int(input())  # 1.	Брой дограми – цяло число в интервала [0..1000];
joinery_type = input()  # 2.	Вид на дограмите – текст "90X130" или "100X150" или "130X180" или "200X300";
delivery = input()  # 3.	Начин на получаване – текст
price = 0
total_price = 0
if joinery_count < 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        price = 110 * joinery_count
        if 60 >= joinery_count > 30:
            price *= 0.95
        elif joinery_count > 60:
            price *= 0.92
    elif joinery_type == "100X150":
        price = 140 * joinery_count
        if joinery_count > 80:
            price *= 0.9
        elif joinery_count > 40:
            price *= 0.94
    elif joinery_type == "130X180":
        price = 190 * joinery_count
        if joinery_count > 50:
            price *= 0.88
        elif joinery_count > 20:
            price *= 0.93
    elif joinery_type == "200X300":
        price = 250 * joinery_count
        if joinery_count > 50:
            price *= 0.86
        elif joinery_count > 25:
            price *= 0.91
    if delivery == "With delivery":
        price += 60
    if joinery_count > 99:
        price *= 0.96

    print(f"{price:.2f} BGN")
