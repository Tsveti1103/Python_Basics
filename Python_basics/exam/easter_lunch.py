sweet_bread = int(input())
eggs_box = int(input())
cookie = int(input())
eggs_paint = eggs_box * 12
sweet_bread_price = sweet_bread * 3.2
eggs_price = eggs_box * 4.35
cookie_price = cookie * 5.4
eggs_paint_price = eggs_paint * 0.15
total_price = eggs_price + sweet_bread_price + cookie_price + eggs_paint_price
print(f"{total_price:.2f}")
