processor_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_count = int(input())
discount = float(input())
processor_price = processor_price - processor_price * discount
video_card_price = video_card_price - video_card_price * discount
price_dollars = processor_price + video_card_price + (ram_price * ram_count)
price_leva = price_dollars * 1.57
print(f"Money needed - {price_leva:.2f} leva.")
