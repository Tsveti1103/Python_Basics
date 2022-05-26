chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
holiday = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2.0
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15
if holiday == "Y":
    chrysanthemums_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15
bouquet_price = chrysanthemums_price * chrysanthemums_count + roses_price * roses_count + tulips_price * tulips_count
if tulips_count > 7 and season == "Spring":
    bouquet_price *= 0.95
if roses_count >= 10 and season == "Winter":
    bouquet_price *= 0.90
if chrysanthemums_count + roses_count + tulips_count > 20:
    bouquet_price *= 0.80
print(f"{bouquet_price + 2:.2f}")
